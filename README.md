# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [DeepSeek-v4-flash-vision-exp](https://api-docs.deepseek.com/guides/vision/) | ⭐ 185 | 💬 43 | [HN Thread](https://news.ycombinator.com/item?id=49386163) |
| **2** | [AI companies destroy physical books – let's scan rare books before it's too late](https://annas-archive.pk/blog/physical-destruction.html) | ⭐ 150 | 💬 92 | [HN Thread](https://news.ycombinator.com/item?id=49385994) |
| **3** | [TigerBeetle Core System Architecture: Deconstructing Performance Engineering](https://ixuvo.com/blog/tigerbeetle-core-system-architecture-performance-engineering) | ⭐ 41 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49386659) |
| **4** | [The Lost Treasure of Sid Meier's Pirates](https://remapradio.com/articles/the-lost-treasure-of-sid-meiers-pirates/) | ⭐ 150 | 💬 79 | [HN Thread](https://news.ycombinator.com/item?id=49384896) |
| **5** | [Small, native web tricks worth remembering](https://htmlcat.net/) | ⭐ 97 | 💬 23 | [HN Thread](https://news.ycombinator.com/item?id=49385860) |
| **6** | [Kino: A high-performance Ractor web server for Ruby 4.0](https://github.com/yaroslav/kino) | ⭐ 17 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49386383) |
| **7** | [We Rebuilt the Linux MicroVM Stack on Apple Silicon](https://encore.dev/blog/firecracker-apple-silicon) | ⭐ 113 | 💬 53 | [HN Thread](https://news.ycombinator.com/item?id=49384716) |
| **8** | [Flat Chair by Sara Paculdo](https://www.toxel.com/tech/2026/08/07/flat-chair-by-sara-paculdo/) | ⭐ 55 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=49331084) |
| **9** | [The August 17 outage](https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/) | ⭐ 578 | 💬 639 | [HN Thread](https://news.ycombinator.com/item?id=49378957) |
| **10** | [The Mystery of Dark Oxygen](https://www.newyorker.com/science/elements/the-mystery-of-dark-oxygen) | ⭐ 15 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49319733) |

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
