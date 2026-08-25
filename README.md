# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Don't Wordle](https://dontwordle.com/) | ⭐ 52 | 💬 16 | [HN Thread](https://news.ycombinator.com/item?id=49432319) |
| **2** | [France's tax agency got hacked (in French)](https://www.cybernetica.fr/piratage-des-impots-comment-en-est-on-arrive-la/) | ⭐ 4 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49433064) |
| **3** | [HelloAssembly The smallest possible complete Windows application](https://github.com/PlummersSoftwareLLC/HelloAssembly) | ⭐ 13 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49432227) |
| **4** | [iCloud+ Hide My Email addresses will remain on icloud.com](https://developer.apple.com/news/?id=1ptvdtcm) | ⭐ 512 | 💬 155 | [HN Thread](https://news.ycombinator.com/item?id=49426564) |
| **5** | [MS Paint and Photos inivisibly watermark even locally generated output with GUID](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) | ⭐ 758 | 💬 368 | [HN Thread](https://news.ycombinator.com/item?id=49421158) |
| **6** | [Xiaomi: New CPU matches Apple cores single threaded, much faster multithreaded](https://twitter.com/lemire/status/2091894299289874926) | ⭐ 916 | 💬 654 | [HN Thread](https://news.ycombinator.com/item?id=49420873) |
| **7** | [How Universities Should Prepare Founders](https://paulgraham.com/prepare.html) | ⭐ 165 | 💬 195 | [HN Thread](https://news.ycombinator.com/item?id=49428121) |
| **8** | [SiFive's First Server Platform](https://chipsandcheese.com/p/sifives-first-server-platform) | ⭐ 78 | 💬 21 | [HN Thread](https://news.ycombinator.com/item?id=49428638) |
| **9** | [How Europe is killing makers and micro-entrepreneurs](https://lectronz.com/u/lectronz/articles/how-europe-is-killing-makers-and-micro-entrepreneurs) | ⭐ 1464 | 💬 919 | [HN Thread](https://news.ycombinator.com/item?id=49419237) |
| **10** | [The entire city of San Francisco as a video game](https://sf.thijs.gg/) | ⭐ 516 | 💬 150 | [HN Thread](https://news.ycombinator.com/item?id=49422784) |

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
