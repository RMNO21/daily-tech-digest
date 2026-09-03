# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Pre-Release of Polars 2.0](https://pola.rs/posts/announcing-polars-2/) | ⭐ 66 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49546753) |
| **2** | [Muse Spark 1.3](https://developer.meta.com/ai/models/muse-spark/) | ⭐ 557 | 💬 379 | [HN Thread](https://news.ycombinator.com/item?id=49541256) |
| **3** | [Gemini 3.8 Flash and 3.8 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) | ⭐ 998 | 💬 567 | [HN Thread](https://news.ycombinator.com/item?id=49537553) |
| **4** | [Three schoolgirls in Kinsale pulled up a pea plant covered in warts (2016)](https://scienceblog.com/b-three-schoolgirls-in-kinsale-pulled-up-a-pea-plant-covered-in-warts-and-instead-of-binning-it-spent-three-years-testing-13000-seeds-in-a-spare-bedroom-the-bacteria-living-in-those-warts-made-barley/) | ⭐ 15 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49546800) |
| **5** | [LLMs and Self-Referentiality](https://scottaaronson.blog/?p=10046) | ⭐ 32 | 💬 15 | [HN Thread](https://news.ycombinator.com/item?id=49530169) |
| **6** | [The Computer Museum of America reclamation project](https://computer-museum.org/wp/) | ⭐ 37 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49511493) |
| **7** | [Holden's Lightning Flight](https://en.wikipedia.org/wiki/Holden%27s_Lightning_flight) | ⭐ 148 | 💬 28 | [HN Thread](https://news.ycombinator.com/item?id=49508405) |
| **8** | [The Browser's Main Thread Is Expensive](https://kciter.so/posts/the-expensive-main-thread/en/) | ⭐ 4 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49522137) |
| **9** | [Three sites made 215,128 “best software” pages for AI. Perplexity cites them](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/) | ⭐ 403 | 💬 194 | [HN Thread](https://news.ycombinator.com/item?id=49536375) |
| **10** | [Google avoids a breakup of its ad tech business](https://www.nytimes.com/2026/09/02/technology/google-ad-tech-remedies.html) | ⭐ 368 | 💬 275 | [HN Thread](https://news.ycombinator.com/item?id=49537131) |

---

## 🗄️ News Archive

- 📅 [2026-09-03](archive/2026-09-03.md)
- 📅 [2026-09-02](archive/2026-09-02.md)
- 📅 [2026-09-01](archive/2026-09-01.md)
- 📅 [2026-08-31](archive/2026-08-31.md)
- 📅 [2026-08-30](archive/2026-08-30.md)
- 📅 [2026-08-29](archive/2026-08-29.md)
- 📅 [2026-08-28](archive/2026-08-28.md)
- 📅 [2026-08-27](archive/2026-08-27.md)
- 📅 [2026-08-26](archive/2026-08-26.md)
- 📅 [2026-08-25](archive/2026-08-25.md)
- 📅 [2026-08-24](archive/2026-08-24.md)
- 📅 [2026-08-23](archive/2026-08-23.md)
- 📅 [2026-08-22](archive/2026-08-22.md)
- 📅 [2026-08-21](archive/2026-08-21.md)

*... and [7 older editions in the archive folder](archive/)*

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
