# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-2026-08-16-blue.svg)](#-todays-highlights-2026-08-16)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest (Git-Scraper)** powered entirely by **GitHub Actions**. Every day, this repository fetches trending technology and artificial intelligence highlights, creates a persistent date-stamped archive, updates the dashboard below, and commits changes directly.

---

## 🚀 Today's Highlights (2026-08-16)

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Semaglutide linked to lower predicted dementia risk](https://alz-journals.onlinelibrary.wiley.com/doi/10.1002/dad2.70432) | ⭐ 340 | 💬 236 | [HN Thread](https://news.ycombinator.com/item?id=49311651) |
| **2** | [ChatGPT lost 22 points of web share in a year](https://aicharts.grok.me/c/market-share) | ⭐ 12 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49315630) |
| **3** | [Cultivating a state of mind where new ideas are born (2023)](https://www.henrikkarlsson.xyz/p/good-ideas) | ⭐ 70 | 💬 19 | [HN Thread](https://news.ycombinator.com/item?id=49314235) |
| **4** | [AI in drug discovery – what it is, where we stand and the path forward](https://www.science.org/content/blog-post/so-how-ai-drug-discovery-doing-really) | ⭐ 84 | 💬 42 | [HN Thread](https://news.ycombinator.com/item?id=49313367) |
| **5** | [At-home test for infected ticks could improve Lyme Disease diagnosis](https://www.smithsonianmag.com/innovation/the-first-at-home-test-for-infected-ticks-could-improve-lyme-disease-diagnosis-180989235/) | ⭐ 210 | 💬 72 | [HN Thread](https://news.ycombinator.com/item?id=49310682) |
| **6** | [Abdominal fat predicts heart disease risk better than BMI](https://www.acc.org/about-acc/press-releases/2026/08/11/14/59/abdominal-fat-predicts-heart-disease-risk-better-than-bmi) | ⭐ 135 | 💬 99 | [HN Thread](https://news.ycombinator.com/item?id=49314403) |
| **7** | [RISC-V: They Should Have Known Better](https://dmitry.gr/?r=06.%20Thoughts&proj=12.%20RV) | ⭐ 224 | 💬 295 | [HN Thread](https://news.ycombinator.com/item?id=49298035) |
| **8** | [Tracking down a Zsh history data loss bug](https://michael.stapelberg.ch/posts/2026-08-09-zsh-history-truncation-bug/) | ⭐ 31 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49314579) |
| **9** | [AI has access to a vastly larger working memory than the human brain](https://davidepiffer.com/p/ai-isnt-outthinking-mathematicians) | ⭐ 406 | 💬 362 | [HN Thread](https://news.ycombinator.com/item?id=49312845) |
| **10** | [Super El Niño Keeps Growing as New Forecasts Reach Record Territory Ahead Winter](https://www.severe-weather.eu/long-range-2/super-el-nino-growth-accelerating-to-record-strength-fall-winter-2026-2027-forecast-impact-united-states-canada-europe-fa/) | ⭐ 57 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=49313428) |

---

## 🗄️ Recent Archives

- 📅 [2026-08-16](archive/2026-08-16.md)
- 📅 [2026-08-15](archive/2026-08-15.md)
- 📅 [2026-08-14](archive/2026-08-14.md)

---

## ⚙️ How It Works

```
┌───────────────────────────────┐
│ GitHub Actions Cron (Every 6h)│ 00:00, 06:00, 12:00, 18:00 UTC
└──────────────┬────────────────┘
               ▼
┌───────────────────────────────┐
│ scraper.py (Hacker News API)  │ Fetches Top Tech & AI Stories
└──────────────┬────────────────┘
               ▼
┌───────────────────────────────┐
│ Markdown Generator            │ Updates archive/2026-08-16.md & README.md
└──────────────┬────────────────┘
               ▼
┌───────────────────────────────┐
│ Git Auto-Commit & Push        │ Signed with RMNO21 identity
└───────────────────────────────┘
```

1. **Scheduled Trigger:** GitHub Actions runs every 6 hours (`00:00`, `06:00`, `12:00`, `18:00` UTC) and supports manual triggering via `workflow_dispatch`.
2. **Data Scraping:** `scraper.py` queries Hacker News API for the highest-ranked stories and discussions.
3. **Archive Generation:** Saves a full snapshot into `archive/YYYY-MM-DD.md`.
4. **Dashboard Update:** Re-renders this `README.md` with live highlights and table of contents.
5. **Auto Commit & Push:** Commits changes using the author's verified credentials, contributing to the GitHub activity graph.

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
  <sub>Maintained automatically by <a href="https://github.com/RMNO21">RMNO21</a> • Powered by GitHub Actions & Hacker News API</sub>
</div>
