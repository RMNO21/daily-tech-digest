# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [OpenRouter is joining Stripe](https://openrouter.ai/blog/announcements/openrouter-is-joining-stripe/) | ⭐ 621 | 💬 331 | [HN Thread](https://news.ycombinator.com/item?id=49364559) |
| **2** | [Go 1.27](https://go.dev/blog/go1.27) | ⭐ 433 | 💬 108 | [HN Thread](https://news.ycombinator.com/item?id=49365405) |
| **3** | [Google replaced Git tags for certain source code with obtaining via Google Drive](https://grapheneos.social/@GrapheneOS/117057099753905023) | ⭐ 286 | 💬 118 | [HN Thread](https://news.ycombinator.com/item?id=49364745) |
| **4** | [Unlocking a locked/deactivated e-waste Cricut Maker](https://sprocketfox.io/xssfox/2026/07/01/cricut-unlock/) | ⭐ 128 | 💬 34 | [HN Thread](https://news.ycombinator.com/item?id=49365841) |
| **5** | [Unsloth Dynamic 3.0 GGUFs](https://unsloth.ai/docs/basics/dynamic-3.0-ggufs) | ⭐ 183 | 💬 66 | [HN Thread](https://news.ycombinator.com/item?id=49365443) |
| **6** | [Manabu Kosaka's Handmade Paper Sculptures](https://coca11272000.wixsite.com/manabukosaka) | ⭐ 21 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49362001) |
| **7** | [A joke domain purchase turned in geopolitical warfare](https://sprocketfox.io/xssfox/2026/08/19/sondehub-and-war/) | ⭐ 747 | 💬 114 | [HN Thread](https://news.ycombinator.com/item?id=49360015) |
| **8** | [Os8088.com: IBM XT OS now has a Browser, CP/M 2.2 with Z80 core and MS Word 1.1a](https://os8088.com/spotlight/) | ⭐ 41 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=49367256) |
| **9** | [Casio F-B100W-1A](https://www.casio.com/uk/watches/casio/product.F-B100W-1A/) | ⭐ 273 | 💬 221 | [HN Thread](https://news.ycombinator.com/item?id=49362887) |
| **10** | [DFlash 2: Keep Drafting Parallel](https://inco.ai/blog/dflash2/) | ⭐ 71 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=49366792) |

---

## 🗄️ News Archive

- 📅 [2026-08-20](archive/2026-08-20.md)
- 📅 [2026-08-19](archive/2026-08-19.md)
- 📅 [2026-08-18](archive/2026-08-18.md)
- 📅 [2026-08-17](archive/2026-08-17.md)
- 📅 [2026-08-16](archive/2026-08-16.md)
- 📅 [2026-08-15](archive/2026-08-15.md)
- 📅 [2026-08-14](archive/2026-08-14.md)

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
