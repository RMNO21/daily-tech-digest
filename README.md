# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Show HN: TitleArt – Make text like it's 1997](https://titleart.dvy.io/) | ⭐ 90 | 💬 15 | [HN Thread](https://news.ycombinator.com/item?id=50238708) |
| **2** | [PaperPilot – Zero-Cloud, Pure-Rust PDF Engine with WASM and MCP](https://github.com/KrushnaVardhanReddy/PaperPilot) | ⭐ 62 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=50238739) |
| **3** | [Cognitive Mercantilism: AI panic resembles fears of early capitalism](https://contraptions.venkateshrao.com/p/cognitive-mercantilism) | ⭐ 27 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=50239027) |
| **4** | [Dolly Parton's Imagination Library](https://imaginationlibrary.com/) | ⭐ 489 | 💬 88 | [HN Thread](https://news.ycombinator.com/item?id=50234474) |
| **5** | [Behind the scenes at the NeXT Computer office](https://exhibits.stanford.edu/menuez/browse/next-computer-inc?per_page=96&sort=pub_year_isi+asc%2C+title_sort+asc&view=masonry) | ⭐ 55 | 💬 21 | [HN Thread](https://news.ycombinator.com/item?id=50238763) |
| **6** | [Show HN: A Truly Modular Keyboard](https://github.com/notaroomba/keybytes) | ⭐ 75 | 💬 19 | [HN Thread](https://news.ycombinator.com/item?id=50228115) |
| **7** | [Overgrown, when plants invade your abandoned tabs](https://charliegerard.dev/blog/overgrown-extension/) | ⭐ 226 | 💬 73 | [HN Thread](https://news.ycombinator.com/item?id=50197108) |
| **8** | [The Fall of Scientific American](https://www.thenation.com/article/society/scientific-american-springer-nature-trump/) | ⭐ 43 | 💬 21 | [HN Thread](https://news.ycombinator.com/item?id=50218693) |
| **9** | [Lula wins election after final votes tallied](https://www.reuters.com/live/brazil-election-live-lula-bolsonaro-face-off-presidential-runoff-2026-10-25/) | ⭐ 306 | 💬 288 | [HN Thread](https://news.ycombinator.com/item?id=50237485) |
| **10** | [Attention Is Not What You Need (2025)](https://arxiv.org/abs/2512.19428) | ⭐ 71 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=50237224) |

---

## 🗄️ News Archive

- 📅 [2026-10-26](archive/2026-10-26.md)
- 📅 [2026-10-25](archive/2026-10-25.md)
- 📅 [2026-10-24](archive/2026-10-24.md)
- 📅 [2026-10-23](archive/2026-10-23.md)
- 📅 [2026-10-22](archive/2026-10-22.md)
- 📅 [2026-10-21](archive/2026-10-21.md)
- 📅 [2026-10-20](archive/2026-10-20.md)
- 📅 [2026-10-19](archive/2026-10-19.md)
- 📅 [2026-10-18](archive/2026-10-18.md)
- 📅 [2026-10-17](archive/2026-10-17.md)
- 📅 [2026-10-16](archive/2026-10-16.md)
- 📅 [2026-10-15](archive/2026-10-15.md)
- 📅 [2026-10-14](archive/2026-10-14.md)
- 📅 [2026-10-13](archive/2026-10-13.md)

*... and [55 older editions in the archive folder](archive/)*

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
