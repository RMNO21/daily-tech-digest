# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Go 1.27](https://go.dev/blog/go1.27) | ⭐ 231 | 💬 35 | [HN Thread](https://news.ycombinator.com/item?id=49365405) |
| **2** | [OpenRouter is joining Stripe](https://openrouter.ai/blog/announcements/openrouter-is-joining-stripe/) | ⭐ 336 | 💬 210 | [HN Thread](https://news.ycombinator.com/item?id=49364559) |
| **3** | [Unsloth Dynamic 3.0 GGUFs](https://unsloth.ai/docs/basics/dynamic-3.0-ggufs) | ⭐ 67 | 💬 15 | [HN Thread](https://news.ycombinator.com/item?id=49365443) |
| **4** | [Pixel 11 Pro Fold feels like the end of an era](https://www.theverge.com/tech/981956/google-pixel-11-pro-fold-review) | ⭐ 20 | 💬 33 | [HN Thread](https://news.ycombinator.com/item?id=49366264) |
| **5** | [A joke domain purchase turned in geopolitical warfare](https://sprocketfox.io/xssfox/2026/08/19/sondehub-and-war/) | ⭐ 593 | 💬 77 | [HN Thread](https://news.ycombinator.com/item?id=49360015) |
| **6** | [Unlocking a locked/deactivated e-waste Cricut Maker](https://sprocketfox.io/xssfox/2026/07/01/cricut-unlock/) | ⭐ 27 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=49365841) |
| **7** | [Casio F-B100W-1A](https://www.casio.com/uk/watches/casio/product.F-B100W-1A/) | ⭐ 173 | 💬 141 | [HN Thread](https://news.ycombinator.com/item?id=49362887) |
| **8** | [Ornith-1.5: From Self-Scaffolding to Self-Improvement](https://ornith.ai/ornith_1_5.html) | ⭐ 133 | 💬 34 | [HN Thread](https://news.ycombinator.com/item?id=49362401) |
| **9** | [Geolocating a random island using geometry and CUDA programming](https://yassa9.github.io/osint/gralhix-004/) | ⭐ 346 | 💬 60 | [HN Thread](https://news.ycombinator.com/item?id=49360545) |
| **10** | [Ramp Launches a Model Router](https://router.com) | ⭐ 26 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=49366067) |

---

## 🗄️ News Archive

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
