# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [ZuckOff Know when a camera is in the room](https://zuckoff.app/) | ⭐ 500 | 💬 209 | [HN Thread](https://news.ycombinator.com/item?id=49785429) |
| **2** | [Disney+: New user agreement allows ads before movies in all subscriptions](https://consumerrights.wiki/w/Disney%2B_ad_policy_change) | ⭐ 263 | 💬 184 | [HN Thread](https://news.ycombinator.com/item?id=49784336) |
| **3** | [Kev: Tiny Jev-like family of decision models built on top of Qwen3.5](https://github.com/jaredpalmer/kev/tree/main) | ⭐ 225 | 💬 97 | [HN Thread](https://news.ycombinator.com/item?id=49783999) |
| **4** | [Jev-Leftpad](https://github.com/f/jev-leftpad) | ⭐ 163 | 💬 61 | [HN Thread](https://news.ycombinator.com/item?id=49784706) |
| **5** | [What Sun Got Wrong](https://bcantrill.dtrace.org/2026/09/20/what-sun-got-wrong/) | ⭐ 4 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49787436) |
| **6** | [Grim Fandango Puzzle Document (1996) [pdf]](http://gameshelf.jmac.org/2008/11/13/GrimPuzzleDoc_small.pdf) | ⭐ 273 | 💬 60 | [HN Thread](https://news.ycombinator.com/item?id=49783495) |
| **7** | [AX – Google’s Open Agentic Orchestrator](https://agentexecutor.io) | ⭐ 567 | 💬 259 | [HN Thread](https://news.ycombinator.com/item?id=49780797) |
| **8** | [Show HN: Lossless-memory – a personal AI memory that never summarizes](https://github.com/aru-labs/lossless-memory) | ⭐ 16 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=49786419) |
| **9** | [ZuckOff Is a Free App That Sees Meta Glasses Before They See You](https://www.wired.me/story/meta-smart-glasses-detector-app-zuckoff) | ⭐ 250 | 💬 30 | [HN Thread](https://news.ycombinator.com/item?id=49785397) |
| **10** | [Samsung is expected to more than double output of its HBM4 and HBM4E DRAM](https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say) | ⭐ 514 | 💬 370 | [HN Thread](https://news.ycombinator.com/item?id=49778029) |

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
