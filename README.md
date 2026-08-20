# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [OpenRouter is joining Stripe](https://openrouter.ai/blog/announcements/openrouter-is-joining-stripe/) | ⭐ 731 | 💬 369 | [HN Thread](https://news.ycombinator.com/item?id=49364559) |
| **2** | [Go 1.27](https://go.dev/blog/go1.27) | ⭐ 514 | 💬 135 | [HN Thread](https://news.ycombinator.com/item?id=49365405) |
| **4** | [A faster way to calculate the day of the week](https://www.benjoffe.com/fast-day-of-week) | ⭐ 51 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49323795) |
| **5** | [Error by AI scribe during medical appointment leaves patient devastated](https://www.abc.net.au/news/2026-08-14/ai-medical-scribe-error-leaves-patient-devastated/107031672) | ⭐ 31 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=49294441) |
| **8** | [Unlocking a locked/deactivated e-waste Cricut Maker](https://sprocketfox.io/xssfox/2026/07/01/cricut-unlock/) | ⭐ 163 | 💬 39 | [HN Thread](https://news.ycombinator.com/item?id=49365841) |
| **9** | [Unsloth Dynamic 3.0 GGUFs](https://unsloth.ai/docs/basics/dynamic-3.0-ggufs) | ⭐ 208 | 💬 80 | [HN Thread](https://news.ycombinator.com/item?id=49365443) |
| **10** | [A joke domain purchase turned in geopolitical warfare](https://sprocketfox.io/xssfox/2026/08/19/sondehub-and-war/) | ⭐ 805 | 💬 126 | [HN Thread](https://news.ycombinator.com/item?id=49360015) |

---

## 🗄️ News Archive

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
