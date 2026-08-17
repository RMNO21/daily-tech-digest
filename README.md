# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [GPU Offload in Rust: Portable, Safe, and Fast](https://arxiv.org/abs/2608.13759) | ⭐ 59 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49334991) |
| **2** | [A Preview of DuckDB v2.0](https://duckdb.org/2026/08/17/duckdb-20-highlights) | ⭐ 429 | 💬 69 | [HN Thread](https://news.ycombinator.com/item?id=49330781) |
| **3** | [AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug) | ⭐ 255 | 💬 112 | [HN Thread](https://news.ycombinator.com/item?id=49331423) |
| **4** | [AI;DR (AI; Didn't Read)](https://www.rickmanelius.com/p/aidr-ai-didnt-read) | ⭐ 184 | 💬 83 | [HN Thread](https://news.ycombinator.com/item?id=49336573) |
| **5** | [Incident with Github.com](https://www.githubstatus.com/incidents/zkxwbgr0cnmx) | ⭐ 398 | 💬 799 | [HN Thread](https://news.ycombinator.com/item?id=49330597) |
| **6** | [India has paved the way for charging merchants a fee on UPI transactions](https://www.bbc.com/news/articles/c8xnwqe00v1o) | ⭐ 17 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49336304) |
| **7** | [Sun Clock](https://sunclock.net/) | ⭐ 91 | 💬 34 | [HN Thread](https://news.ycombinator.com/item?id=49333824) |
| **8** | [How to disable or avoid intrusive AI](https://www.librarian.net/notoai/) | ⭐ 193 | 💬 98 | [HN Thread](https://news.ycombinator.com/item?id=49331220) |
| **9** | [AirTag reveals Amazon is trashing rare books to train AI](https://arstechnica.com/tech-policy/2026/08/hidden-airtag-reveals-amazon-is-trashing-rare-books-to-train-ai/) | ⭐ 104 | 💬 62 | [HN Thread](https://news.ycombinator.com/item?id=49336050) |
| **10** | [GPT 5.6 Sol is the best "vision" model OpenAI ever released](https://blog.roboflow.com/openai-gpt-5-6/) | ⭐ 257 | 💬 137 | [HN Thread](https://news.ycombinator.com/item?id=49329575) |

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
