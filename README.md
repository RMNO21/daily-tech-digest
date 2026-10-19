# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Putting Linux on my RTX spark laptop because I don't have a Microsoft account](https://josie.lol/blog/linux-rtx-spark) | ⭐ 96 | 💬 38 | [HN Thread](https://news.ycombinator.com/item?id=50158100) |
| **2** | [MiniMax M3.1 Flash](https://www.minimax.io/blog/minimax-m31f) | ⭐ 310 | 💬 127 | [HN Thread](https://news.ycombinator.com/item?id=50154540) |
| **3** | [I built a drone with only one motor [video]](https://www.youtube.com/watch?v=Ndftcft6XhU) | ⭐ 264 | 💬 48 | [HN Thread](https://news.ycombinator.com/item?id=50150089) |
| **4** | [The reverts will continue until morale improves](http://peter.eisentraut.org/blog/2026/10/09/the-reverts-will-continue-until-morale-improves) | ⭐ 143 | 💬 22 | [HN Thread](https://news.ycombinator.com/item?id=50156206) |
| **5** | [Wine ported to OpenBSD](https://marc.info/?l=openbsd-ports&m=179236125692175) | ⭐ 467 | 💬 152 | [HN Thread](https://news.ycombinator.com/item?id=50152307) |
| **6** | [OpenBSD 8.0 release will have inteldrm/radeondrm/amdgpu drivers from Linux 6.18](https://bsd.network/@brynet/117407035545900963) | ⭐ 30 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=50158138) |
| **7** | [Android apps running native on macOS](https://github.com/kksimp/Mac.apk) | ⭐ 211 | 💬 92 | [HN Thread](https://news.ycombinator.com/item?id=50154624) |
| **8** | [It's still ok to enjoy programming](https://chriskiehl.com/article/it-is-still-ok-to-enjoy-programming) | ⭐ 360 | 💬 352 | [HN Thread](https://news.ycombinator.com/item?id=50134472) |
| **9** | [RuneScape Bench: MMOs for Agents [video]](https://www.youtube.com/watch?v=cNm4zyUtWj0) | ⭐ 121 | 💬 47 | [HN Thread](https://news.ycombinator.com/item?id=50136126) |
| **10** | [The fire retardant in the seafood chain](https://insideclimatenews.org/news/14102026/ethoxyquin-fire-retardant-in-seafood-chain/) | ⭐ 83 | 💬 26 | [HN Thread](https://news.ycombinator.com/item?id=50134359) |

---

## 🗄️ News Archive

- 📅 [2026-10-19](archive/2026-10-19.md)
- 📅 [2026-10-18](archive/2026-10-18.md)
- 📅 [2026-10-17](archive/2026-10-17.md)
- 📅 [2026-10-16](archive/2026-10-16.md)
- 📅 [2026-10-15](archive/2026-10-15.md)
- 📅 [2026-10-14](archive/2026-10-14.md)
- 📅 [2026-10-13](archive/2026-10-13.md)
- 📅 [2026-10-10](archive/2026-10-10.md)
- 📅 [2026-10-09](archive/2026-10-09.md)
- 📅 [2026-10-08](archive/2026-10-08.md)
- 📅 [2026-10-07](archive/2026-10-07.md)
- 📅 [2026-10-05](archive/2026-10-05.md)
- 📅 [2026-10-04](archive/2026-10-04.md)
- 📅 [2026-10-03](archive/2026-10-03.md)

*... and [48 older editions in the archive folder](archive/)*

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
