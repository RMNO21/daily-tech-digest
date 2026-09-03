# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Grok Outage](https://status.x.ai/) | ⭐ 93 | 💬 65 | [HN Thread](https://news.ycombinator.com/item?id=49551589) |
| **2** | [Audacity 4.0](https://github.com/audacity/audacity/releases/tag/Audacity-4.0.0) | ⭐ 695 | 💬 164 | [HN Thread](https://news.ycombinator.com/item?id=49548395) |
| **3** | [Sony makes bold claim about game ownership](https://aginggamer.net/game-industry/sony-makes-bold-claim-about-game-ownership/) | ⭐ 24 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=49551925) |
| **4** | [ChatGPT Is Throwing 404](https://chatgpt.com/) | ⭐ 322 | 💬 248 | [HN Thread](https://news.ycombinator.com/item?id=49550614) |
| **5** | [Any Human Ever – One life, drawn at random from all who have ever lived](https://anyhumanever.com/) | ⭐ 65 | 💬 37 | [HN Thread](https://news.ycombinator.com/item?id=49550698) |
| **6** | [New York Times and The Athletic workers demand company scrap Kalshi deal](https://newsguild.org/new-york-times-and-the-athletic-workers-demand-company-scrap-kalshi-deal/) | ⭐ 43 | 💬 13 | [HN Thread](https://news.ycombinator.com/item?id=49549919) |
| **7** | [Elevated Errors for Multiple Models](https://status.claude.com/incidents/461yvfrzpwtt) | ⭐ 182 | 💬 145 | [HN Thread](https://news.ycombinator.com/item?id=49549676) |
| **8** | [Pre-Release of Polars 2.0](https://pola.rs/posts/announcing-polars-2/) | ⭐ 313 | 💬 105 | [HN Thread](https://news.ycombinator.com/item?id=49546753) |
| **9** | [The Browser's Main Thread Is Expensive](https://kciter.so/posts/the-expensive-main-thread/en/) | ⭐ 281 | 💬 99 | [HN Thread](https://news.ycombinator.com/item?id=49522137) |
| **10** | [Invisible Companies](https://colossus.com/article/invisible-companies/) | ⭐ 107 | 💬 33 | [HN Thread](https://news.ycombinator.com/item?id=49521264) |

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
