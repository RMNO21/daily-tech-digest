import os
import sys
import json
import random
import hashlib
import urllib.request
from datetime import datetime, timezone

HN_TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
ARCHIVE_DIR = "archive"
TOP_STORIES_COUNT = 10
HEADERS = {"User-Agent": "DailyTechDigest/1.0 (GitHub: RMNO21)"}

COMMIT_MESSAGES = [
    "feat: sync latest tech & AI news updates",
    "docs: update daily digests and breaking headlines",
    "chore: refresh latest news feeds",
    "feat: update top trending community discussions",
    "docs: refresh tech highlights and discussion threads",
    "chore: sync latest developer news snapshots",
    "feat: update breaking tech stories",
    "docs: update daily news digest"
]


def should_sync_now() -> bool:
    """Smart sync schedule: distributes updates naturally across the day."""
    if "--force" in sys.argv:
        return True

    now_utc = datetime.now(timezone.utc)
    date_str = now_utc.strftime("%Y-%m-%d")
    current_hour = now_utc.hour

    seed_val = int(hashlib.md5(date_str.encode()).hexdigest(), 16)
    rng = random.Random(seed_val)
    
    # Target updates between 4 and 12 slots per day
    daily_target = 4 + (seed_val % 9)
    available_hours = list(range(4, 24)) # Active global hours
    scheduled_hours = set(rng.sample(available_hours, daily_target))

    if current_hour in scheduled_hours:
        return True

    print(f"[{now_utc.strftime('%H:%M:%S')} UTC] Sync window inactive for hour {current_hour}. Next active cycle scheduled.")
    return False


def get_natural_commit_message() -> str:
    """Returns a natural, varied commit message based on current timestamp."""
    now_utc = datetime.now(timezone.utc)
    msg_idx = (now_utc.hour + now_utc.day) % len(COMMIT_MESSAGES)
    return COMMIT_MESSAGES[msg_idx]


def fetch_json(url: str, timeout: int = 15):
    """Fetch and parse JSON from a URL using urllib."""
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as response:
        if response.status == 200:
            return json.loads(response.read().decode("utf-8"))
    return None


def fetch_top_stories(limit: int = TOP_STORIES_COUNT):
    """Fetch top tech and AI stories from Hacker News API."""
    print(f"Fetching top {limit} stories from Hacker News API...")
    try:
        top_ids = fetch_json(HN_TOP_STORIES_URL)
        if not top_ids:
            print("Failed to retrieve story IDs.", file=sys.stderr)
            return []
        top_ids = top_ids[:limit]
    except Exception as e:
        print(f"Error fetching top stories: {e}", file=sys.stderr)
        return []

    stories = []
    for rank, item_id in enumerate(top_ids, start=1):
        try:
            data = fetch_json(HN_ITEM_URL.format(item_id=item_id), timeout=10)
            if not data:
                continue

            title = data.get("title", "Untitled Story").strip()
            hn_discussion_url = f"https://news.ycombinator.com/item?id={item_id}"
            article_url = data.get("url", hn_discussion_url).strip()
            score = data.get("score", 0)
            by = data.get("by", "anonymous")
            comments = data.get("descendants", 0)

            stories.append({
                "rank": rank,
                "id": item_id,
                "title": title,
                "url": article_url,
                "hn_url": hn_discussion_url,
                "score": score,
                "by": by,
                "comments": comments,
            })
            print(f"[{rank}/{limit}] Fetched: {title[:55]}...")
        except Exception as e:
            print(f"Error fetching story {item_id}: {e}", file=sys.stderr)

    return stories


def format_archive_content(today: str, stories: list) -> str:
    """Format markdown content for the daily archive file."""
    lines = [
        f"# 📰 Tech & AI News Digest — {today}",
        "",
        f"> Automatically generated on `{today}`.",
        "",
        "| # | Story & Link | Points | Comments | Discussion |",
        "|:---:|:---|:---:|:---:|:---:|",
    ]
    for s in stories:
        title_escaped = s["title"].replace("|", "\\|")
        lines.append(
            f"| **{s['rank']}** | [{title_escaped}]({s['url']}) | ⭐ {s['score']} | 💬 {s['comments']} | [HN Thread]({s['hn_url']}) |"
        )

    lines.extend([
        "",
        "---",
        "*Curated automatically from Hacker News Top Tech Stories.*",
        ""
    ])
    return "\n".join(lines)


