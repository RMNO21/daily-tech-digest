# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [iCloud+ Hide My Email addresses will remain on icloud.com](https://developer.apple.com/news/?id=1ptvdtcm) | ⭐ 210 | 💬 46 | [HN Thread](https://news.ycombinator.com/item?id=49426564) |
| **2** | [Xiaomi: New CPU matches Apple cores single threaded, much faster multithreaded](https://twitter.com/lemire/status/2091894299289874926) | ⭐ 722 | 💬 487 | [HN Thread](https://news.ycombinator.com/item?id=49420873) |
| **3** | [MS Paint and Photos inivisibly watermark even locally generated output with GUID](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) | ⭐ 557 | 💬 224 | [HN Thread](https://news.ycombinator.com/item?id=49421158) |
| **4** | [Moon (2024)](https://ciechanow.ski/moon/) | ⭐ 94 | 💬 15 | [HN Thread](https://news.ycombinator.com/item?id=49426466) |
| **5** | [The entire city of San Francisco as a video game](https://sf.thijs.gg/) | ⭐ 337 | 💬 118 | [HN Thread](https://news.ycombinator.com/item?id=49422784) |
| **6** | [How Europe is killing makers and micro-entrepreneurs](https://lectronz.com/u/lectronz/articles/how-europe-is-killing-makers-and-micro-entrepreneurs) | ⭐ 1051 | 💬 654 | [HN Thread](https://news.ycombinator.com/item?id=49419237) |
| **7** | [Bookshelf – Self-hosted eBook library that runs on object storage](https://github.com/murerkinn/bookshelf) | ⭐ 32 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=49427001) |
| **8** | [One corner of China’s internet is insisting that the Tang Dynasty never existed](https://www.cnn.com/2026/08/19/style/china-tang-dynasty-never-existed-hoax-intl-hnk) | ⭐ 123 | 💬 98 | [HN Thread](https://news.ycombinator.com/item?id=49425819) |
| **9** | [Where did all the public bathrooms go?](https://daily.jstor.org/where-did-all-the-public-bathrooms-go/) | ⭐ 151 | 💬 301 | [HN Thread](https://news.ycombinator.com/item?id=49422800) |
| **10** | [Jabber/XMPP: 25 Years of Digital Independence](https://gultsch.de/posts/25-years-of-digital-independence/) | ⭐ 167 | 💬 64 | [HN Thread](https://news.ycombinator.com/item?id=49421536) |

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
