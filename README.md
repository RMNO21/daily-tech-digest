# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [A Preview of DuckDB v2.0](https://duckdb.org/2026/08/17/duckdb-20-highlights) | ⭐ 209 | 💬 29 | [HN Thread](https://news.ycombinator.com/item?id=49330781) |
| **2** | [AI-Generated GitHub Copilot "Autofix" Allowed Compromise of Snowflake's Jira](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug) | ⭐ 97 | 💬 43 | [HN Thread](https://news.ycombinator.com/item?id=49331423) |
| **3** | [GPT 5.6 Sol is the best "vision" model OpenAI ever released](https://blog.roboflow.com/openai-gpt-5-6/) | ⭐ 183 | 💬 100 | [HN Thread](https://news.ycombinator.com/item?id=49329575) |
| **4** | [Launch HN: Speko (YC S26) – OpenRouter for Voice AI](https://speko.ai/) | ⭐ 22 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=49332751) |
| **5** | [How to disable or avoid intrusive AI](https://www.librarian.net/notoai/) | ⭐ 75 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=49331220) |
| **6** | [How to put 170 atoms in an atom](https://signoregalilei.com/2026/08/02/how-to-put-170-atoms-in-an-atom/) | ⭐ 41 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49331474) |
| **7** | [GitHub down again? no PR access](https://news.ycombinator.com/item?id=49330632) | ⭐ 280 | 💬 97 | [HN Thread](https://news.ycombinator.com/item?id=49330632) |
| **8** | [Olo (Color)](https://en.wikipedia.org/wiki/Olo_(color)) | ⭐ 53 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49270194) |
| **9** | [Apple's App Tracking Transparency treated its own apps better than rivals](https://www.bundeskartellamt.de/SharedDocs/Meldung/EN/Pressemitteilungen/2026/08_17_2026_Apple_ATTF.html) | ⭐ 166 | 💬 58 | [HN Thread](https://news.ycombinator.com/item?id=49331222) |
| **10** | [How I developed an Am29000 C compiler and web browser](https://nanochess.org/am29000_c_compiler_web_browser.html) | ⭐ 30 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49323474) |

---

## 🗄️ News Archive

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
