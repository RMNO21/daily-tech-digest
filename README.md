# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Xiaomi MiMo v2.6](https://mimo.xiaomi.com/mimo-v2-6) | ⭐ 391 | 💬 197 | [HN Thread](https://news.ycombinator.com/item?id=49792730) |
| **2** | [NASA’s Mars Sample Return mission is dead](https://www.science.org/content/article/nasa-s-mars-sample-return-mission-dead) | ⭐ 251 | 💬 183 | [HN Thread](https://news.ycombinator.com/item?id=49791939) |
| **3** | [Suspension of the de minimis administrative exemption for imports $800 or less](https://www.personalimportation.org/advocacy) | ⭐ 93 | 💬 48 | [HN Thread](https://news.ycombinator.com/item?id=49793322) |
| **4** | [Data Protection Commission fines Google €403M over processing of location data](https://www.dataprotection.ie/en/news-media/latest-news/data-protection-commission-fines-google-eu403-million-following-inquiry-googles-processing-location) | ⭐ 22 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49794354) |
| **5** | [Transformers Explained Visually](https://poloclub.github.io/transformer-explainer/) | ⭐ 134 | 💬 19 | [HN Thread](https://news.ycombinator.com/item?id=49792342) |
| **6** | [What Sun got wrong](https://bcantrill.dtrace.org/2026/09/20/what-sun-got-wrong/) | ⭐ 471 | 💬 260 | [HN Thread](https://news.ycombinator.com/item?id=49787436) |
| **7** | [Attention is all you have](https://alicegg.tech/2026/09/21/attention) | ⭐ 531 | 💬 152 | [HN Thread](https://news.ycombinator.com/item?id=49787726) |
| **8** | [AI coding has made CI a bottleneck, so we reworked ours to keep up](https://linear.app/now/ci-bottleneck-reworked) | ⭐ 108 | 💬 93 | [HN Thread](https://news.ycombinator.com/item?id=49792067) |
| **9** | [I don't want to read what you didn't write](https://blog.colinbreck.com/i-dont-want-to-read-what-you-didnt-write/) | ⭐ 64 | 💬 22 | [HN Thread](https://news.ycombinator.com/item?id=49794330) |
| **10** | [Divide by depth for instant 3D](https://gabrieloc.com/2026/09/15/perspective.html) | ⭐ 59 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49769561) |

---

## 🗄️ News Archive

- 📅 [2026-09-21](archive/2026-09-21.md)
- 📅 [2026-09-20](archive/2026-09-20.md)
- 📅 [2026-09-19](archive/2026-09-19.md)
- 📅 [2026-09-18](archive/2026-09-18.md)
- 📅 [2026-09-16](archive/2026-09-16.md)
- 📅 [2026-09-15](archive/2026-09-15.md)
- 📅 [2026-09-14](archive/2026-09-14.md)
- 📅 [2026-09-13](archive/2026-09-13.md)
- 📅 [2026-09-12](archive/2026-09-12.md)
- 📅 [2026-09-11](archive/2026-09-11.md)
- 📅 [2026-09-10](archive/2026-09-10.md)
- 📅 [2026-09-09](archive/2026-09-09.md)
- 📅 [2026-09-08](archive/2026-09-08.md)
- 📅 [2026-09-07](archive/2026-09-07.md)

*... and [24 older editions in the archive folder](archive/)*

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
