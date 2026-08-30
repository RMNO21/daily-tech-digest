# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Bug Blindness](https://danluu.com/bug-blind/) | ⭐ 128 | 💬 50 | [HN Thread](https://news.ycombinator.com/item?id=49494520) |
| **2** | [Hy4 preview](https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/) | ⭐ 229 | 💬 137 | [HN Thread](https://news.ycombinator.com/item?id=49492632) |
| **3** | [RISC-V is now officially supported by CPython](https://blog.python.org/2026/08/riscv-now-officially-supported/) | ⭐ 62 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=49425252) |
| **4** | [Algorithmic Rent-Pricing Litigation Expands Under New State and Local Laws](https://www.morganlewis.com/pubs/2026/08/algorithmic-rent-pricing-litigation-expands-under-new-state-and-local-laws) | ⭐ 22 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=49495127) |
| **5** | [FreeCORE TrueNAS Core – Continued](https://freecore.org/) | ⭐ 53 | 💬 28 | [HN Thread](https://news.ycombinator.com/item?id=49494856) |
| **6** | [Tether: iMessage, SMS, etc. on Linux](https://zackbartel.com/blog/2026/08/tether/) | ⭐ 395 | 💬 165 | [HN Thread](https://news.ycombinator.com/item?id=49415386) |
| **7** | [Show HN: I missed the moving blocks, so I built a real Linux disk defragmenter](https://github.com/gbin/defragger) | ⭐ 29 | 💬 18 | [HN Thread](https://news.ycombinator.com/item?id=49438865) |
| **8** | [Nancy Grace Roman Space Telescope](https://science.nasa.gov/mission/roman-space-telescope/) | ⭐ 160 | 💬 68 | [HN Thread](https://news.ycombinator.com/item?id=49490870) |
| **9** | [Lawmakers added $1 to car insurance policies. That money paid for Flock cameras](https://www.texastribune.org/2026/08/28/texas-flock-cameras-auto-insurance-fee-mvcpa-grants/) | ⭐ 194 | 💬 88 | [HN Thread](https://news.ycombinator.com/item?id=49494182) |
| **10** | [Benjamin Franklin's Alter Egos Gave Him the Most Freedom](https://www.smithsonianmag.com/history/among-all-great-things-benjamin-franklin-invented-discovered-alter-egos-gave-him-most-freedom-180988824/) | ⭐ 18 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49494751) |

---

## 🗄️ News Archive

- 📅 [2026-08-30](archive/2026-08-30.md)
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

*... and [3 older editions in the archive folder](archive/)*

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
