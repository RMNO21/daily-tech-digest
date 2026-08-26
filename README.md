# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [FDA authorizes first wearable device that monitors ketone and blood sugar levels](https://www.fda.gov/news-events/press-announcements/fda-authorizes-first-wearable-device-continuously-monitors-both-ketone-levels-and-blood-sugar) | ⭐ 255 | 💬 145 | [HN Thread](https://news.ycombinator.com/item?id=49439017) |
| **2** | [Apple introduces M6 and M5 Ultra](https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/) | ⭐ 955 | 💬 898 | [HN Thread](https://news.ycombinator.com/item?id=49433292) |
| **3** | [OpenAI Jalapeño: Better than Nvidia Blackwell](https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia) | ⭐ 323 | 💬 222 | [HN Thread](https://news.ycombinator.com/item?id=49434378) |
| **4** | [New Mac Studio with M5 Max and M5 Ultra](https://www.apple.com/newsroom/2026/08/apple-introduces-new-mac-studio-with-m5-max-and-m5-ultra/) | ⭐ 702 | 💬 447 | [HN Thread](https://news.ycombinator.com/item?id=49433316) |
| **5** | [When str.lower() is a security vulnerability in Python – Seth Larson](https://sethmlarson.dev/when-str-lower-is-a-security-vulnerability) | ⭐ 58 | 💬 29 | [HN Thread](https://news.ycombinator.com/item?id=49440410) |
| **6** | [Black hole singularity is a surface not a point](https://arxiv.org/abs/2608.21590) | ⭐ 184 | 💬 125 | [HN Thread](https://news.ycombinator.com/item?id=49437210) |
| **7** | [Maiao: Gerrit-style code review workflow for GitHub, GitLab, Gitea, others](https://github.com/runetes/maiao) | ⭐ 25 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49441666) |
| **8** | [Python's pre-declared constants are kinda weird](https://sebsite.pw/w/20260801-pythonconstants.html) | ⭐ 140 | 💬 110 | [HN Thread](https://news.ycombinator.com/item?id=49441033) |
| **9** | [Show HN: TeXbrain, a LaTeX editor that runs pdfTeX in the browser via WASM](https://github.com/swimmingbrain/texbrain) | ⭐ 46 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=49441375) |
| **10** | [C2PA Cameras Do Not Survive Contact with Reality](https://www.da.vidbuchanan.co.uk/blog/android-c2pa.html) | ⭐ 76 | 💬 35 | [HN Thread](https://news.ycombinator.com/item?id=49439499) |

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
