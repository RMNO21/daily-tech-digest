# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [World Labs Is Joining AMD](https://www.worldlabs.ai/blog/amd-announcement) | ⭐ 103 | 💬 28 | [HN Thread](https://news.ycombinator.com/item?id=49883760) |
| **2** | [Jeff – Jev-compatible 0.8B decision models, trained at home, ~30 ms](https://github.com/firelex/jeff) | ⭐ 103 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=49883844) |
| **3** | [Pirating the Pirates](https://mubi.com/en/notebook/posts/pirating-the-pirates) | ⭐ 348 | 💬 168 | [HN Thread](https://news.ycombinator.com/item?id=49880036) |
| **4** | [MicroLLM Lab – Try 7 tiny LLM's in the browser](https://stateofutopia.com/experiments/microllmlab/) | ⭐ 90 | 💬 33 | [HN Thread](https://news.ycombinator.com/item?id=49882781) |
| **5** | [Pacing the Frontier is not the actual goal for AI labs](https://www.lesswrong.com/posts/Nm4ewbYovtjq69dvH/pacing-the-frontier-is-not-the-actual-goal-for-ai-labs) | ⭐ 32 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=49884119) |
| **6** | [12,000-year-old Göbeklitepe burials explain scattered bones](https://archaeologymag.com/2026/09/gobeklitepe-burials-hundreds-of-scattered-bones/) | ⭐ 37 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49855059) |
| **7** | [Scientists solve 1840s space weather mystery](https://arstechnica.com/science/2026/09/scientists-solve-1840s-space-weather-mystery/) | ⭐ 24 | 💬 13 | [HN Thread](https://news.ycombinator.com/item?id=49883536) |
| **8** | [Hijacking the PS5's RTMP stream](https://yashgarg.dev/posts/hijacking-ps5-rtmp-stream/) | ⭐ 161 | 💬 51 | [HN Thread](https://news.ycombinator.com/item?id=49879702) |
| **9** | [Joseph Szabo’s pictures of American adolescents](https://www.newyorker.com/culture/photo-booth/the-teen-portraits-that-captivated-sofia-coppola) | ⭐ 63 | 💬 29 | [HN Thread](https://news.ycombinator.com/item?id=49881606) |
| **10** | [Palantir founder purchases large swath of forest in Sweden](https://www.arctictoday.com/palantir-founder-purchases-large-swath-of-forest-in-sweden/) | ⭐ 69 | 💬 59 | [HN Thread](https://news.ycombinator.com/item?id=49884169) |

---

## 🗄️ News Archive

- 📅 [2026-09-28](archive/2026-09-28.md)
- 📅 [2026-09-27](archive/2026-09-27.md)
- 📅 [2026-09-26](archive/2026-09-26.md)
- 📅 [2026-09-25](archive/2026-09-25.md)
- 📅 [2026-09-24](archive/2026-09-24.md)
- 📅 [2026-09-22](archive/2026-09-22.md)
- 📅 [2026-09-21](archive/2026-09-21.md)
- 📅 [2026-09-20](archive/2026-09-20.md)
- 📅 [2026-09-19](archive/2026-09-19.md)
- 📅 [2026-09-18](archive/2026-09-18.md)
- 📅 [2026-09-16](archive/2026-09-16.md)
- 📅 [2026-09-15](archive/2026-09-15.md)
- 📅 [2026-09-14](archive/2026-09-14.md)
- 📅 [2026-09-13](archive/2026-09-13.md)

*... and [30 older editions in the archive folder](archive/)*

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
