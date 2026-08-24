# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [SeL4 security proofs now complete on AArch64](https://proofcraft.systems/news-2026/#2026-08-21) | ⭐ 39 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=49418255) |
| **2** | [Omakase Computing](https://learn.omacom.io/3/omacom/76/omakase-computing) | ⭐ 36 | 💬 32 | [HN Thread](https://news.ycombinator.com/item?id=49418117) |
| **3** | [I were 17, I'd learn how to build LLMs from scratch](https://twitter.com/paulg/status/2091544343589060625) | ⭐ 245 | 💬 355 | [HN Thread](https://news.ycombinator.com/item?id=49412396) |
| **4** | [Everything I own, owned](https://schlarp.com/posts/everything-i-own-owned/) | ⭐ 1077 | 💬 294 | [HN Thread](https://news.ycombinator.com/item?id=49413320) |
| **5** | [The Future Belongs to the Weird](https://essays.georgestrakhov.com/weird/) | ⭐ 49 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=49416953) |
| **6** | [FDA clears blood test to aid evaluation for Alzheimer's disease](https://medicine.washu.edu/news/fda-clears-blood-test-to-aid-evaluation-for-alzheimers-disease/) | ⭐ 80 | 💬 28 | [HN Thread](https://news.ycombinator.com/item?id=49415893) |
| **7** | [Executable Is a SQLite Database](https://fzakaria.com/2026/08/23/your-executable-is-a-sqlite-database) | ⭐ 179 | 💬 23 | [HN Thread](https://news.ycombinator.com/item?id=49415271) |
| **8** | [Agent Is Not the Model](https://code.joejag.com/2026/your-agent-is-not-the-model.html) | ⭐ 10 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49418163) |
| **9** | [Anthropic's best AI model struggles to attract users as cheaper tools thrive](https://www.ft.com/content/5ee49718-c258-4f01-aa32-7e5b76ae5245) | ⭐ 599 | 💬 533 | [HN Thread](https://news.ycombinator.com/item?id=49411102) |
| **10** | [Fast drilldown dashboards from a single Parquet file](https://www.hamiltonulmer.com/customer-dashboards-r2-hyparquet/) | ⭐ 51 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49416652) |

---

## 🗄️ News Archive

- 📅 [2026-08-24](archive/2026-08-24.md)
- 📅 [2026-08-23](archive/2026-08-23.md)
- 📅 [2026-08-22](archive/2026-08-22.md)
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
