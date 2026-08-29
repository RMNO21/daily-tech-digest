# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Tencent Releases and Open-Sources Tencent Hy4 Preview](https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/) | ⭐ 103 | 💬 47 | [HN Thread](https://news.ycombinator.com/item?id=49492632) |
| **2** | [$44M Solar-Powered EV Production Deal Struck](https://frequal.com/aptera/ProductionDealAug2026.html) | ⭐ 14 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=49493563) |
| **3** | [vLLM v0.28.0](https://github.com/vllm-project/vllm/releases/tag/v0.28.0) | ⭐ 65 | 💬 21 | [HN Thread](https://news.ycombinator.com/item?id=49492067) |
| **4** | [Tether: iMessage, SMS, etc. on Linux](https://zackbartel.com/blog/2026/08/tether/) | ⭐ 262 | 💬 117 | [HN Thread](https://news.ycombinator.com/item?id=49415386) |
| **5** | [What we want is a hunter gatherer lifestyle with space age tools](https://www.strangeloopcanon.com/p/what-we-want-is-a-hunter-gatherer) | ⭐ 38 | 💬 31 | [HN Thread](https://news.ycombinator.com/item?id=49493244) |
| **6** | [Calibrate Before You Accelerate: Bias Toward Action in a New Role](https://tucker.wales/writing/bias-towards-action/) | ⭐ 76 | 💬 28 | [HN Thread](https://news.ycombinator.com/item?id=49491714) |
| **7** | [Nancy Grace Roman Space Telescope Launches this Sunday](https://www.npr.org/2026/08/28/nx-s1-5905370/nasa-nancy-grace-roman-space-telescope-dark-energy-supernova) | ⭐ 33 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49482833) |
| **8** | [Functional State Machines in Rust: Typestate and Newtype Patterns](https://dl.acm.org/doi/10.1145/3830438.3830958) | ⭐ 22 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49492368) |
| **9** | [SQLite as a Document Database (2020)](https://dgl.cx/2020/06/sqlite-json-support) | ⭐ 145 | 💬 42 | [HN Thread](https://news.ycombinator.com/item?id=49426995) |
| **10** | [Domain-Driven Agents](https://coldtake.dev/blog/domain-driven-agents) | ⭐ 23 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49492584) |

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
