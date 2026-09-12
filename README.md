# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Retrospectively Reverse-Engineering Apple's Neural Engine](https://eiln.github.io/posts/ane.html) | ⭐ 93 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49670032) |
| **2** | [IKEA made a mod for Skyrim [video]](https://www.youtube.com/watch?v=iZODN0QUgjI) | ⭐ 153 | 💬 26 | [HN Thread](https://news.ycombinator.com/item?id=49639647) |
| **3** | [A misalignment of AI in mathematics](https://mathandai.org/) | ⭐ 948 | 💬 909 | [HN Thread](https://news.ycombinator.com/item?id=49662371) |
| **4** | [I spent $220 on Google app ads and 60% of the installs were robots](https://dayzlegame.com/blog/google-ads-bot-farm/) | ⭐ 557 | 💬 294 | [HN Thread](https://news.ycombinator.com/item?id=49662990) |
| **5** | [Navier-Stokes Announcement](https://www.claymath.org/news/navier-stokes-announcement/) | ⭐ 179 | 💬 118 | [HN Thread](https://news.ycombinator.com/item?id=49668706) |
| **6** | [A Design Space Exploration of Async/Await](https://cel.cs.brown.edu/blog/design-space-async-await/) | ⭐ 297 | 💬 79 | [HN Thread](https://news.ycombinator.com/item?id=49626718) |
| **7** | [Great Lakes sturgeon may be 400 years old:Scientists rethinking how to save them](https://www.cbc.ca/news/canada/ontario-great-lakes-sturgeon-lifespan-study-9.7329250) | ⭐ 72 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=49624456) |
| **8** | [google.com/goto: Google's anti-scraping update](https://www.autom.dev/blog/google-search-goto-links) | ⭐ 449 | 💬 351 | [HN Thread](https://news.ycombinator.com/item?id=49668386) |
| **9** | [Usenet rewind archive search engine](https://www.usenet-rewind.com/) | ⭐ 66 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=49668777) |
| **10** | [Inverse Kinematics and Foot Locking](https://theorangeduck.com/page/inverse-kinematics-foot-locking) | ⭐ 50 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49595505) |

---

## 🗄️ News Archive

- 📅 [2026-09-12](archive/2026-09-12.md)
- 📅 [2026-09-11](archive/2026-09-11.md)
- 📅 [2026-09-10](archive/2026-09-10.md)
- 📅 [2026-09-09](archive/2026-09-09.md)
- 📅 [2026-09-08](archive/2026-09-08.md)
- 📅 [2026-09-07](archive/2026-09-07.md)
- 📅 [2026-09-06](archive/2026-09-06.md)
- 📅 [2026-09-05](archive/2026-09-05.md)
- 📅 [2026-09-04](archive/2026-09-04.md)
- 📅 [2026-09-03](archive/2026-09-03.md)
- 📅 [2026-09-02](archive/2026-09-02.md)
- 📅 [2026-09-01](archive/2026-09-01.md)
- 📅 [2026-08-31](archive/2026-08-31.md)
- 📅 [2026-08-30](archive/2026-08-30.md)

*... and [16 older editions in the archive folder](archive/)*

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
