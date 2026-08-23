# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [The End of an Athlon](http://www.os2museum.com/wp/the-end-of-an-athlon/) | ⭐ 63 | 💬 13 | [HN Thread](https://news.ycombinator.com/item?id=49406333) |
| **2** | [JIT Compiling Code in 5μs](https://malisper.me/jit-compiling-code-in-5-us/) | ⭐ 44 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49406387) |
| **3** | [To become a better writer, read as much as you can](https://nappertime.com/the-golden-rule-of-becoming-a-better-writer/) | ⭐ 108 | 💬 58 | [HN Thread](https://news.ycombinator.com/item?id=49405870) |
| **4** | [MartyPC is a cross-platform emulator of early PCs written in Rust](https://martypc.net/) | ⭐ 105 | 💬 27 | [HN Thread](https://news.ycombinator.com/item?id=49405816) |
| **5** | [I Dream of Quieter Computing](https://henry.codes/writing/i-dream-of-quieter-computing/) | ⭐ 58 | 💬 34 | [HN Thread](https://news.ycombinator.com/item?id=49405682) |
| **6** | [Why your local LLM feels dumber than it is](https://forum.level1techs.com/t/why-your-local-llm-feels-dumber-than-it-is/253917) | ⭐ 325 | 💬 110 | [HN Thread](https://news.ycombinator.com/item?id=49402232) |
| **7** | [Wi-Fi 8 is the first wireless upgrade in years that isn't chasing speed](https://www.xda-developers.com/wi-fi-8-first-wireless-upgrade-years-isnt-chasing-speed-home-networks-need-it/) | ⭐ 74 | 💬 52 | [HN Thread](https://news.ycombinator.com/item?id=49406539) |
| **8** | [The Art and Beauty of Blade Runner (2015)](https://nappertime.com/the-art-of-and-beauty-of-blade-runner/) | ⭐ 68 | 💬 21 | [HN Thread](https://news.ycombinator.com/item?id=49405331) |
| **9** | [Scrap (2006)](https://twitter.com/moxie/status/2091218652133732491) | ⭐ 367 | 💬 196 | [HN Thread](https://news.ycombinator.com/item?id=49402189) |
| **10** | [ElevenLabs, TwelveLabs, ThirteenLabs](https://quantumi.sh/public/labs.html) | ⭐ 392 | 💬 115 | [HN Thread](https://news.ycombinator.com/item?id=49400408) |

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
