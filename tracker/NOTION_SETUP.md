# Daily tracking in Notion

There are three ways to get the 60 days into Notion. Pick one.

| Option | Effort | Best for |
|---|---|---|
| A. Ask Claude in this project to create it | None | You have the Notion connector connected in Claude |
| B. Import the CSV | 5 minutes, no code | Quickest manual route |
| C. Sync script | 10 minutes once, then one command | Keeping Notion and the repo in sync, and pulling your progress back into git |

All three produce the same database: one row per day with these columns.

| Property | Type | Filled by |
|---|---|---|
| Name | Title | Plan |
| Day, Week | Number | Plan |
| Phase, Area | Select | Plan |
| Planned Date | Date | Plan (regenerate with a different start date, see below) |
| Status | Select: Not started, In progress, Done, Skipped | **You** |
| Done | Checkbox | **You** |
| Confidence | Number 1-5 | **You**, honestly. Anything under 3 gets redone on review day. |
| Minutes | Number | **You** |
| Outcome, Lab, SME Question, Deliverable, Resources | Text | Plan |
| Day Page | URL | Plan (links to the day's page in GitHub) |
| Notes | Text | **You** |

## Option A: let Claude do it

With the Notion connector connected, ask in this project: "Create the 60-day tracker in Notion from tracker/notion-tracker.csv." Claude creates the database with the right property types and all 60 rows.

## Option B: import the CSV

1. Download [`notion-tracker.csv`](notion-tracker.csv) (open it on GitHub and click **Download raw file**).
2. In Notion, open the page where you want the tracker, then **⋯ → Import → CSV**, and pick the file.
3. Notion imports every column as text. Change these property types (click the column header → **Edit property → Type**):
   - Day, Week, Confidence, Minutes → **Number**
   - Phase, Area, Status → **Select**
   - Planned Date → **Date**
   - Done → **Checkbox** (the "No" values become unchecked)
   - Day Page → **URL**
4. Add the views below.

## Option C: the sync script

1. Go to https://www.notion.so/profile/integrations, create an **internal integration**, and copy its secret.
2. Open the Notion page that will hold the tracker, then **⋯ → Connections → add your integration**.
3. Copy that page's ID: the 32-character string at the end of its URL.
4. Run:

   ```bash
   pip install requests
   export NOTION_TOKEN=ntn_xxx
   export NOTION_PARENT_PAGE_ID=<page id>
   python3 tracker/notion_sync.py push
   ```

   The first run creates the database and prints `export NOTION_DATABASE_ID=...`. Keep that value (for example in your shell profile) for later runs.
5. Any time:
   - `python3 tracker/notion_sync.py push` updates the plan columns if you edited `data/curriculum.yaml`. It never touches Status, Done, Confidence, Minutes or Notes on existing rows.
   - `python3 tracker/notion_sync.py pull` writes your progress to `tracker/progress.csv`. Commit it weekly so your GitHub history shows your consistency.

Keep the token out of git. It is only read from the environment.

## Recommended views

| View | Type | Set up |
|---|---|---|
| Today | Table | Filter: Planned Date is today, or Status is In progress |
| Board | Board | Group by Status |
| By phase | Table | Group by Phase, sort by Day |
| Calendar | Calendar | By Planned Date |
| Needs review | Table | Filter: Confidence less than 3 |

Useful formula property, **Days late**: `if(prop("Done"), 0, max(0, dateBetween(now(), prop("Planned Date"), "days")))`.

## Changing the start date

Dates start on 2026-11-09 by default. To start another day, or to skip weekends:

```bash
pip install pyyaml
python3 scripts/generate.py --start 2026-11-16 --weekends-off
```

That rewrites `notion-tracker.csv` and the day pages. Re-import, or run `notion_sync.py push`. Push does update Planned Date on existing rows.

## Daily routine (2 minutes)

1. Open the **Today** view and click **Day Page**.
2. Do the 45 minutes.
3. Commit your notes, then set Status, Done, Confidence, Minutes and a one-line note in Notion.
