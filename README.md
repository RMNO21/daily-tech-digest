# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Beam: Reflection's 501B open-weight model](https://reflection.ai/blog/introducing-beam) | ⭐ 224 | 💬 62 | [HN Thread](https://news.ycombinator.com/item?id=49969183) |
| **2** | [Dust: Pretraining Transformers Without Backpropagation](https://qlabs.sh/research/dust) | ⭐ 48 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49970871) |
| **3** | [Find the flattest route between any two points in SF](https://flattensf.com/) | ⭐ 33 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=49971230) |
| **4** | [Opus 5.5 agents discover two room-temperature magnetic semiconductor candidates](https://www.vals.ai/blogs/room-temperature-magnetic-semiconductors) | ⭐ 126 | 💬 107 | [HN Thread](https://news.ycombinator.com/item?id=49970667) |
| **5** | [Web Search API](https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/) | ⭐ 456 | 💬 208 | [HN Thread](https://news.ycombinator.com/item?id=49963171) |
| **6** | [Competitive Programmer's Handbook (2018) [pdf]](https://cses.fi/book/book.pdf) | ⭐ 78 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=49944049) |
| **7** | [Using Blu-ray M-Disk as Backup of Last Resort](https://smyck.net/2026/10/03/holocron-the-backup-of-last-resort/) | ⭐ 22 | 💬 19 | [HN Thread](https://news.ycombinator.com/item?id=49951693) |
| **8** | [Making a GTK application in Haskell, part 1](https://floreal.tech/blog/2026/making-a-gtk-app-in-haskell-part-1/) | ⭐ 119 | 💬 27 | [HN Thread](https://news.ycombinator.com/item?id=49965308) |
| **9** | [Anthropic reported diary entry to police, woman faces felony charge](https://www.techspot.com/news/114091-florida-woman-used-claude-diary-anthropic-reported-shoot.html) | ⭐ 434 | 💬 362 | [HN Thread](https://news.ycombinator.com/item?id=49961057) |
| **10** | [A third way of using Linux](https://hisvirusness.com/third-is-the-way) | ⭐ 13 | 💬 23 | [HN Thread](https://news.ycombinator.com/item?id=49970073) |

---

## 🗄️ News Archive

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
- 📅 [2026-09-25](archive/2026-09-25.md)
- 📅 [2026-09-24](archive/2026-09-24.md)
- 📅 [2026-09-22](archive/2026-09-22.md)
- 📅 [2026-09-21](archive/2026-09-21.md)

*... and [37 older editions in the archive folder](archive/)*

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
