# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Fable 5.1 Solves the Cyphral Distich, a 370-year-old cipher](https://www.vals.ai/blogs/fable-solves-cyphral-distich) | ⭐ 734 | 💬 311 | [HN Thread](https://news.ycombinator.com/item?id=49688695) |
| **2** | [Spaceships (Reverse Asteroid)](https://spaceships.treybastian.com/) | ⭐ 141 | 💬 28 | [HN Thread](https://news.ycombinator.com/item?id=49638510) |
| **3** | [Registration without a phone number on Signal will use zero-knowledge proofs](https://community.signalusers.org/t/registration-without-a-phone-number/2222?page=10) | ⭐ 193 | 💬 86 | [HN Thread](https://news.ycombinator.com/item?id=49689048) |
| **4** | [The case against JPEG XL](https://giannirosato.com/blog/post/case-against-jxl/) | ⭐ 100 | 💬 121 | [HN Thread](https://news.ycombinator.com/item?id=49690554) |
| **5** | [Apple's Dimensional Drawings](https://developer.apple.com/accessories/dimensional-drawings/) | ⭐ 121 | 💬 37 | [HN Thread](https://news.ycombinator.com/item?id=49690174) |
| **6** | [Astra and Fable still hack on simple variants of alignment evals from 2025](https://www.lesswrong.com/posts/munJKF7iWMsWJLAH2/astra-and-fable-still-hack-on-simple-variants-of-alignment) | ⭐ 416 | 💬 188 | [HN Thread](https://news.ycombinator.com/item?id=49684393) |
| **7** | [Rope, twine and thread: Invisible technologies of the Stone Age](https://knowablemagazine.org/content/article/society/2026/prehistory-lost-threads) | ⭐ 31 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49662246) |
| **8** | [Data collected by cars and sold to third parties](https://www.theverge.com/column/994172/your-car-is-selling-your-data) | ⭐ 377 | 💬 199 | [HN Thread](https://news.ycombinator.com/item?id=49683953) |
| **9** | [Julia 1.13 highlights](https://julialang.org/blog/2026/09/julia-1.13-highlights/) | ⭐ 196 | 💬 18 | [HN Thread](https://news.ycombinator.com/item?id=49642645) |
| **10** | [The Malicious Use of Artificial Intelligence](https://arxiv.org/abs/1802.07228) | ⭐ 40 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=49690678) |

---

## 🗄️ News Archive

- 📅 [2026-09-14](archive/2026-09-14.md)
- 📅 [2026-09-13](archive/2026-09-13.md)
- 📅 [2026-09-12](archive/2026-09-12.md)
- 📅 [2026-09-11](archive/2026-09-11.md)
- 📅 [2026-09-10](archive/2026-09-10.md)
- 📅 [2026-09-09](archive/2026-09-09.md)
- 📅 [2026-09-08](archive/2026-09-08.md)
- 📅 [2026-09-07](archive/2026-09-07.md)
- 📅 [2026-09-06](archive/2026-09-06.md)
- 📅 [2026-09-05](archive/2026-09-05.md)
- 📅 [2026-09-04](archive/2026-09-04.md)
- 📅 [2026-09-03](archive/2026-09-03.md)
- 📅 [2026-09-02](archive/2026-09-02.md)
- 📅 [2026-09-01](archive/2026-09-01.md)

*... and [18 older editions in the archive folder](archive/)*

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
