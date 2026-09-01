# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Tailcat: Tailscale Without Tailscale, by Tailscale](https://tailscale.com/blog/tailcat) | ⭐ 39 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49517420) |
| **2** | [Fastpotify](https://fastpotify.rocks/) | ⭐ 30 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49517448) |
| **3** | [Google Antigravity introduces Boost deep reasoning (/boost)](https://antigravity.google/docs/boost/) | ⭐ 24 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=49517537) |
| **4** | [2004 RuneScape fit a multiplayer RPG into 56k dial-up](https://jkm.dev/posts/how-2004-runescape-fit-a-multiplayer-rpg-into-56k-dialup/) | ⭐ 65 | 💬 37 | [HN Thread](https://news.ycombinator.com/item?id=49516699) |
| **5** | [I turned my security cameras into an automatic bird identification system](https://jasontucker.blog/how-i-turned-my-security-cameras-into-an-automatic-bird-identification-system-with-birdnet-go/) | ⭐ 406 | 💬 99 | [HN Thread](https://news.ycombinator.com/item?id=49511856) |
| **6** | [Playa Phone](https://playaphone.com/) | ⭐ 543 | 💬 196 | [HN Thread](https://news.ycombinator.com/item?id=49510514) |
| **7** | [A walkable ASCII cyberpunk city in one HTML file [video]](https://www.youtube.com/watch?v=3YtygAx_C6A) | ⭐ 253 | 💬 33 | [HN Thread](https://news.ycombinator.com/item?id=49512975) |
| **8** | [Terence Tao explains 6 essential mathematical concepts [video]](https://www.youtube.com/watch?v=OOMx2BHHWtE) | ⭐ 284 | 💬 32 | [HN Thread](https://news.ycombinator.com/item?id=49503521) |
| **9** | [Dwarf Fortress is getting the mother of all magic updates](https://www.rockpapershotgun.com/dwarf-fortress-is-getting-the-mother-of-all-magic-updates-extending-to-the-fundamental-cosmological-makeup-of-the-universe) | ⭐ 335 | 💬 126 | [HN Thread](https://news.ycombinator.com/item?id=49467636) |
| **10** | [RotaryCell: Making an unmodified rotary phone work over LTE with an ESP32-S3](https://github.com/fregacmols/RotaryCell) | ⭐ 7 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49517297) |

---

## 🗄️ News Archive

- 📅 [2026-09-01](archive/2026-09-01.md)
- 📅 [2026-08-31](archive/2026-08-31.md)
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

*... and [5 older editions in the archive folder](archive/)*

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
