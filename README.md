# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [/dev/null: social network for developers](https://dev-null.sh) | ⭐ 37 | 💬 35 | [HN Thread](https://news.ycombinator.com/item?id=50121004) |
| **2** | [JPEG XL vs. AVIF for web use-cases](https://jakearchibald.com/2026/jpeg-xl-vs-avif/) | ⭐ 51 | 💬 27 | [HN Thread](https://news.ycombinator.com/item?id=50120224) |
| **3** | [Apple ML Research: Muse Spark Open with MLX on Mac Studio](https://machinelearning.apple.com/research/mlx-distributed-inference) | ⭐ 139 | 💬 72 | [HN Thread](https://news.ycombinator.com/item?id=50118320) |
| **4** | [Desire to Move Permanently to U.S. at New Low](https://news.gallup.com/poll/708614/desire-migrate-drops-new-low.aspx) | ⭐ 102 | 💬 78 | [HN Thread](https://news.ycombinator.com/item?id=50120664) |
| **5** | [Big Fish: Exploiting a 37-Year-Old Kernel Bug in OpenBSD](https://calif.io/research/big-fish) | ⭐ 93 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=50118977) |
| **6** | [What on Earth Is Dekton?](https://www.worksinprogress.news/p/porcelain) | ⭐ 72 | 💬 21 | [HN Thread](https://news.ycombinator.com/item?id=50118828) |
| **7** | [Piramidal (YC W24) Is Hiring](https://job-boards.greenhouse.io/piramidalinc/jobs/4443102009) | ⭐ 1 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50121188) |
| **8** | [Show HN: Gemini 4 Argon plays StarCraft](https://starskirmish.com/bench/v0-2/) | ⭐ 83 | 💬 44 | [HN Thread](https://news.ycombinator.com/item?id=50118688) |
| **9** | [I Love Software Rendering](https://www.jamesfmackenzie.com/2026/10/13/i-love-software-rendering/) | ⭐ 207 | 💬 144 | [HN Thread](https://news.ycombinator.com/item?id=50117746) |
| **10** | [Stolen Renoir paintings found hidden, and damaged, behind cinder block wall](https://www.cbsnews.com/news/stolen-renoir-paintings-found-behind-wall-france/) | ⭐ 42 | 💬 30 | [HN Thread](https://news.ycombinator.com/item?id=50074322) |

---

## 🗄️ News Archive

- 📅 [2026-10-16](archive/2026-10-16.md)
- 📅 [2026-10-15](archive/2026-10-15.md)
- 📅 [2026-10-14](archive/2026-10-14.md)
- 📅 [2026-10-13](archive/2026-10-13.md)
- 📅 [2026-10-10](archive/2026-10-10.md)
- 📅 [2026-10-09](archive/2026-10-09.md)
- 📅 [2026-10-08](archive/2026-10-08.md)
- 📅 [2026-10-07](archive/2026-10-07.md)
- 📅 [2026-10-05](archive/2026-10-05.md)
- 📅 [2026-10-04](archive/2026-10-04.md)
- 📅 [2026-10-03](archive/2026-10-03.md)
- 📅 [2026-10-02](archive/2026-10-02.md)
- 📅 [2026-10-01](archive/2026-10-01.md)
- 📅 [2026-09-30](archive/2026-09-30.md)

*... and [45 older editions in the archive folder](archive/)*

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
