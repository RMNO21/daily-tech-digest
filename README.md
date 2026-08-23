# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Sydney Marathon medal mistakenly depicts Munich stadium](https://www.bbc.com/news/articles/cvg92y1wzn8o) | ⭐ 27 | 💬 13 | [HN Thread](https://news.ycombinator.com/item?id=49407576) |
| **2** | [To become a better writer, read as much as you can](https://nappertime.com/the-golden-rule-of-becoming-a-better-writer/) | ⭐ 238 | 💬 154 | [HN Thread](https://news.ycombinator.com/item?id=49405870) |
| **3** | [The End of an Athlon](http://www.os2museum.com/wp/the-end-of-an-athlon/) | ⭐ 124 | 💬 40 | [HN Thread](https://news.ycombinator.com/item?id=49406333) |
| **4** | [Show HN: Live 3D satellite tracker and the declassified Pentagon UFO archive](https://skylens.yantraai.app/) | ⭐ 21 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49407309) |
| **5** | [JIT Compiling Code in 5μs](https://malisper.me/jit-compiling-code-in-5-us/) | ⭐ 91 | 💬 50 | [HN Thread](https://news.ycombinator.com/item?id=49406387) |
| **6** | [MartyPC is a cross-platform emulator of early PCs written in Rust](https://martypc.net/) | ⭐ 138 | 💬 49 | [HN Thread](https://news.ycombinator.com/item?id=49405816) |
| **7** | [I gave Qwen 3.8 27B a reverse-engineering job and it finished in 30 minutes](https://www.xda-developers.com/qwen-3-8-27b-reverse-engineering-job-frontier-model/) | ⭐ 64 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=49407507) |
| **8** | [Fast and Hard Code](https://lucumr.pocoo.org/2026/8/22/fast-hard-code/) | ⭐ 59 | 💬 21 | [HN Thread](https://news.ycombinator.com/item?id=49406285) |
| **9** | [Why your local LLM feels dumber than it is](https://forum.level1techs.com/t/why-your-local-llm-feels-dumber-than-it-is/253917) | ⭐ 389 | 💬 151 | [HN Thread](https://news.ycombinator.com/item?id=49402232) |
| **10** | [The Art and Beauty of Blade Runner (2015)](https://nappertime.com/the-art-of-and-beauty-of-blade-runner/) | ⭐ 109 | 💬 46 | [HN Thread](https://news.ycombinator.com/item?id=49405331) |

---

## 🗄️ News Archive

- 📅 [2026-08-23](archive/2026-08-23.md)
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
