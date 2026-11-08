#!/usr/bin/env python3
"""Check every http(s) link in the repo's Markdown and YAML files.

YouTube links are checked through YouTube's oEmbed endpoint, because a deleted or private
video still returns HTTP 200 on its watch page. Everything else gets a GET with a browser
User-Agent. Exit code is 1 if any link is broken.

Usage: python3 scripts/check_links.py [--verbose]
"""
from __future__ import annotations

import concurrent.futures as cf
import os
import re
import time
import sys
import urllib.parse
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
URL_RE = re.compile(r"https?://[^\s<>\"'`)\]|]+")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
SKIP_PREFIXES = (
    "http://localhost", "http://127.0.0.1", "https://localhost",
    "https://api.notion.com",  # API base, needs a token
    "https://github.com/vinaybandakka/cybersecurity-journey",  # this repo; files exist once merged
)
SKIP_DIRS = {".git", "node_modules", ".venv"}
# Sites behind bot protection that often answer 403/429 to CI runners even though they load fine
# in a browser. A failure here is reported as WARN (check it by hand) instead of failing the build.
BOT_PROTECTED = ("cloudflare.com", "tryhackme.com", "iso.org", "blogspot.com", "crt.sh", "youtube.com")
GH_REPO_RE = re.compile(r"^https://github\.com/([^/]+)/([^/#?]+)/?$")


def collect() -> dict[str, set[str]]:
    found: dict[str, set[str]] = {}
    for path in ROOT.rglob("*"):
        if path.suffix not in {".md", ".yaml", ".yml"} or any(p in SKIP_DIRS for p in path.parts):
            continue
        if path.name == "notion-tracker.csv":
            continue
        for url in URL_RE.findall(path.read_text(encoding="utf-8")):
            url = url.rstrip(".,;:")
            if url.startswith(SKIP_PREFIXES) or "<" in url or "{" in url:
                continue
            if "." not in urllib.parse.urlparse(url).netloc:  # lab hostnames like http://juice-shop:3000
                continue
            found.setdefault(url, set()).add(str(path.relative_to(ROOT)))
    return found


def _get(s: requests.Session, url: str, **kw) -> requests.Response:
    """GET with retries on rate limiting and transient server errors."""
    for attempt in range(4):
        r = s.get(url, timeout=25, **kw)
        if r.status_code not in (429, 500, 502, 503, 504):
            return r
        time.sleep(2 ** attempt * 2)
    return r


def check(url: str) -> tuple[str, str, str]:
    """Return (url, status, info) where status is OK, WARN or BROKEN."""
    s = requests.Session()
    s.headers.update({"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9",
                      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"})
    host = urllib.parse.urlparse(url).netloc
    protected = host.endswith(BOT_PROTECTED)
    try:
        if host.endswith("youtube.com") and ("/watch" in url or "/playlist" in url):
            r = _get(s, "https://www.youtube.com/oembed", params={"url": url, "format": "json"})
            if r.status_code == 200:
                return url, "OK", f"youtube: {r.json().get('title', '')}"
            return url, "BROKEN", f"youtube oembed {r.status_code}"
        if host.endswith("youtube.com") and "/@" in url:  # channel handle: YouTube answers 404 if it doesn't exist
            r = _get(s, url)
            if r.status_code == 200:
                return url, "OK", "youtube channel"
            return url, "BROKEN" if r.status_code == 404 else "WARN", f"youtube channel {r.status_code}"
        m = GH_REPO_RE.match(url)
        if m:  # github.com throttles anonymous page loads, so ask the API instead
            headers = {"Accept": "application/vnd.github+json"}
            if os.environ.get("GITHUB_TOKEN"):
                headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
            r = _get(s, f"https://api.github.com/repos/{m[1]}/{m[2]}", headers=headers)
            if r.status_code == 200:
                j = r.json()
                return url, "OK", "github repo" + (" (ARCHIVED)" if j.get("archived") else "")
            return url, "BROKEN", f"github api {r.status_code}"
        r = _get(s, url, allow_redirects=True)
        if r.status_code < 400:
            return url, "OK", f"{r.status_code} -> {r.url}" if r.url != url else str(r.status_code)
        if protected and r.status_code in (403, 429):
            return url, "WARN", f"HTTP {r.status_code} (bot protection, check in a browser)"
        return url, "BROKEN", f"HTTP {r.status_code}"
    except Exception as e:  # noqa: BLE001
        if protected:
            return url, "WARN", f"{type(e).__name__} (bot protection, check in a browser)"
        return url, "BROKEN", f"error {type(e).__name__}: {e}"


def main() -> int:
    verbose = "--verbose" in sys.argv
    links = collect()
    print(f"Checking {len(links)} unique links...")
    bad, warn = [], []
    with cf.ThreadPoolExecutor(max_workers=6) as ex:
        for url, status, info in ex.map(check, sorted(links)):
            if status == "BROKEN":
                bad.append(url)
                print(f"BROKEN  {url}  [{info}]  in {', '.join(sorted(links[url]))}")
            elif status == "WARN":
                warn.append(url)
                print(f"WARN    {url}  [{info}]")
            elif verbose:
                print(f"OK      {url}  [{info}]")
    print(f"\n{len(links) - len(bad) - len(warn)} ok, {len(warn)} need a manual browser check, {len(bad)} broken")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
