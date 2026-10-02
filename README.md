# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Dutch computer museums (2022)](https://aresluna.org/dutch-computer-museums/) | ⭐ 64 | 💬 15 | [HN Thread](https://news.ycombinator.com/item?id=49935751) |
| **2** | [Court agrees with EFF: Utah's VPN law demands a technical impossibility](https://www.eff.org/deeplinks/2026/10/court-agrees-eff-utahs-vpn-law-demands-technical-impossibility) | ⭐ 163 | 💬 67 | [HN Thread](https://news.ycombinator.com/item?id=49927754) |
| **3** | [The Legend of von Neumann (1973) [pdf]](https://gwern.net/doc/math/1973-halmos.pdf) | ⭐ 185 | 💬 97 | [HN Thread](https://news.ycombinator.com/item?id=49933235) |
| **4** | [FLUX 3 Image](https://bfl.ai/models/flux-3-image) | ⭐ 137 | 💬 23 | [HN Thread](https://news.ycombinator.com/item?id=49925974) |
| **5** | [Sites in ChatGPT](https://chatgpt.com/features/sites/) | ⭐ 56 | 💬 63 | [HN Thread](https://news.ycombinator.com/item?id=49927747) |
| **6** | [Show HN: Giving Opus 5.5 a simulated paint canvas](https://stillwet.art/) | ⭐ 105 | 💬 35 | [HN Thread](https://news.ycombinator.com/item?id=49928566) |
| **7** | [Shimano Bicycle Museum Review](https://inrng.com/2026/10/shimano-bicycle-museum/) | ⭐ 271 | 💬 67 | [HN Thread](https://news.ycombinator.com/item?id=49930047) |
| **8** | [Loss of cell identity drives human aging: Two new papers](https://erictopol.substack.com/p/loss-of-cell-identity-drives-human) | ⭐ 8 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49926411) |
| **9** | [ICC judge on what U.S. sanctions mean for her and global courts](https://www.npr.org/2026/10/01/nx-s1-5977815/trump-icc-sanctions-kimberly-prost) | ⭐ 142 | 💬 53 | [HN Thread](https://news.ycombinator.com/item?id=49935867) |
| **10** | [Giving friends custom text buzzes based on Morse code](https://liquidbrain.net/blog/giving-friends-custom-text-buzzes-based-on-morse-code/) | ⭐ 39 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=49925653) |

---

## 🗄️ News Archive

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
- 📅 [2026-09-20](archive/2026-09-20.md)
- 📅 [2026-09-19](archive/2026-09-19.md)
- 📅 [2026-09-18](archive/2026-09-18.md)

*... and [34 older editions in the archive folder](archive/)*

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
