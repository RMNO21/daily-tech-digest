# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [US FAA says it will phase out floppy disks from air traffic control by 2028](https://www.reuters.com/world/us/us-faa-says-it-will-phase-out-floppy-disks-air-traffic-control-by-2028-2026-11-05/) | ⭐ 51 | 💬 71 | [HN Thread](https://news.ycombinator.com/item?id=50388001) |
| **2** | [Tesla to wind down Cybertruck production](https://www.nbcnews.com/tech/tech-news/tesla-wind-cybertruck-production-years-poor-sales-markets-rcna607817) | ⭐ 315 | 💬 920 | [HN Thread](https://news.ycombinator.com/item?id=50391456) |
| **3** | [First steps in bare-metal programming using UEFI](https://kevinboone.me/efitest_index.html) | ⭐ 41 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=50394855) |
| **4** | [Gemini Omni 1.2 Flash](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/) | ⭐ 213 | 💬 164 | [HN Thread](https://news.ycombinator.com/item?id=50392118) |
| **5** | [Blender's UI and Runtime: Much Faster Than GPUI](https://github.com/ppmpreetham/BUI) | ⭐ 548 | 💬 218 | [HN Thread](https://news.ycombinator.com/item?id=50389333) |
| **6** | [Deus Ex](https://www.filfre.net/2026/11/deus-ex/) | ⭐ 209 | 💬 95 | [HN Thread](https://news.ycombinator.com/item?id=50393758) |
| **7** | [Rune: A native GPU-rendered Rust UI framework for macOS, Windows, Linux and web](https://github.com/anomalyco/rune) | ⭐ 30 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=50394569) |
| **8** | [UpCodes (YC S17) is hiring SDR's to sell AI compliance software](https://up.codes/careers?utm_source=HN) | ⭐ 1 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50395043) |
| **9** | [Claude Code sends your email address to websites](https://github.com/anthropics/claude-code/issues/107757) | ⭐ 1494 | 💬 468 | [HN Thread](https://news.ycombinator.com/item?id=50385272) |
| **10** | [Lippitt-Knoster in Practice (Field Notes for Managing Complex Projects)](https://sharedphysics.com/lippitt-knoster-in-practice-field-notes-for-managing-complex-projects/) | ⭐ 29 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=50393089) |

---

## 🗄️ News Archive

- 📅 [2026-11-06](archive/2026-11-06.md)
- 📅 [2026-11-05](archive/2026-11-05.md)
- 📅 [2026-11-04](archive/2026-11-04.md)
- 📅 [2026-11-03](archive/2026-11-03.md)
- 📅 [2026-11-02](archive/2026-11-02.md)
- 📅 [2026-10-31](archive/2026-10-31.md)
- 📅 [2026-10-30](archive/2026-10-30.md)
- 📅 [2026-10-28](archive/2026-10-28.md)
- 📅 [2026-10-27](archive/2026-10-27.md)
- 📅 [2026-10-26](archive/2026-10-26.md)
- 📅 [2026-10-25](archive/2026-10-25.md)
- 📅 [2026-10-24](archive/2026-10-24.md)
- 📅 [2026-10-23](archive/2026-10-23.md)
- 📅 [2026-10-22](archive/2026-10-22.md)

*... and [64 older editions in the archive folder](archive/)*

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
