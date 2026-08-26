# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Omarchy is full of security holes](https://blog.happyfellow.dev/merchants-of-insecurity/) | ⭐ 161 | 💬 141 | [HN Thread](https://news.ycombinator.com/item?id=49447682) |
| **2** | [RAG Is Simpler Than You Think](https://www.lighthousenewsletter.com/p/rag-is-simpler-than-you-think) | ⭐ 171 | 💬 83 | [HN Thread](https://news.ycombinator.com/item?id=49445727) |
| **3** | [Oldinsurancemaps.net is now a Charter Project](https://openstreetmap.us/news/2026/08/oim-charter-project/) | ⭐ 97 | 💬 16 | [HN Thread](https://news.ycombinator.com/item?id=49445873) |
| **4** | [Z.ai confirms Ox Alpha is a new GLM-series model and will release its weights](https://www.bloomberg.com/news/articles/2026-08-26/china-s-z-ai-made-ox-alpha-stealth-model-that-rivals-deepseek) | ⭐ 203 | 💬 89 | [HN Thread](https://news.ycombinator.com/item?id=49446422) |
| **5** | [XCancel and Nitter are receiving C&D letters from XCorp](https://news.ycombinator.com/item?id=49446210) | ⭐ 110 | 💬 38 | [HN Thread](https://news.ycombinator.com/item?id=49446210) |
| **6** | [Apple introduces M6 and M5 Ultra](https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/) | ⭐ 1209 | 💬 1169 | [HN Thread](https://news.ycombinator.com/item?id=49433292) |
| **7** | [Beyond Recall and the Illusion of Competence](https://var0.xyz/posts/beyond-recall-and-the-illusion-of-competence.html) | ⭐ 34 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=49446442) |
| **8** | [Proliferate (YC S25) Is Hiring](https://www.ycombinator.com/companies/proliferate/jobs/OgpCKYJ-founding-product-engineer) | ⭐ 1 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49447480) |
| **9** | [Value Classes Still Need Compiler Sympathy](https://johan-sjolen.github.io/post/compiler-sympathy/compiler-sympathy/) | ⭐ 49 | 💬 19 | [HN Thread](https://news.ycombinator.com/item?id=49445884) |
| **10** | [Stalking the Wily Hacker: 40 years later – Cliff Stoll [video]](https://www.youtube.com/watch?v=656058JxTM0) | ⭐ 151 | 💬 45 | [HN Thread](https://news.ycombinator.com/item?id=49395802) |

---

## 🗄️ News Archive

- 📅 [2026-08-26](archive/2026-08-26.md)
- 📅 [2026-08-25](archive/2026-08-25.md)
- 📅 [2026-08-24](archive/2026-08-24.md)
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
