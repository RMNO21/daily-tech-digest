# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Iceland votes on whether to restart talks on joining EU](https://www.bbc.com/news/articles/cn45vdxyvvlo) | ⭐ 159 | 💬 179 | [HN Thread](https://news.ycombinator.com/item?id=49489057) |
| **2** | [Samsung's Processing-in-Memory (PIM)](https://chipsandcheese.com/p/hot-chips-2026-samsungs-processing) | ⭐ 148 | 💬 48 | [HN Thread](https://news.ycombinator.com/item?id=49487341) |
| **3** | [GUIs should be fully keyboard-driven](https://ckardaris.com/blog/2026/08/28/keyboard-driven-guis.html) | ⭐ 889 | 💬 440 | [HN Thread](https://news.ycombinator.com/item?id=49479837) |
| **4** | [Boot a Virtual iPhone via Apple's Virtualization.framework](https://github.com/Lakr233/vphone-cli) | ⭐ 316 | 💬 83 | [HN Thread](https://news.ycombinator.com/item?id=49485267) |
| **5** | [Htmx 4.0](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released) | ⭐ 715 | 💬 177 | [HN Thread](https://news.ycombinator.com/item?id=49478178) |
| **6** | [Europe's last regular standard-gauge steam passenger service](https://parowozowniawolsztyn.pl/?page_id=2141) | ⭐ 68 | 💬 18 | [HN Thread](https://news.ycombinator.com/item?id=49456819) |
| **7** | [Hunting Down a Go Runtime Bug on 32-Bit Embedded Systems](https://sigma-star.at/blog/2026/08/go-runtime-netpoll-bug/) | ⭐ 50 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49450782) |
| **8** | [Glacier Mice](https://en.wikipedia.org/wiki/Glacier_mice) | ⭐ 53 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49424320) |
| **9** | [U.S. sanctions against the A/I Collective](https://www.inventati.org/) | ⭐ 639 | 💬 637 | [HN Thread](https://news.ycombinator.com/item?id=49477854) |
| **10** | [StemDeck, a free, open-source and local AI stem separator](https://github.com/stemdeckapp/stemdeck) | ⭐ 143 | 💬 32 | [HN Thread](https://news.ycombinator.com/item?id=49486081) |

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
