# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [How Bluesky draws its logo on screenshots](https://timmarinin.net/2026/bluesky-screenshots/) | ⭐ 203 | 💬 144 | [HN Thread](https://news.ycombinator.com/item?id=49338459) |
| **2** | [Quake Shareware, a CD-ROM just a little too full](https://fabiensanglard.net/quake_shareware_cd/index.html) | ⭐ 136 | 💬 60 | [HN Thread](https://news.ycombinator.com/item?id=49338328) |
| **3** | [Flock cameras haven't improved Atlanta's crime clearance rates](https://atlpresscollective.com/2026/07/28/flock-cameras-atlanta-clearance-rates/) | ⭐ 40 | 💬 21 | [HN Thread](https://news.ycombinator.com/item?id=49338732) |
| **4** | [Fairphone 6 and PostmarketOS working main camera](https://catcrafts.net/posts/fairphone-6-postmarketos-working-main-camera) | ⭐ 77 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=49338285) |
| **5** | [GPT-5.6 Sol Pricing Cut by 50%](https://openrouter.ai/openai/gpt-5.6-sol) | ⭐ 94 | 💬 36 | [HN Thread](https://news.ycombinator.com/item?id=49337602) |
| **6** | [A Preview of DuckDB v2.0](https://duckdb.org/2026/08/17/duckdb-20-highlights) | ⭐ 528 | 💬 95 | [HN Thread](https://news.ycombinator.com/item?id=49330781) |
| **7** | [GPU Offload in Rust: Portable, Safe, and Fast](https://arxiv.org/abs/2608.13759) | ⭐ 157 | 💬 36 | [HN Thread](https://news.ycombinator.com/item?id=49334991) |
| **8** | [Incident with Github.com](https://www.githubstatus.com/incidents/zkxwbgr0cnmx) | ⭐ 527 | 💬 911 | [HN Thread](https://news.ycombinator.com/item?id=49330597) |
| **9** | [AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug) | ⭐ 314 | 💬 125 | [HN Thread](https://news.ycombinator.com/item?id=49331423) |
| **10** | [The Road to MS-DOS 2.0](https://nemanjatrifunovic.substack.com/p/the-road-to-ms-dos-2) | ⭐ 17 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49269966) |

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
