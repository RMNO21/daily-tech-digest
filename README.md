# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Copyright does not protect AI-generated content in EU](https://mathstodon.xyz/@maxpool/117128107757895678) | ⭐ 65 | 💬 64 | [HN Thread](https://news.ycombinator.com/item?id=49382041) |
| **2** | [The August 17 outage, and the work ahead](https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/) | ⭐ 312 | 💬 353 | [HN Thread](https://news.ycombinator.com/item?id=49378957) |
| **3** | [Consumer Rights Wiki](https://consumerrights.wiki/w/Main_Page) | ⭐ 213 | 💬 31 | [HN Thread](https://news.ycombinator.com/item?id=49378243) |
| **4** | [I like 'em thick: an apology to my English teachers](https://www.experimental-history.com/p/i-like-em-thick) | ⭐ 558 | 💬 258 | [HN Thread](https://news.ycombinator.com/item?id=49347543) |
| **5** | [There's no such thing as a small software team anymore](https://jacob.gold/posts/theres-no-such-thing-as-a-small-software-team/) | ⭐ 16 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49382152) |
| **6** | [Aaron Swartz was prosecuted for scraping, while Meta does it without consequence](https://blog.curiousquail.com/im-upset-again-about-a-co-creator-of-rss-being-prosecuted-for-something-meta-is-doing-with-little-consequence/) | ⭐ 952 | 💬 219 | [HN Thread](https://news.ycombinator.com/item?id=49379550) |
| **7** | [AliExpress runs silent WebAudio fingerprinting that breaks Bluetooth multipoint](https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html) | ⭐ 879 | 💬 287 | [HN Thread](https://news.ycombinator.com/item?id=49372583) |
| **8** | [I should have loved biology (2020)](https://jsomers.net/i-should-have-loved-biology/) | ⭐ 198 | 💬 74 | [HN Thread](https://news.ycombinator.com/item?id=49377853) |
| **9** | [HTML Can Do That](https://chrisburnell.com/html-can-do-that/) | ⭐ 572 | 💬 162 | [HN Thread](https://news.ycombinator.com/item?id=49362689) |
| **10** | [Stealth Model](https://openrouter.ai/stealth/ox-alpha) | ⭐ 23 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49381896) |

---

## 🗄️ News Archive

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
