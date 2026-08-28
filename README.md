# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Stopping the smart TV from being used against you](https://www.s-config.com/stopping-a-smart-tv-from-being-used-against-you/) | ⭐ 61 | 💬 36 | [HN Thread](https://news.ycombinator.com/item?id=49483816) |
| **2** | [GUIs should be fully keyboard-driven](https://ckardaris.com/blog/2026/08/28/keyboard-driven-guis.html) | ⭐ 452 | 💬 240 | [HN Thread](https://news.ycombinator.com/item?id=49479837) |
| **3** | [25,000 Lbs. Of Chicken Products Recalled in 5 States: USDA](https://www.thehealthy.com/news/chicken-recall-fsis-august-2026/) | ⭐ 154 | 💬 109 | [HN Thread](https://news.ycombinator.com/item?id=49483182) |
| **4** | [Htmx 4.0](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released) | ⭐ 416 | 💬 102 | [HN Thread](https://news.ycombinator.com/item?id=49478178) |
| **5** | [Just the rumour of a bug is enough to find an exploit these days](https://anil.recoil.org/notes/rumour-is-the-exploit) | ⭐ 196 | 💬 66 | [HN Thread](https://news.ycombinator.com/item?id=49480466) |
| **6** | [U.S. sanctions against the A/I Collective](https://www.inventati.org/) | ⭐ 409 | 💬 363 | [HN Thread](https://news.ycombinator.com/item?id=49477854) |
| **7** | [Inception-style curved map for turn-by-turn directions](https://www.orbify.eu/demo/) | ⭐ 369 | 💬 126 | [HN Thread](https://news.ycombinator.com/item?id=49477564) |
| **8** | [Curvature Beziers: Improving on a timeless recipe](https://acko.net/blog/curvature-beziers/) | ⭐ 46 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=49422743) |
| **9** | [Visual Analysis of Binary Files](https://binvis.io/#/) | ⭐ 46 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49443783) |
| **10** | [Autonomous Mathematical Discovery in an Open-World Multi-Agent Environment](https://arxiv.org/abs/2608.23691) | ⭐ 60 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49481455) |

---

## 🗄️ News Archive

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
- 📅 [2026-08-15](archive/2026-08-15.md)

*... and [1 older editions in the archive folder](archive/)*

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
