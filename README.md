# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [FTL: A new operating system for clouds](https://ftl-os.org/) | ⭐ 64 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=49944912) |
| **2** | [Kolibri: A Sovereign Open-Weight Model](https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/) | ⭐ 253 | 💬 45 | [HN Thread](https://news.ycombinator.com/item?id=49942706) |
| **3** | [Woking Electrical Control Room (2016)](http://www.darbiansphotography.com/woking-electrical-control-room-urbex) | ⭐ 88 | 💬 13 | [HN Thread](https://news.ycombinator.com/item?id=49938399) |
| **4** | [City building games have a Soul Problem pt.2](https://www.radical-elements.com/minor-epiphanies/city-building-games-have-a-soul-problem-pt2) | ⭐ 77 | 💬 70 | [HN Thread](https://news.ycombinator.com/item?id=49945323) |
| **5** | [Body Awareness in Goffin's Cockatoos](https://www.nature.com/articles/s41598-026-57500-7) | ⭐ 19 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49913106) |
| **6** | [C++ Insights – See your source code with the eyes of a Compiler](https://github.com/andreasfertig/cppinsights) | ⭐ 96 | 💬 15 | [HN Thread](https://news.ycombinator.com/item?id=49928361) |
| **7** | [Newgrounds.com – A community of games, music, and art](https://www.newgrounds.com/) | ⭐ 391 | 💬 110 | [HN Thread](https://news.ycombinator.com/item?id=49940394) |
| **8** | [RetailReady (YC W24) Is Hiring](https://www.ycombinator.com/companies/retailready/jobs/bFcgIe4-implementations) | ⭐ 1 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49945904) |
| **9** | [Court agrees with EFF: Utah's VPN law demands a technical impossibility](https://www.eff.org/deeplinks/2026/10/court-agrees-eff-utahs-vpn-law-demands-technical-impossibility) | ⭐ 744 | 💬 362 | [HN Thread](https://news.ycombinator.com/item?id=49927754) |
| **10** | [Mike Tomlin spent 12 years building a Minecraft city](https://www.nytimes.com/athletic/7648198/2026/10/01/mike-tomlin-minecraft-nfl-coach/) | ⭐ 611 | 💬 139 | [HN Thread](https://news.ycombinator.com/item?id=49925184) |

---

## 🗄️ News Archive

- 📅 [2026-10-03](archive/2026-10-03.md)
- 📅 [2026-10-02](archive/2026-10-02.md)
- 📅 [2026-10-01](archive/2026-10-01.md)
- 📅 [2026-09-30](archive/2026-09-30.md)
- 📅 [2026-09-29](archive/2026-09-29.md)
- 📅 [2026-09-28](archive/2026-09-28.md)
- 📅 [2026-09-27](archive/2026-09-27.md)
- 📅 [2026-09-26](archive/2026-09-26.md)
- 📅 [2026-09-25](archive/2026-09-25.md)
- 📅 [2026-09-24](archive/2026-09-24.md)
- 📅 [2026-09-22](archive/2026-09-22.md)
- 📅 [2026-09-21](archive/2026-09-21.md)
- 📅 [2026-09-20](archive/2026-09-20.md)
- 📅 [2026-09-19](archive/2026-09-19.md)

*... and [35 older editions in the archive folder](archive/)*

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
