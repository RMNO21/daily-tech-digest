# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Apple introduces M6 and M5 Ultra for a big leap in performance and AI compute](https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/) | ⭐ 485 | 💬 402 | [HN Thread](https://news.ycombinator.com/item?id=49433292) |
| **2** | [New Mac Studio with M5 Max and M5 Ultra](https://www.apple.com/newsroom/2026/08/apple-introduces-new-mac-studio-with-m5-max-and-m5-ultra/) | ⭐ 448 | 💬 289 | [HN Thread](https://news.ycombinator.com/item?id=49433316) |
| **3** | [New Mac mini, featuring M6 and M5 Pro](https://www.apple.com/newsroom/2026/08/apple-unveils-a-more-powerful-mac-mini-featuring-the-all-new-m6-and-m5-pro/) | ⭐ 214 | 💬 121 | [HN Thread](https://news.ycombinator.com/item?id=49433450) |
| **4** | [Qwen 3.8-Flash-Next releasing tomorrow (125B a6B)](https://modelscope.cn/models/Qwen/Qwen3.8-Flash-Next) | ⭐ 199 | 💬 83 | [HN Thread](https://news.ycombinator.com/item?id=49432317) |
| **5** | [Bomb Fishing Is Wreaking Havoc on Indonesia's Coral Reefs](https://e360.yale.edu/digest/bomb-fishing-coral-reefs) | ⭐ 103 | 💬 73 | [HN Thread](https://news.ycombinator.com/item?id=49434820) |
| **6** | [Don't Wordle](https://dontwordle.com/) | ⭐ 197 | 💬 82 | [HN Thread](https://news.ycombinator.com/item?id=49432319) |
| **7** | [HelloAssembly The smallest possible complete Windows application](https://github.com/PlummersSoftwareLLC/HelloAssembly) | ⭐ 62 | 💬 34 | [HN Thread](https://news.ycombinator.com/item?id=49432227) |
| **8** | [Beyond Good and Evil: Nietzsche and the Great War](https://www.historytoday.com/archive/feature/beyond-good-and-evil-nietzsche-and-great-war) | ⭐ 13 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=49435495) |
| **9** | [AI is hitting entry-level jobs hardest, Stanford study finds](https://arstechnica.com/ai/2026/08/ai-is-hitting-entry-level-jobs-hardest-stanford-study-finds/) | ⭐ 56 | 💬 34 | [HN Thread](https://news.ycombinator.com/item?id=49435147) |
| **10** | [MySQL CDC to BigQuery: what periodic syncs miss, and how binlog avoids it](https://www.erathos.com/en/blog/mysql-cdc-to-bigquery) | ⭐ 18 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49434613) |

---

## 🗄️ News Archive

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
