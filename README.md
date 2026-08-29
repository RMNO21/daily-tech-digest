# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Our decision on Cursor following its acquisition by SpaceX](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/) | ⭐ 356 | 💬 148 | [HN Thread](https://news.ycombinator.com/item?id=49486172) |
| **2** | [Boot a Virtual iPhone via Apple's Virtualization.framework](https://github.com/Lakr233/vphone-cli) | ⭐ 209 | 💬 67 | [HN Thread](https://news.ycombinator.com/item?id=49485267) |
| **3** | [GUIs should be fully keyboard-driven](https://ckardaris.com/blog/2026/08/28/keyboard-driven-guis.html) | ⭐ 723 | 💬 357 | [HN Thread](https://news.ycombinator.com/item?id=49479837) |
| **4** | [TurboKV: Insanely fast Rust key-value store](https://github.com/kingroryg/turbokv) | ⭐ 62 | 💬 22 | [HN Thread](https://news.ycombinator.com/item?id=49486334) |
| **5** | [Htmx 4.0](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released) | ⭐ 607 | 💬 150 | [HN Thread](https://news.ycombinator.com/item?id=49478178) |
| **6** | [9th Circuit sides with states in Kalshi gambling fight](https://azmirror.com/2026/08/28/9th-circuit-sides-with-states-in-kalshi-gambling-fight-potentially-reviving-arizonas-prosecution/) | ⭐ 113 | 💬 83 | [HN Thread](https://news.ycombinator.com/item?id=49485452) |
| **7** | [U.S. sanctions against the A/I Collective](https://www.inventati.org/) | ⭐ 546 | 💬 541 | [HN Thread](https://news.ycombinator.com/item?id=49477854) |
| **8** | [I accidentally turned LLM memory into program analysis](https://pwning.systems/posts/llm-memory-program-analysis/) | ⭐ 95 | 💬 16 | [HN Thread](https://news.ycombinator.com/item?id=49485416) |
| **9** | [StemDeck, a free, open-source and local AI stem separator](https://github.com/stemdeckapp/stemdeck) | ⭐ 66 | 💬 13 | [HN Thread](https://news.ycombinator.com/item?id=49486081) |
| **10** | [Does the Sumerian King List Align with Paleoclimate Events?](https://www.vectorian.be/articles/2026-06-07/sumerian-king-list-paleoclimate-alignment-explorer/) | ⭐ 77 | 💬 30 | [HN Thread](https://news.ycombinator.com/item?id=49485532) |

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