def get_archive_list() -> list:
    """List all past archive files sorted in reverse chronological order."""
    if not os.path.exists(ARCHIVE_DIR):
        return []
    files = [f for f in os.listdir(ARCHIVE_DIR) if f.endswith(".md")]
    files.sort(reverse=True)
    return files


def generate_readme(today: str, stories: list, archive_files: list) -> str:
    """Generate the root README.md with highlights and archive index."""
    story_rows = []
    for s in stories:
        title_escaped = s["title"].replace("|", "\\|")
        story_rows.append(
            f"| **{s['rank']}** | [{title_escaped}]({s['url']}) | ⭐ {s['score']} | 💬 {s['comments']} | [HN Thread]({s['hn_url']}) |"
        )
    story_table = "\n".join(story_rows)

    # Archive links (show up to recent 14 days)
    archive_links = []
    for f in archive_files[:14]:
        date_label = f.replace(".md", "")
        archive_links.append(f"- 📅 [{date_label}](archive/{f})")
    
    archive_section = "\n".join(archive_links) if archive_links else "_No previous archives yet._"
    if len(archive_files) > 14:
        archive_section += f"\n\n*... and [{len(archive_files) - 14} older editions in the archive folder](archive/)*"

    readme_content = f"""# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
{story_table}

---

## 🗄️ News Archive

{archive_section}

---

## ⚙️ How It Works

```
┌───────────────────────────────┐
│ GitHub Actions Automation     │
└──────────────┬────────────────┘
               ▼
┌───────────────────────────────┐
│ scraper.py (Hacker News API)  │ Fetches Top Tech & AI Stories
└──────────────┬────────────────┘
               ▼
┌───────────────────────────────┐
│ Markdown Generator            │ Updates archive/ & README.md
└──────────────┬────────────────┘
               ▼
┌───────────────────────────────┐
│ Repository Sync               │ Preserves news records
└───────────────────────────────┘
```

1. **Workflow Trigger:** Automated GitHub Actions workflow executes on schedule and supports manual triggers.
2. **Data Aggregation:** `scraper.py` queries the official Hacker News API to retrieve top tech and AI stories.
3. **Archive Storage:** Archives historical snapshots in the `archive/` directory.
4. **Dashboard Generation:** Dynamically updates `README.md` with the latest stories and archive index.

---

## 🛠️ Local Development & Testing

```bash
# 1. Clone repository
git clone https://github.com/RMNO21/daily-tech-digest.git
cd daily-tech-digest

# 2. Run scraper (Zero dependencies, pure Python standard library)
python scraper.py --force
```

---

<div align="center">
  <sub>Maintained by <a href="https://github.com/RMNO21">RMNO21</a> • Powered by GitHub Actions & Hacker News API</sub>
</div>
"""
    return readme_content


def main():
    if not should_sync_now():
        sys.exit(0)

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    print(f"--- Starting Daily Tech Digest for {today} ---")
    
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    
    stories = fetch_top_stories(limit=TOP_STORIES_COUNT)
    if not stories:
        print("No stories fetched. Exiting.")
        return

    # 1. Save daily archive
    archive_path = os.path.join(ARCHIVE_DIR, f"{today}.md")
    archive_content = format_archive_content(today, stories)
    with open(archive_path, "w", encoding="utf-8") as f:
        f.write(archive_content)
    print(f"Saved daily archive to: {archive_path}")

    # 2. Re-index archives & update README.md
    archive_files = get_archive_list()
    readme_content = generate_readme(today, stories, archive_files)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    print("Updated README.md successfully.")


if __name__ == "__main__":
    main()
