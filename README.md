# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [iCloud+ Hide My Email addresses will remain on icloud.com](https://developer.apple.com/news/?id=1ptvdtcm) | ⭐ 318 | 💬 77 | [HN Thread](https://news.ycombinator.com/item?id=49426564) |
| **2** | [Xiaomi: New CPU matches Apple cores single threaded, much faster multithreaded](https://twitter.com/lemire/status/2091894299289874926) | ⭐ 779 | 💬 527 | [HN Thread](https://news.ycombinator.com/item?id=49420873) |
| **3** | [MS Paint and Photos inivisibly watermark even locally generated output with GUID](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) | ⭐ 616 | 💬 242 | [HN Thread](https://news.ycombinator.com/item?id=49421158) |
| **4** | [Headlong: A Microharness for Persistent Agents](https://www.laude.org/updates/headlong-a-microharness-for-persistent-agents) | ⭐ 11 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49428882) |
| **5** | [How Universities Should Prepare Founders](https://paulgraham.com/prepare.html) | ⭐ 52 | 💬 52 | [HN Thread](https://news.ycombinator.com/item?id=49428121) |
| **6** | [Moon (2024)](https://ciechanow.ski/moon/) | ⭐ 125 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=49426466) |
| **7** | [How Europe is killing makers and micro-entrepreneurs](https://lectronz.com/u/lectronz/articles/how-europe-is-killing-makers-and-micro-entrepreneurs) | ⭐ 1130 | 💬 676 | [HN Thread](https://news.ycombinator.com/item?id=49419237) |
| **8** | [The entire city of San Francisco as a video game](https://sf.thijs.gg/) | ⭐ 394 | 💬 130 | [HN Thread](https://news.ycombinator.com/item?id=49422784) |
| **9** | [Nostr is an inclusive communication commons](https://nostr.org/) | ⭐ 47 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49399722) |
| **10** | [Bookshelf – Self-hosted eBook library that runs on object storage](https://github.com/murerkinn/bookshelf) | ⭐ 60 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=49427001) |

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
