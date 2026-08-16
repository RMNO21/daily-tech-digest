# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Claude: System Prompts](https://platform.claude.com/docs/en/release-notes/system-prompts) | ⭐ 98 | 💬 42 | [HN Thread](https://news.ycombinator.com/item?id=49319556) |
| **2** | [Firefox for iOS now has a native adblocker](https://support.mozilla.org/en-US/kb/block-ads-firefox-ios) | ⭐ 54 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=49319633) |
| **3** | [A SAT Attack on Tarski's High School Algebra Problem](https://arxiv.org/abs/2608.08421) | ⭐ 30 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=49268565) |
| **4** | [Does anyone run Postgres without PgBouncer?](https://brandur.org/fragments/postgres-without-pgbouncer) | ⭐ 49 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=49277952) |
| **5** | [Research papers using "kidney disappointment" instead of "kidney failure"](https://scholar.google.com/scholar?q=%22kidney+disappointment%22) | ⭐ 77 | 💬 33 | [HN Thread](https://news.ycombinator.com/item?id=49319389) |
| **6** | [Asus Bike Booster](https://www.asus.com/accessories/bike-booster/asus-oxiis/oxiis-intelligent-bike-booster/) | ⭐ 509 | 💬 354 | [HN Thread](https://news.ycombinator.com/item?id=49268580) |
| **7** | [Chestnut – eGPU dock with open-source firmware](https://hwbusters.com/news/comma-ai-egpu-dock-runs-open-source-firmware-249-bare-799-with-an-rx-9060/) | ⭐ 63 | 💬 16 | [HN Thread](https://news.ycombinator.com/item?id=49292385) |
| **8** | [Tasklet (YC P26) Is Hiring a Head of Design Engineering](https://tasklet.ai/careers/head-of-design-engineering) | ⭐ 1 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49319892) |
| **9** | [Asynchronous I/O in DuckDB: Work, Thread, Work](https://duckdb.org/2026/07/31/asynchronous-io) | ⭐ 215 | 💬 26 | [HN Thread](https://news.ycombinator.com/item?id=49243061) |
| **10** | [Superconducting monolayer cuprate with a single CuO2 plane](https://www.nature.com/articles/s41586-026-10857-1) | ⭐ 35 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49277153) |

---

## 🗄️ News Archive

- 📅 [2026-08-16](archive/2026-08-16.md)
- 📅 [2026-08-15](archive/2026-08-15.md)
- 📅 [2026-08-14](archive/2026-08-14.md)

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
python scraper.py
```

---

<div align="center">
  <sub>Maintained by <a href="https://github.com/RMNO21">RMNO21</a> • Powered by GitHub Actions & Hacker News API</sub>
</div>
