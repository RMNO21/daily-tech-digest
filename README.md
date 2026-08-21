# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Kobo can run apps now](https://bandarlabs.github.io/Cobalt/) | ⭐ 256 | 💬 94 | [HN Thread](https://news.ycombinator.com/item?id=49390427) |
| **2** | [Felony Bench](https://www.felonybench.com/) | ⭐ 307 | 💬 142 | [HN Thread](https://news.ycombinator.com/item?id=49389430) |
| **3** | [Scientists release biggest 2D map of the universe](https://newscenter.lbl.gov/2026/08/10/scientists-release-biggest-2d-map-of-the-universe/) | ⭐ 56 | 💬 16 | [HN Thread](https://news.ycombinator.com/item?id=49392200) |
| **4** | [Kagi added a setting for removing paywalled links from search results](https://kagi.com/changelog#11296) | ⭐ 861 | 💬 295 | [HN Thread](https://news.ycombinator.com/item?id=49388154) |
| **5** | [AI boosted homework scores, then exam scores dropped: study](https://www.economist.com/graphic-detail/2026/08/18/does-ai-stop-children-from-learning) | ⭐ 137 | 💬 190 | [HN Thread](https://news.ycombinator.com/item?id=49357530) |
| **6** | [Quick impressions: A week of using Codex more than Claude](https://allaboutcoding.ghinda.com/a-week-of-using-codex-more-than-claude/) | ⭐ 13 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49393051) |
| **7** | [I accidentally logged hundreds of thousands of phone calls to military bases](https://lina.sh/blog/hijacking-e164-arpa) | ⭐ 326 | 💬 38 | [HN Thread](https://news.ycombinator.com/item?id=49387570) |
| **8** | [Felony charges for citizen deleting phone data at US Border](https://www.nytimes.com/2026/08/21/us/politics/samuel-tunick-deleted-phone-felony.html) | ⭐ 200 | 💬 283 | [HN Thread](https://news.ycombinator.com/item?id=49386895) |
| **9** | [People of ACM – Russ Cox](https://www.acm.org/articles/people-of-acm/2026/russ-cox) | ⭐ 34 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49327408) |
| **10** | [A look under our trunk: what's in our compute](https://waymo.com/blog/2026/08/look-under-our-trunk/) | ⭐ 49 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=49374853) |

---

## 🗄️ News Archive

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
