# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [How Hacker News ranking works: scoring, controversy, and penalties (2013)](https://www.righto.com/2013/11/how-hacker-news-ranking-really-works.html) | ⭐ 41 | 💬 15 | [HN Thread](https://news.ycombinator.com/item?id=49770293) |
| **2** | [I built non-autoregressive decision models with RL a year ago](https://laya.convaiinnovations.com/) | ⭐ 1027 | 💬 238 | [HN Thread](https://news.ycombinator.com/item?id=49765348) |
| **3** | [AI-generated posters don’t have to be horrible](https://john.hartnup.uk/2026/06/07/ai-event-posters.html) | ⭐ 1295 | 💬 711 | [HN Thread](https://news.ycombinator.com/item?id=49764791) |
| **4** | [Measure internet censorship. Contribute to the largest open dataset](https://ooni.org/install) | ⭐ 59 | 💬 36 | [HN Thread](https://news.ycombinator.com/item?id=49769676) |
| **5** | [English: A vs. An](https://www.redblobgames.com/blog/2026-09-16-english-a-vs-an/) | ⭐ 86 | 💬 81 | [HN Thread](https://news.ycombinator.com/item?id=49769944) |
| **6** | [Compiler-style optimization for drawing via Skia](https://arxiv.org/abs/2603.23696) | ⭐ 35 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=49743934) |
| **7** | [Mayday Mysteries](http://www.maydaymystery.org/mayday/) | ⭐ 15 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49770362) |
| **8** | [Two parallel neural ectoderm progenitors contribute to the developing brain](https://med.stanford.edu/news/all-news/2026/09/two-separate-brains.html) | ⭐ 599 | 💬 229 | [HN Thread](https://news.ycombinator.com/item?id=49763697) |
| **9** | [Deodands put a price on objects that caused death](https://daily.jstor.org/how-the-railways-killed-a-medieval-law/) | ⭐ 29 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49731996) |
| **10** | [UFO Series Home Page: "UFO" TV Series from 1970](https://ufoseries.com/) | ⭐ 42 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=49754194) |

---

## 🗄️ News Archive

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
- 📅 [2026-09-06](archive/2026-09-06.md)
- 📅 [2026-09-05](archive/2026-09-05.md)

*... and [22 older editions in the archive folder](archive/)*

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
