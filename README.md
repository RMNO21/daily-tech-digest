# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Breaking Up with Google Play: Why Conversations Is Now Free](https://gultsch.de/posts/breaking-up-with-google-play/) | ⭐ 454 | 💬 183 | [HN Thread](https://news.ycombinator.com/item?id=49855315) |
| **2** | [PipePipe: NewPipe hard fork implementing SponsorBlock](https://github.com/InfinityLoop1308/PipePipe) | ⭐ 78 | 💬 42 | [HN Thread](https://news.ycombinator.com/item?id=49842764) |
| **3** | [Fifteen years later, the Apple Cards origin story](https://lexontech.org/fifteen-years-later-the-apple-cards-origin-story) | ⭐ 229 | 💬 38 | [HN Thread](https://news.ycombinator.com/item?id=49854693) |
| **4** | [Show HN: A Claude Code skill to analyze your chess games](https://github.com/brumar/chess-postmortem-skills) | ⭐ 26 | 💬 16 | [HN Thread](https://news.ycombinator.com/item?id=49857528) |
| **5** | [The Lost Atomic Update on Loongson CPU](https://jia.je/hardware/2026/09/24/loongson-cpu-erratum-en/) | ⭐ 19 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49827900) |
| **6** | [Modern Object Pascal Introduction for Programmers – Castle Game Engine](https://castle-engine.io/modern_pascal) | ⭐ 68 | 💬 29 | [HN Thread](https://news.ycombinator.com/item?id=49829202) |
| **7** | [Revealing the details of how OpenAI agents hacked Hugging Face](https://swarmtraces.org/) | ⭐ 618 | 💬 398 | [HN Thread](https://news.ycombinator.com/item?id=49849985) |
| **8** | [Reflections on 1,000 Days of Math](https://gmays.com/reflections-on-1000-days-of-math/) | ⭐ 32 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=49816907) |
| **9** | [Automattic has a new board after failed attempt to put CEO on leave](https://techcrunch.com/2026/09/25/automattic-has-a-new-board-after-failed-attempt-to-put-ceo-on-leave/) | ⭐ 43 | 💬 37 | [HN Thread](https://news.ycombinator.com/item?id=49857572) |
| **10** | [Analyzing Frontier Model Progress with My Favourite Game: Prince of Persia](https://blog.priyan.in/2026/09/analyzing-frontier-model-progress-with.html) | ⭐ 22 | 💬 18 | [HN Thread](https://news.ycombinator.com/item?id=49849820) |

---

## 🗄️ News Archive

- 📅 [2026-09-26](archive/2026-09-26.md)
- 📅 [2026-09-25](archive/2026-09-25.md)
- 📅 [2026-09-24](archive/2026-09-24.md)
- 📅 [2026-09-22](archive/2026-09-22.md)
- 📅 [2026-09-21](archive/2026-09-21.md)
- 📅 [2026-09-20](archive/2026-09-20.md)
- 📅 [2026-09-19](archive/2026-09-19.md)
- 📅 [2026-09-18](archive/2026-09-18.md)
- 📅 [2026-09-16](archive/2026-09-16.md)
- 📅 [2026-09-15](archive/2026-09-15.md)
- 📅 [2026-09-14](archive/2026-09-14.md)
- 📅 [2026-09-13](archive/2026-09-13.md)
- 📅 [2026-09-12](archive/2026-09-12.md)
- 📅 [2026-09-11](archive/2026-09-11.md)

*... and [28 older editions in the archive folder](archive/)*

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
python scraper.py --force
```

---

<div align="center">
  <sub>Maintained by <a href="https://github.com/RMNO21">RMNO21</a> • Powered by GitHub Actions & Hacker News API</sub>
</div>
