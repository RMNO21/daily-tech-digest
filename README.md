# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [MiMo v2.6](https://mimo.xiaomi.com/mimo-v2-6) | ⭐ 689 | 💬 326 | [HN Thread](https://news.ycombinator.com/item?id=49792730) |
| **2** | [Spymarks, Not Watermarks](https://brand.io/article/spymarks/) | ⭐ 244 | 💬 45 | [HN Thread](https://news.ycombinator.com/item?id=49794615) |
| **3** | [Transformers Explained Visually](https://poloclub.github.io/transformer-explainer/) | ⭐ 275 | 💬 42 | [HN Thread](https://news.ycombinator.com/item?id=49792342) |
| **4** | [What Sun got wrong](https://bcantrill.dtrace.org/2026/09/20/what-sun-got-wrong/) | ⭐ 541 | 💬 313 | [HN Thread](https://news.ycombinator.com/item?id=49787436) |
| **5** | [Attention is all you have](https://alicegg.tech/2026/09/21/attention) | ⭐ 659 | 💬 198 | [HN Thread](https://news.ycombinator.com/item?id=49787726) |
| **6** | [I don't want to read what you didn't write](https://blog.colinbreck.com/i-dont-want-to-read-what-you-didnt-write/) | ⭐ 461 | 💬 159 | [HN Thread](https://news.ycombinator.com/item?id=49794330) |
| **7** | [PDF Forgeries Are Surprisingly Rare (2022)](https://gwern.net/blog/2022/pdf-forgery) | ⭐ 14 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=49774269) |
| **8** | [NASA’s Mars Sample Return mission is dead](https://www.science.org/content/article/nasa-s-mars-sample-return-mission-dead) | ⭐ 345 | 💬 283 | [HN Thread](https://news.ycombinator.com/item?id=49791939) |
| **9** | [Claude Status – Elevated errors for multiple models](https://status.claude.com/incidents/7g1qpkyz5gxh) | ⭐ 83 | 💬 62 | [HN Thread](https://news.ycombinator.com/item?id=49795579) |
| **10** | [AI coding has made CI a bottleneck, so we reworked ours to keep up](https://linear.app/now/ci-bottleneck-reworked) | ⭐ 178 | 💬 184 | [HN Thread](https://news.ycombinator.com/item?id=49792067) |

---

## 🗄️ News Archive

- 📅 [2026-09-22](archive/2026-09-22.md)
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

*... and [25 older editions in the archive folder](archive/)*

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
