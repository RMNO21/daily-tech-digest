# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Cloudflare acquires Deno](https://deno.com/blog/cloudflare) | ⭐ 912 | 💬 488 | [HN Thread](https://news.ycombinator.com/item?id=50019911) |
| **2** | [No Man Is an Island](https://borretti.me/article/no-man-is-an-island) | ⭐ 75 | 💬 27 | [HN Thread](https://news.ycombinator.com/item?id=50025935) |
| **3** | [Triple-A Minesweeper](https://minesweeper.mikelacher.com/) | ⭐ 318 | 💬 71 | [HN Thread](https://news.ycombinator.com/item?id=50022292) |
| **4** | [Show HN: Carrier-Explode: iPhone, Pixel and Galaxy carrier settings decoded](https://carrierexplode.com/) | ⭐ 114 | 💬 13 | [HN Thread](https://news.ycombinator.com/item?id=50024499) |
| **5** | [Our $445M Series D](https://oxide.computer/blog/our-445m-series-d) | ⭐ 510 | 💬 210 | [HN Thread](https://news.ycombinator.com/item?id=50020014) |
| **6** | [Ideas aren't getting harder to find, anyone who tells you otherwise is a coward](https://www.experimental-history.com/p/ideas-arent-getting-harder-to-find) | ⭐ 53 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=50024571) |
| **7** | [Typesafe AI raises $870M at $7.5B](https://typesafe.ai/blog/series-ai) | ⭐ 151 | 💬 124 | [HN Thread](https://news.ycombinator.com/item?id=50023450) |
| **8** | [Pointing AI at archives found a forgotten meteorite, lost rhinos, and more](https://jessewaites.com/blog/post/i-pointed-ai-at-400-years-of-archives/) | ⭐ 65 | 💬 30 | [HN Thread](https://news.ycombinator.com/item?id=50019056) |
| **9** | [Sorry, I'm in a meeting](https://iminafleeting.com/) | ⭐ 639 | 💬 211 | [HN Thread](https://news.ycombinator.com/item?id=50018088) |
| **10** | [Show HN: Let your AI agents paint big arrows, boxes and text on your screen](https://github.com/franzenzenhofer/big-arrow-on-the-screen) | ⭐ 345 | 💬 145 | [HN Thread](https://news.ycombinator.com/item?id=50018817) |

---

## 🗄️ News Archive

- 📅 [2026-10-09](archive/2026-10-09.md)
- 📅 [2026-10-08](archive/2026-10-08.md)
- 📅 [2026-10-07](archive/2026-10-07.md)
- 📅 [2026-10-05](archive/2026-10-05.md)
- 📅 [2026-10-04](archive/2026-10-04.md)
- 📅 [2026-10-03](archive/2026-10-03.md)
- 📅 [2026-10-02](archive/2026-10-02.md)
- 📅 [2026-10-01](archive/2026-10-01.md)
- 📅 [2026-09-30](archive/2026-09-30.md)
- 📅 [2026-09-29](archive/2026-09-29.md)
- 📅 [2026-09-28](archive/2026-09-28.md)
- 📅 [2026-09-27](archive/2026-09-27.md)
- 📅 [2026-09-26](archive/2026-09-26.md)
- 📅 [2026-09-25](archive/2026-09-25.md)

*... and [40 older editions in the archive folder](archive/)*

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
