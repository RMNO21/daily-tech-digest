# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [The Internet Is Kind of a Predatory Cesspit Now](https://www.stephendiehl.com/posts/internet_predatory_cesspit/) | ⭐ 97 | 💬 48 | [HN Thread](https://news.ycombinator.com/item?id=49492193) |
| **2** | [Warp builds self-improving agents on Claude](https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude) | ⭐ 4 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49492432) |
| **3** | [SQLite as a Document Database (2020)](https://dgl.cx/2020/06/sqlite-json-support) | ⭐ 111 | 💬 27 | [HN Thread](https://news.ycombinator.com/item?id=49426995) |
| **4** | [Calibrate Before You Accelerate: Bias Toward Action in a New Role](https://tucker.wales/writing/bias-towards-action/) | ⭐ 24 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49491714) |
| **5** | [Tether: iMessage, SMS, etc. on Linux](https://zackbartel.com/blog/2026/08/tether/) | ⭐ 149 | 💬 80 | [HN Thread](https://news.ycombinator.com/item?id=49415386) |
| **6** | [Sleepwalker: Passive Backdoor with Its Own Command Language](https://r136a1.dev/2026/08/24/sleepwalker-a-passive-backdoor-with-its-own-command-language/) | ⭐ 35 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49428756) |
| **7** | [Indirect Calling of Nested Functions on GCC Without Executable Stack](https://uecker.codeberg.page/2026-08-29.html) | ⭐ 49 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=49490138) |
| **8** | [Quantifying Colour](https://ekunazanu.foo/lab/quantifying-colour/) | ⭐ 36 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49490832) |
| **9** | [Show HN: Typebase – A single-folder back end you write in TypeScript](https://typebase.io) | ⭐ 72 | 💬 15 | [HN Thread](https://news.ycombinator.com/item?id=49447178) |
| **10** | [Good Culture Is the Biggest Productivity Hack, Not AI](https://newsletter.eng-leadership.com/p/good-culture-is-the-biggest-productivity) | ⭐ 60 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=49491568) |

---

## 🗄️ News Archive

- 📅 [2026-08-29](archive/2026-08-29.md)
- 📅 [2026-08-28](archive/2026-08-28.md)
- 📅 [2026-08-27](archive/2026-08-27.md)
- 📅 [2026-08-26](archive/2026-08-26.md)
- 📅 [2026-08-25](archive/2026-08-25.md)
- 📅 [2026-08-24](archive/2026-08-24.md)
- 📅 [2026-08-23](archive/2026-08-23.md)
- 📅 [2026-08-22](archive/2026-08-22.md)
- 📅 [2026-08-21](archive/2026-08-21.md)
- 📅 [2026-08-20](archive/2026-08-20.md)
- 📅 [2026-08-19](archive/2026-08-19.md)
- 📅 [2026-08-18](archive/2026-08-18.md)
- 📅 [2026-08-17](archive/2026-08-17.md)
- 📅 [2026-08-16](archive/2026-08-16.md)

*... and [2 older editions in the archive folder](archive/)*

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
