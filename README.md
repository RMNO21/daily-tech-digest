# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Kagi added a setting for removing paywalled links from search results](https://kagi.com/changelog#11296) | ⭐ 514 | 💬 188 | [HN Thread](https://news.ycombinator.com/item?id=49388154) |
| **2** | [AI companies destroy physical books – let's scan rare books before it's too late](https://annas-archive.pk/blog/physical-destruction.html) | ⭐ 612 | 💬 373 | [HN Thread](https://news.ycombinator.com/item?id=49385994) |
| **3** | [Omacom Foundation Launches with $8M](https://omarchy.org/news/2026/08/omacom-foundation-launches-with-8-million/) | ⭐ 41 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=49390132) |
| **4** | [DeepSeek-v4-flash-vision-exp](https://api-docs.deepseek.com/guides/vision/) | ⭐ 343 | 💬 114 | [HN Thread](https://news.ycombinator.com/item?id=49386163) |
| **5** | [I accidentally logged phone calls to military bases](https://lina.sh/blog/hijacking-e164-arpa) | ⭐ 145 | 💬 23 | [HN Thread](https://news.ycombinator.com/item?id=49387570) |
| **6** | [AI Boosted Homework Scores by 18% – Then Exam Scores Dropped 20%, Study Shows](https://canews24.online/?p=71) | ⭐ 60 | 💬 37 | [HN Thread](https://news.ycombinator.com/item?id=49389565) |
| **7** | [Cancer-Related Mortality Among US Pilots and Flight Attendants](https://jamanetwork.com/journals/jamainternalmedicine/article-abstract/2852504) | ⭐ 32 | 💬 15 | [HN Thread](https://news.ycombinator.com/item?id=49389524) |
| **8** | [c100](https://caligra.com/c100/) | ⭐ 74 | 💬 48 | [HN Thread](https://news.ycombinator.com/item?id=49389392) |
| **9** | [Felony Bench](https://www.felonybench.com/) | ⭐ 35 | 💬 13 | [HN Thread](https://news.ycombinator.com/item?id=49389430) |
| **10** | [WPD won't replace stolen Flock cameras, citing public trust](https://www.winonapost.com/news/wpd-wont-replace-stolen-flock-cameras-citing-public-trust/article_06a67859-2d97-414b-aa8f-d8751ad214bb.html) | ⭐ 36 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49388682) |

---

## 🗄️ News Archive

- 📅 [2026-08-21](archive/2026-08-21.md)
- 📅 [2026-08-20](archive/2026-08-20.md)
- 📅 [2026-08-19](archive/2026-08-19.md)
- 📅 [2026-08-18](archive/2026-08-18.md)
- 📅 [2026-08-17](archive/2026-08-17.md)
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
