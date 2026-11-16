# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Outages reported at Bank of America, Chase, U.S. Bank, Wells Fargo and Zelle](https://apnews.com/article/bank-outage-chase-wells-fargo-truist-50fee2693c22f597fa6ca51a97ef2cda) | ⭐ 603 | 💬 466 | [HN Thread](https://news.ycombinator.com/item?id=50521045) |
| **2** | [Carnegie Mellon is putting computer science courses on YouTube for free](https://www.cs.cmu.edu/learn/) | ⭐ 49 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=50522980) |
| **3** | [Rust changed me as a developer](https://blog.startifact.com/posts/how-rust-changed-me/) | ⭐ 71 | 💬 30 | [HN Thread](https://news.ycombinator.com/item?id=50522563) |
| **4** | [Grazing sheep in fields with solar arrays](https://news.cornell.edu/stories/2026/10/sheep-grazing-solar-fields-offers-farmers-economic-ecological-gains) | ⭐ 170 | 💬 140 | [HN Thread](https://news.ycombinator.com/item?id=50520182) |
| **5** | [Jiff 1.0: A datetime library for Rust](https://burntsushi.net/jiff/) | ⭐ 252 | 💬 54 | [HN Thread](https://news.ycombinator.com/item?id=50519744) |
| **6** | [Frame – 31.5" color ePaper display](https://trmnl.com/blog/introducing-frame) | ⭐ 227 | 💬 145 | [HN Thread](https://news.ycombinator.com/item?id=50519354) |
| **7** | [Spamhaus new email sender requirements in November](https://www.spamhaus.org/sender-guidelines/) | ⭐ 12 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=50523784) |
| **8** | [Squircles](https://linebender.org/wiki/curves/squircle/) | ⭐ 69 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=50515151) |
| **9** | [Launch HN: Axonnic (YC F26) – Sleeves that track fingers and estimate force](https://news.ycombinator.com/item?id=50522776) | ⭐ 21 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=50522776) |
| **10** | [My Quest to push native Three.js quality match AAA Game Engines](https://ben3d.ca/blog/building-the-aaa-lighting-pipeline-in-threejs) | ⭐ 39 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=50523291) |

---

## 🗄️ News Archive

- 📅 [2026-11-16](archive/2026-11-16.md)
- 📅 [2026-11-15](archive/2026-11-15.md)
- 📅 [2026-11-14](archive/2026-11-14.md)
- 📅 [2026-11-11](archive/2026-11-11.md)
- 📅 [2026-11-10](archive/2026-11-10.md)
- 📅 [2026-11-09](archive/2026-11-09.md)
- 📅 [2026-11-08](archive/2026-11-08.md)
- 📅 [2026-11-07](archive/2026-11-07.md)
- 📅 [2026-11-06](archive/2026-11-06.md)
- 📅 [2026-11-05](archive/2026-11-05.md)
- 📅 [2026-11-04](archive/2026-11-04.md)
- 📅 [2026-11-03](archive/2026-11-03.md)
- 📅 [2026-11-02](archive/2026-11-02.md)
- 📅 [2026-10-31](archive/2026-10-31.md)

*... and [72 older editions in the archive folder](archive/)*

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
