# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [There's no reason for software to be slow anymore](https://danluu.com/perf-opt/) | ⭐ 171 | 💬 139 | [HN Thread](https://news.ycombinator.com/item?id=49395628) |
| **2** | [Felony Bench](https://www.felonybench.com/) | ⭐ 585 | 💬 244 | [HN Thread](https://news.ycombinator.com/item?id=49389430) |
| **3** | [Rust Glancer: Rust LSP using 100x less RAM](https://rust-glancer.github.io/blog/hello-world/) | ⭐ 79 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=49393052) |
| **4** | [Kobo can run apps now](https://bandarlabs.github.io/Cobalt/) | ⭐ 467 | 💬 164 | [HN Thread](https://news.ycombinator.com/item?id=49390427) |
| **5** | [Initial focus for our partnership with Motorola is a regular non-folding device](https://grapheneos.social/@GrapheneOS/117136278553665985) | ⭐ 41 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=49395605) |
| **6** | [Early Humans Likely Ate Carbs and Sugary Foods](https://www.history.com/articles/early-human-ancestors-diet-sugar-carbs) | ⭐ 16 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=49396086) |
| **7** | [Three important steps in my maturation process](https://thomasdullien.github.io/posts/2026-08-21-three-important-steps-in-my-maturation-process/) | ⭐ 90 | 💬 26 | [HN Thread](https://news.ycombinator.com/item?id=49394496) |
| **8** | [Scientists release biggest 2D map of the universe](https://newscenter.lbl.gov/2026/08/10/scientists-release-biggest-2d-map-of-the-universe/) | ⭐ 165 | 💬 52 | [HN Thread](https://news.ycombinator.com/item?id=49392200) |
| **9** | [Kagi added a setting for removing paywalled links from search results](https://kagi.com/changelog#11296) | ⭐ 1047 | 💬 349 | [HN Thread](https://news.ycombinator.com/item?id=49388154) |
| **10** | [Felony charges for citizen deleting phone data at US Border](https://www.nytimes.com/2026/08/21/us/politics/samuel-tunick-deleted-phone-felony.html) | ⭐ 637 | 💬 794 | [HN Thread](https://news.ycombinator.com/item?id=49386895) |

---

## 🗄️ News Archive

- 📅 [2026-08-22](archive/2026-08-22.md)
- 📅 [2026-08-21](archive/2026-08-21.md)
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
