# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Can gzip be a language model?](https://nathan.rs/posts/gzip-lm/) | ⭐ 136 | 💬 55 | [HN Thread](https://news.ycombinator.com/item?id=49797323) |
| **2** | [Study: Young users (9 to 18Y) ditch Google for AI, with unknown consequences](https://norwegianscitechnews.com/2026/09/young-users-ditch-google-for-ai-with-unknown-consequences/) | ⭐ 19 | 💬 19 | [HN Thread](https://news.ycombinator.com/item?id=49798451) |
| **3** | [MiMo v2.6](https://mimo.xiaomi.com/mimo-v2-6) | ⭐ 906 | 💬 402 | [HN Thread](https://news.ycombinator.com/item?id=49792730) |
| **4** | [Spymarks, Not Watermarks](https://brand.io/article/spymarks/) | ⭐ 444 | 💬 110 | [HN Thread](https://news.ycombinator.com/item?id=49794615) |
| **5** | [I said no and Apple said yes](https://dbushell.com/2026/09/22/apple-intelligence/) | ⭐ 128 | 💬 70 | [HN Thread](https://news.ycombinator.com/item?id=49797982) |
| **6** | [AMD's random number generator can't generate a 0?](https://board.flatassembler.net/topic.php?t=24261) | ⭐ 13 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49798204) |
| **7** | [Transformers Explained Visually](https://poloclub.github.io/transformer-explainer/) | ⭐ 412 | 💬 64 | [HN Thread](https://news.ycombinator.com/item?id=49792342) |
| **8** | [Attention is all you have](https://alicegg.tech/2026/09/21/attention) | ⭐ 812 | 💬 243 | [HN Thread](https://news.ycombinator.com/item?id=49787726) |
| **9** | [What Sun got wrong](https://bcantrill.dtrace.org/2026/09/20/what-sun-got-wrong/) | ⭐ 592 | 💬 342 | [HN Thread](https://news.ycombinator.com/item?id=49787436) |
| **10** | [MiMo-v2.6-Pro: Intelligence, Performance and Price Analysis](https://artificialanalysis.ai/models/mimo-v2-6-pro) | ⭐ 64 | 💬 18 | [HN Thread](https://news.ycombinator.com/item?id=49796660) |

---

## 🗄️ News Archive

- 📅 [2026-09-22](archive/2026-09-22.md)
- 📅 [2026-09-21](archive/2026-09-21.md)
- 📅 [2026-09-20](archive/2026-09-20.md)
- 📅 [2026-09-19](archive/2026-09-19.md)
- 📅 [2026-09-18](archive/2026-09-18.md)
- 📅 [2026-09-16](archive/2026-09-16.md)
- 📅 [2026-09-15](archive/2026-09-15.md)
- 📅 [2026-09-14](archive/2026-09-14.md)
- 📅 [2026-09-13](archive/2026-09-13.md)
- 📅 [2026-09-12](archive/2026-09-12.md)
- 📅 [2026-09-11](archive/2026-09-11.md)
- 📅 [2026-09-10](archive/2026-09-10.md)
- 📅 [2026-09-09](archive/2026-09-09.md)
- 📅 [2026-09-08](archive/2026-09-08.md)

*... and [25 older editions in the archive folder](archive/)*

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
