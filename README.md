# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [A 3D fruit fly on macOS desktop powered by the real FlyWire connectome](https://github.com/DenisSergeevitch/desktop-fly) | ⭐ 141 | 💬 34 | [HN Thread](https://news.ycombinator.com/item?id=49353221) |
| **2** | [The Amazon tax](https://seths.blog/2026/08/the-amazon-tax/) | ⭐ 925 | 💬 535 | [HN Thread](https://news.ycombinator.com/item?id=49345263) |
| **3** | [Solo – a .so loader for static Linux binaries](https://github.com/pg83/solo) | ⭐ 32 | 💬 38 | [HN Thread](https://news.ycombinator.com/item?id=49354613) |
| **4** | [How does IKEA come up with names for its products?](https://www.ikea.com/se/en/customer-service/knowledge/articles/6f564c4d-2ccc-46de-b643-545a3948dc79.html) | ⭐ 222 | 💬 140 | [HN Thread](https://news.ycombinator.com/item?id=49349984) |
| **5** | [Show HN: Interactive, animated architecture of any HuggingFace models](https://modelmap.cc) | ⭐ 28 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49354664) |
| **6** | [Turbovec – Google's TurboQuant for vector search in Rust](https://github.com/RyanCodrai/turbovec) | ⭐ 202 | 💬 27 | [HN Thread](https://news.ycombinator.com/item?id=49349898) |
| **7** | [AI usage patterns in software teams](https://linear.app/data) | ⭐ 35 | 💬 18 | [HN Thread](https://news.ycombinator.com/item?id=49353432) |
| **8** | [Being ambitious and being a dad](https://nicholascharriere.com/blog/being-ambitious-and-being-a-dad/) | ⭐ 261 | 💬 142 | [HN Thread](https://news.ycombinator.com/item?id=49321298) |
| **9** | [Using the railway network as a flatbed scanner](https://philo.gay/linecam/) | ⭐ 396 | 💬 64 | [HN Thread](https://news.ycombinator.com/item?id=49344825) |
| **10** | [Cursor launches Origin, GitHub alternative](https://cursor.com/changelog/origin-code-hosting) | ⭐ 462 | 💬 361 | [HN Thread](https://news.ycombinator.com/item?id=49334209) |

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
