# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Tailwind Labs is joining Shopify](https://tailwindcss.com/blog/tailwind-is-joining-shopify) | ⭐ 481 | 💬 187 | [HN Thread](https://news.ycombinator.com/item?id=49626190) |
| **2** | [No Man's Sky Cosmos](https://www.nomanssky.com/cosmos-update/) | ⭐ 77 | 💬 52 | [HN Thread](https://news.ycombinator.com/item?id=49628493) |
| **3** | [GPT-6 Astra, Looped Transformers, and Hidden Reasoning](https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and) | ⭐ 65 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=49627370) |
| **4** | [Claude, change the "Add to Cart" button to blue](https://opusfived.dev/) | ⭐ 620 | 💬 236 | [HN Thread](https://news.ycombinator.com/item?id=49623754) |
| **5** | [Desert Ant Labs: local, fast models that run on device](https://desertant.com/blog/introducing-desert-ant-labs/) | ⭐ 264 | 💬 69 | [HN Thread](https://news.ycombinator.com/item?id=49624823) |
| **6** | [Anthropic Is Building a Predictive Surveillance System to Monitor Activists](https://prospect.org/2026/09/09/anthropic-artificial-intelligence-surveillance-system-monitor-activists/) | ⭐ 121 | 💬 35 | [HN Thread](https://news.ycombinator.com/item?id=49628704) |
| **7** | [GNU Radio in the Browser](https://gnuradioworld.com/) | ⭐ 26 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49628576) |
| **8** | [Planet Labs' Open Satellite Feed](https://tech.marksblogg.com/planet-labs-open-satellite-feed.html) | ⭐ 23 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49628429) |
| **9** | [Rails 8 Guide: Features, Requirements and Upgrade Path (2026)](https://blog.appsignal.com/2024/10/07/whats-new-in-ruby-on-rails-8.html) | ⭐ 19 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49628409) |
| **10** | [Defining AI Psychosis. Part 2: "Prolific AI Psychosis"](https://jeffs.blog/p/defining-ai-psychosis-part-2-prolific) | ⭐ 13 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49628880) |

---

## 🗄️ News Archive

- 📅 [2026-09-09](archive/2026-09-09.md)
- 📅 [2026-09-08](archive/2026-09-08.md)
- 📅 [2026-09-07](archive/2026-09-07.md)
- 📅 [2026-09-06](archive/2026-09-06.md)
- 📅 [2026-09-05](archive/2026-09-05.md)
- 📅 [2026-09-04](archive/2026-09-04.md)
- 📅 [2026-09-03](archive/2026-09-03.md)
- 📅 [2026-09-02](archive/2026-09-02.md)
- 📅 [2026-09-01](archive/2026-09-01.md)
- 📅 [2026-08-31](archive/2026-08-31.md)
- 📅 [2026-08-30](archive/2026-08-30.md)
- 📅 [2026-08-29](archive/2026-08-29.md)
- 📅 [2026-08-28](archive/2026-08-28.md)
- 📅 [2026-08-27](archive/2026-08-27.md)

*... and [13 older editions in the archive folder](archive/)*

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
