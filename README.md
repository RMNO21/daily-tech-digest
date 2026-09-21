# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [What Sun got wrong](https://bcantrill.dtrace.org/2026/09/20/what-sun-got-wrong/) | ⭐ 375 | 💬 199 | [HN Thread](https://news.ycombinator.com/item?id=49787436) |
| **2** | [Attention is all you have](https://alicegg.tech/2026/09/21/attention) | ⭐ 356 | 💬 101 | [HN Thread](https://news.ycombinator.com/item?id=49787726) |
| **3** | [Turn off and restrict access to Apple Intelligence features on Mac](https://support.apple.com/guide/mac-help/turn-restrict-access-apple-intelligence-mchlb2e44f94/mac) | ⭐ 105 | 💬 72 | [HN Thread](https://news.ycombinator.com/item?id=49790409) |
| **4** | [Why Does an NPM Math Library Need an Encrypted Loader?](https://safedep.io/mathmain-encrypted-loader/) | ⭐ 34 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49791378) |
| **5** | [Grok 4.7](https://x.ai/news/grok-4-7) | ⭐ 341 | 💬 285 | [HN Thread](https://news.ycombinator.com/item?id=49788838) |
| **6** | [In Search of a Compositional Theory of Self-Stabilization](http://muratbuffalo.blogspot.com/2026/09/in-search-of-compositional-theory-of.html) | ⭐ 9 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49791797) |
| **7** | [US halts flights at busy East Coast airports, says fiber line cut](https://www.reuters.com/world/us/faa-halts-some-us-east-coast-flights-due-communication-issues-2026-09-21/) | ⭐ 63 | 💬 23 | [HN Thread](https://news.ycombinator.com/item?id=49791509) |
| **8** | [Avoiding the babbling-idiot failure in a time-triggered communication system](https://ieeexplore.ieee.org/document/689473) | ⭐ 13 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49791117) |
| **9** | [Python Workers are now generally available](https://blog.cloudflare.com/python-workers-ga/) | ⭐ 121 | 💬 15 | [HN Thread](https://news.ycombinator.com/item?id=49787142) |
| **10** | [This Digital Radio Gets Messages to the World’s Remotest Locations](https://spectrum.ieee.org/hermes-shortwave-radio-digital-data) | ⭐ 49 | 💬 26 | [HN Thread](https://news.ycombinator.com/item?id=49789228) |

---

## 🗄️ News Archive

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
- 📅 [2026-09-07](archive/2026-09-07.md)

*... and [24 older editions in the archive folder](archive/)*

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
