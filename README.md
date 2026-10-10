# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [2D Vehicles](https://patkerr.co.uk/2d-vehicles/) | ⭐ 279 | 💬 66 | [HN Thread](https://news.ycombinator.com/item?id=49991852) |
| **2** | [A city-building game in which the city would prefer you didn't](https://housing.over.pizza/) | ⭐ 59 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=50036864) |
| **3** | [Why DuckDB 2.0 is faster](https://motherduck.com/blog/why-duckdb-20-is-faster/) | ⭐ 101 | 💬 30 | [HN Thread](https://news.ycombinator.com/item?id=50035530) |
| **4** | [Nix wrote half of my debugger](https://fzakaria.com/2026/10/07/nix-wrote-half-of-my-debugger) | ⭐ 77 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=50017247) |
| **5** | [Knuth reward check](https://www.thomas-huehn.com/knuth-reward-check/) | ⭐ 119 | 💬 47 | [HN Thread](https://news.ycombinator.com/item?id=50034081) |
| **6** | [The Lightbulb Computer](https://lightbulbcomputer.com/) | ⭐ 134 | 💬 34 | [HN Thread](https://news.ycombinator.com/item?id=50029487) |
| **7** | [Talorys – A self-hosted personal AI agent on Cloudflare's free tier](https://github.com/rociiu/talorys) | ⭐ 223 | 💬 113 | [HN Thread](https://news.ycombinator.com/item?id=50031614) |
| **8** | [Mxc: Microsoft Execution Containers version 1.0.0](https://blogs.windows.com/windowsdeveloper/2026/10/07/microsoft-execution-containers-policy-driven-containment-for-ai-agents/) | ⭐ 141 | 💬 32 | [HN Thread](https://news.ycombinator.com/item?id=50016956) |
| **9** | [Recent AI models struggled to match a human algorithmic innovation](https://epoch.ai/publications/innovationeval) | ⭐ 54 | 💬 48 | [HN Thread](https://news.ycombinator.com/item?id=50027257) |
| **10** | [REA Reverse – Engineer Anything](https://rea.tools/) | ⭐ 662 | 💬 292 | [HN Thread](https://news.ycombinator.com/item?id=50028275) |

---

## 🗄️ News Archive

- 📅 [2026-10-10](archive/2026-10-10.md)
- 📅 [2026-10-09](archive/2026-10-09.md)
- 📅 [2026-10-08](archive/2026-10-08.md)
- 📅 [2026-10-07](archive/2026-10-07.md)
- 📅 [2026-10-05](archive/2026-10-05.md)
- 📅 [2026-10-04](archive/2026-10-04.md)
- 📅 [2026-10-03](archive/2026-10-03.md)
- 📅 [2026-10-02](archive/2026-10-02.md)
- 📅 [2026-10-01](archive/2026-10-01.md)
- 📅 [2026-09-30](archive/2026-09-30.md)
- 📅 [2026-09-29](archive/2026-09-29.md)
- 📅 [2026-09-28](archive/2026-09-28.md)
- 📅 [2026-09-27](archive/2026-09-27.md)
- 📅 [2026-09-26](archive/2026-09-26.md)

*... and [41 older editions in the archive folder](archive/)*

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
