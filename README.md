# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Revealing the details of how OpenAI agents hacked Hugging Face](https://swarmtraces.org/) | ⭐ 433 | 💬 263 | [HN Thread](https://news.ycombinator.com/item?id=49849985) |
| **2** | [A single function Jev-like wrapper for LLMs, including vision models](http://allanrbo.blogspot.com/2026/09/a-jev-like-wrapper-for-llms-including.html) | ⭐ 49 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49853175) |
| **3** | [Plan mode is dead](https://www.aymannadeem.com/artificial/intelligence,/developer/tools/2026/09/24/plan-mode-is-dead.html) | ⭐ 276 | 💬 248 | [HN Thread](https://news.ycombinator.com/item?id=49840054) |
| **4** | [Ollaya – Ollama for open-source, Jev-style decision models](https://ollaya.dev/) | ⭐ 420 | 💬 114 | [HN Thread](https://news.ycombinator.com/item?id=49848269) |
| **5** | [Show HN: Jev Plays Pokémon Red](https://jev-pokemon.vercel.app/) | ⭐ 188 | 💬 80 | [HN Thread](https://news.ycombinator.com/item?id=49845172) |
| **6** | [What even is an OS now?](https://sockpuppet.org/blog/2026/09/25/what-even-is-an-os-now/) | ⭐ 173 | 💬 265 | [HN Thread](https://news.ycombinator.com/item?id=49850305) |
| **7** | [The Murky History of Soviet-Born Tetris](https://thereader.mitpress.mit.edu/the-bizarre-murky-history-of-soviet-born-tetris/) | ⭐ 31 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=49838040) |
| **8** | [Postgres SELECT DISTINCT Does Not Scale](https://www.dbos.dev/blog/postgres-select-distinct-does-not-scale) | ⭐ 65 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=49835096) |
| **9** | [How I changed teaching after AI managed to do all my homework assignments](https://thelastsoftwareengineer.substack.com/p/how-i-changed-teaching-after-ai-managed) | ⭐ 52 | 💬 13 | [HN Thread](https://news.ycombinator.com/item?id=49836579) |
| **10** | [Jury finds Facebook liable for deceiving users in Cambridge Analytica case](https://www.cbsnews.com/news/facebook-liable-deceiving-users-cambridge-analytica/) | ⭐ 196 | 💬 41 | [HN Thread](https://news.ycombinator.com/item?id=49852302) |

---

## 🗄️ News Archive

- 📅 [2026-09-26](archive/2026-09-26.md)
- 📅 [2026-09-25](archive/2026-09-25.md)
- 📅 [2026-09-24](archive/2026-09-24.md)
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

*... and [28 older editions in the archive folder](archive/)*

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
