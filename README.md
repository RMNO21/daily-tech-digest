# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Astra can read and write weights to improve Qwen](https://rikiyat.github.io/blog/weight-space-programming/) | ⭐ 1654 | 💬 527 | [HN Thread](https://news.ycombinator.com/item?id=50341174) |
| **2** | [Anthropic's growth just flattened](https://www.regenerator1.com/p/anthropics-growth-just-flattened) | ⭐ 79 | 💬 59 | [HN Thread](https://news.ycombinator.com/item?id=50344958) |
| **3** | [Show HN: Subvocal – Talk to your computer without making noise](https://news.ycombinator.com/item?id=50340088) | ⭐ 478 | 💬 263 | [HN Thread](https://news.ycombinator.com/item?id=50340088) |
| **4** | [Apple reports fourth quarter results](https://www.apple.com/newsroom/2026/11/apple-reports-fourth-quarter-results/) | ⭐ 51 | 💬 29 | [HN Thread](https://news.ycombinator.com/item?id=50344670) |
| **5** | [US boy names that became girl names and vice versa](https://namedaisy.com/blog/boy-names-that-became-girl-names) | ⭐ 248 | 💬 278 | [HN Thread](https://news.ycombinator.com/item?id=50339397) |
| **6** | [Launch HN: Momentic (YC W24) – Agents that catch bugs by using your app](https://momentic.ai/) | ⭐ 109 | 💬 72 | [HN Thread](https://news.ycombinator.com/item?id=50339913) |
| **7** | [If you love a website, back it up](https://blog.mistys-internet.website/post/2026/10/29/if-you-love-a-website-back-it-up/) | ⭐ 346 | 💬 85 | [HN Thread](https://news.ycombinator.com/item?id=50336518) |
| **8** | [Show HN: Warsaw in voxels – An interactive 3D map of the city centre](https://p.migdal.pl/warsaw-vibe-voxel/) | ⭐ 192 | 💬 34 | [HN Thread](https://news.ycombinator.com/item?id=50339221) |
| **9** | [The SEC Should Block Anthropic's IPO to Protect the Public](https://www.techpolicy.press/the-sec-should-block-anthropics-ipo-to-protect-the-public/) | ⭐ 77 | 💬 37 | [HN Thread](https://news.ycombinator.com/item?id=50344919) |
| **10** | [Ask HN: Who is hiring? (November 2026)](https://news.ycombinator.com/item?id=50338728) | ⭐ 162 | 💬 133 | [HN Thread](https://news.ycombinator.com/item?id=50338728) |

---

## 🗄️ News Archive

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
- 📅 [2026-10-21](archive/2026-10-21.md)
- 📅 [2026-10-20](archive/2026-10-20.md)
- 📅 [2026-10-19](archive/2026-10-19.md)
- 📅 [2026-10-18](archive/2026-10-18.md)

*... and [60 older editions in the archive folder](archive/)*

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
