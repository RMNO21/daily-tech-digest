# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [AnkiDroid: Google Play no longer allowing Open Collective donation link](https://github.com/ankidroid/Anki-Android/issues/21656) | ⭐ 317 | 💬 59 | [HN Thread](https://news.ycombinator.com/item?id=49520022) |
| **2** | [44% on ARC-AGI-1 in 67 cents](https://mvakde.github.io/blog/44-on-arc-1/) | ⭐ 139 | 💬 36 | [HN Thread](https://news.ycombinator.com/item?id=49519939) |
| **3** | [Fastpotify](https://fastpotify.rocks/) | ⭐ 548 | 💬 322 | [HN Thread](https://news.ycombinator.com/item?id=49517448) |
| **4** | [American Airlines' Legendary Mechanic Passes Away at 100 After 80-Year Career](https://simpleflying.com/american-airlines-mechanic-passes-away-100-record-80-years/) | ⭐ 129 | 💬 49 | [HN Thread](https://news.ycombinator.com/item?id=49493468) |
| **5** | [EFF to Courts: Don't Rewrite Copyright over AI Hype](https://www.eff.org/deeplinks/2026/08/eff-courts-dont-rewrite-copyright-over-ai-hype) | ⭐ 20 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49521315) |
| **6** | [GPU World](https://www.gpuworld.org/) | ⭐ 296 | 💬 172 | [HN Thread](https://news.ycombinator.com/item?id=49517584) |
| **8** | [Restroom Archive](https://restroomarchive.com) | ⭐ 185 | 💬 47 | [HN Thread](https://news.ycombinator.com/item?id=49517624) |
| **9** | [Playa Phone](https://playaphone.com/) | ⭐ 672 | 💬 215 | [HN Thread](https://news.ycombinator.com/item?id=49510514) |
| **10** | [I turned my security cameras into an automatic bird identification system](https://jasontucker.blog/how-i-turned-my-security-cameras-into-an-automatic-bird-identification-system-with-birdnet-go/) | ⭐ 538 | 💬 137 | [HN Thread](https://news.ycombinator.com/item?id=49511856) |

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
