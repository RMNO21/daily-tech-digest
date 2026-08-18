# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [How Bluesky draws its logo on screenshots](https://timmarinin.net/2026/bluesky-screenshots/) | ⭐ 467 | 💬 323 | [HN Thread](https://news.ycombinator.com/item?id=49338459) |
| **2** | [GPT-5.6 Sol Pricing Cut by 50%](https://openrouter.ai/openai/gpt-5.6-sol) | ⭐ 411 | 💬 242 | [HN Thread](https://news.ycombinator.com/item?id=49337602) |
| **3** | [Quake Shareware, a CD-ROM just a little too full](https://fabiensanglard.net/quake_shareware_cd/index.html) | ⭐ 321 | 💬 134 | [HN Thread](https://news.ycombinator.com/item?id=49338328) |
| **4** | [Fairphone 6 and PostmarketOS working main camera](https://catcrafts.net/posts/fairphone-6-postmarketos-working-main-camera) | ⭐ 176 | 💬 41 | [HN Thread](https://news.ycombinator.com/item?id=49338285) |
| **5** | [A Preview of DuckDB v2.0](https://duckdb.org/2026/08/17/duckdb-20-highlights) | ⭐ 624 | 💬 112 | [HN Thread](https://news.ycombinator.com/item?id=49330781) |
| **6** | [The Benchmarkpocalypse](https://danluu.com/benchpocalypse/) | ⭐ 83 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=49340299) |
| **7** | [Ranking the Most Brilliantly Colored Birds with Data](https://moultano.wordpress.com/2026/08/14/fairly-ranking-the-most-brilliant-birds/) | ⭐ 11 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49311115) |
| **8** | [Shattered skeleton is first confirmed death from trebuchet](https://www.science.org/content/article/shattered-skeleton-scottish-castle-first-confirmed-death-trebuchet) | ⭐ 63 | 💬 42 | [HN Thread](https://news.ycombinator.com/item?id=49285139) |
| **9** | [AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug) | ⭐ 367 | 💬 141 | [HN Thread](https://news.ycombinator.com/item?id=49331423) |
| **10** | [Olo (Color)](https://en.wikipedia.org/wiki/Olo_(color)) | ⭐ 418 | 💬 80 | [HN Thread](https://news.ycombinator.com/item?id=49270194) |

---

## 🗄️ News Archive

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
