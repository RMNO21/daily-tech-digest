# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Beware Management Consultants](https://about.iceland.co.uk/our-story/the-dark-ages/beware-management-consultants/) | ⭐ 82 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=49351324) |
| **2** | [Turbovec – Google's TurboQuant for vector search in Rust](https://github.com/RyanCodrai/turbovec) | ⭐ 120 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=49349898) |
| **3** | [The Amazon tax](https://seths.blog/2026/08/the-amazon-tax/) | ⭐ 657 | 💬 436 | [HN Thread](https://news.ycombinator.com/item?id=49345263) |
| **4** | [Using the railway network as a flatbed scanner](https://philo.gay/linecam/) | ⭐ 329 | 💬 53 | [HN Thread](https://news.ycombinator.com/item?id=49344825) |
| **5** | [How does IKEA come up with names for its products?](https://www.ikea.com/se/en/customer-service/knowledge/articles/6f564c4d-2ccc-46de-b643-545a3948dc79.html) | ⭐ 126 | 💬 82 | [HN Thread](https://news.ycombinator.com/item?id=49349984) |
| **6** | [Fixing a bricked Framework laptop](https://quantum5.ca/2026/08/16/fixing-bricked-amd-7040-series-framework-13-laptop-with-20-tools/) | ⭐ 287 | 💬 191 | [HN Thread](https://news.ycombinator.com/item?id=49345220) |
| **7** | [Cursor launches Origin, GitHub alternative](https://cursor.com/changelog/origin-code-hosting) | ⭐ 324 | 💬 251 | [HN Thread](https://news.ycombinator.com/item?id=49334209) |
| **8** | [Norway Should Buy OpenAI](https://www.onethousandmeans.com/p/norway-should-buy-openai) | ⭐ 120 | 💬 117 | [HN Thread](https://news.ycombinator.com/item?id=49351330) |
| **9** | [Linux 7.3 improves performance when running out of vRAM](https://pixelcluster.dev/VRAM-Overcommit/) | ⭐ 464 | 💬 216 | [HN Thread](https://news.ycombinator.com/item?id=49342719) |
| **10** | [Pacing model development in an era of cyber-critical capabilities](https://openai.com/index/pacing-model-development-cyber-capabilities/) | ⭐ 26 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49350031) |

---

## 🗄️ News Archive

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
