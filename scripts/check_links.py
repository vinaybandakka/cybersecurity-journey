#!/usr/bin/env python3
"""Check every http(s) link in the repo's Markdown and YAML files.

YouTube links are checked through YouTube's oEmbed endpoint, because a deleted or private
video still returns HTTP 200 on its watch page. Everything else gets a GET with a browser
User-Agent. Exit code is 1 if any link is broken.

Usage: python3 scripts/check_links.py [--verbose]
"""
from __future__ import annotations

import concurrent.futures as cf
import re
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
            found.setdefault(url, set()).add(str(path.relative_to(ROOT)))
    return found


def check(url: str) -> tuple[str, bool, str]:
    s = requests.Session()
    s.headers.update({"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9",
                      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"})
    try:
        host = urllib.parse.urlparse(url).netloc
        if host.endswith("youtube.com") and ("/watch" in url or "/playlist" in url):
            r = s.get("https://www.youtube.com/oembed", params={"url": url, "format": "json"}, timeout=20)
            if r.status_code == 200:
                return url, True, f"youtube: {r.json().get('title', '')}"
            return url, False, f"youtube oembed {r.status_code}"
        if host.endswith("youtube.com") and "/@" in url:
            r = s.get(url, timeout=20)
            ok = r.status_code == 200 and '"channelId"' in r.text
            return url, ok, f"channel {r.status_code}"
        r = s.get(url, timeout=25, allow_redirects=True)
        if r.status_code < 400:
            return url, True, f"{r.status_code} -> {r.url}" if r.url != url else str(r.status_code)
        return url, False, f"HTTP {r.status_code}"
    except Exception as e:  # noqa: BLE001
        return url, False, f"error {type(e).__name__}: {e}"


def main() -> int:
    verbose = "--verbose" in sys.argv
    links = collect()
    print(f"Checking {len(links)} unique links...")
    bad = []
    with cf.ThreadPoolExecutor(max_workers=12) as ex:
        for url, ok, info in ex.map(check, sorted(links)):
            if not ok:
                bad.append((url, info))
                print(f"BROKEN  {url}  [{info}]  in {', '.join(sorted(links[url]))}")
            elif verbose:
                print(f"OK      {url}  [{info}]")
    print(f"\n{len(links) - len(bad)} ok, {len(bad)} broken")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
