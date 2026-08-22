# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [hdiutil is deprecated in macOS 27 Golden Gate](https://lapcatsoftware.com/articles/2026/8/7.html) | ⭐ 70 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=49402741) |
| **2** | [NetBSD and My Life (2005)](https://mail-index.netbsd.org/netbsd-advocacy/2005/09/10/0000.html) | ⭐ 36 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49402781) |
| **3** | [Scrap](https://twitter.com/moxie/status/2091218652133732491) | ⭐ 100 | 💬 23 | [HN Thread](https://news.ycombinator.com/item?id=49402189) |
| **4** | [ElevenLabs, TwelveLabs, ThirteenLabs](https://quantumi.sh/public/labs.html) | ⭐ 232 | 💬 76 | [HN Thread](https://news.ycombinator.com/item?id=49400408) |
| **5** | [Hister – A private, full content search index that you control](https://hister.org/) | ⭐ 111 | 💬 40 | [HN Thread](https://news.ycombinator.com/item?id=49351802) |
| **6** | [A Friendly Introduction to Racket](https://geometridae.bearblog.dev/a-friendly-introduction-to-racket/) | ⭐ 104 | 💬 42 | [HN Thread](https://news.ycombinator.com/item?id=49399898) |
| **7** | [Show HN: Make your logo extra bright on HDR screens](https://www.soverybright.com/) | ⭐ 17 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=49402521) |
| **8** | [typ.ing](https://typ.ing/) | ⭐ 86 | 💬 27 | [HN Thread](https://news.ycombinator.com/item?id=49346854) |
| **9** | [RF Cafe](https://www.rfcafe.com/) | ⭐ 74 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=49355659) |
| **10** | [Why your local LLM feels dumber than it is](https://forum.level1techs.com/t/why-your-local-llm-feels-dumber-than-it-is/253917) | ⭐ 15 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49402232) |

---

## 🗄️ News Archive

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
