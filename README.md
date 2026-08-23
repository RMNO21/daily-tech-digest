# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Figmimic – A bookmarklet to copy any webpage into Figma as editable layers](https://marcua.net/minitools/figmimic/) | ⭐ 13 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49402213) |
| **2** | [NanoGPT Speedrun Frontier](https://www.primeintellect.ai/research/nanogpt-speedrun) | ⭐ 44 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=49404380) |
| **3** | [Scrap (2006)](https://twitter.com/moxie/status/2091218652133732491) | ⭐ 313 | 💬 175 | [HN Thread](https://news.ycombinator.com/item?id=49402189) |
| **4** | [Why your local LLM feels dumber than it is](https://forum.level1techs.com/t/why-your-local-llm-feels-dumber-than-it-is/253917) | ⭐ 176 | 💬 58 | [HN Thread](https://news.ycombinator.com/item?id=49402232) |
| **5** | [ElevenLabs, TwelveLabs, ThirteenLabs](https://quantumi.sh/public/labs.html) | ⭐ 303 | 💬 101 | [HN Thread](https://news.ycombinator.com/item?id=49400408) |
| **6** | [Hister – A private, full content search index that you control](https://hister.org/) | ⭐ 231 | 💬 66 | [HN Thread](https://news.ycombinator.com/item?id=49351802) |
| **7** | [NetBSD and my life (2005)](https://mail-index.netbsd.org/netbsd-advocacy/2005/09/10/0000.html) | ⭐ 94 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=49402781) |
| **8** | [RF Cafe](https://www.rfcafe.com/) | ⭐ 149 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=49355659) |
| **9** | [typ.ing](https://typ.ing/) | ⭐ 176 | 💬 56 | [HN Thread](https://news.ycombinator.com/item?id=49346854) |
| **10** | [How a Texas student blew the whistle on a rogue AI hacking attempt](https://www.reuters.com/world/how-texas-student-blew-whistle-rogue-ai-hacking-attempt-2026-08-20/) | ⭐ 109 | 💬 41 | [HN Thread](https://news.ycombinator.com/item?id=49387959) |

---

## 🗄️ News Archive

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
