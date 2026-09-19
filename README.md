# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Human brain is two separate organs, Stanford Medicine-led research finds](https://med.stanford.edu/news/all-news/2026/09/two-separate-brains.html) | ⭐ 260 | 💬 107 | [HN Thread](https://news.ycombinator.com/item?id=49763697) |
| **2** | [AI-generated posters don’t have to be horrible](https://john.hartnup.uk/2026/06/07/ai-event-posters.html) | ⭐ 147 | 💬 98 | [HN Thread](https://news.ycombinator.com/item?id=49764791) |
| **3** | [If math is more than proof, we need to better celebrate the rest of it](https://terrytao.wordpress.com/2026/09/18/if-math-is-more-than-proof-we-need-to-better-celebrate-the-rest-of-it/) | ⭐ 115 | 💬 82 | [HN Thread](https://news.ycombinator.com/item?id=49763928) |
| **4** | [GPT-6 Astra Solves a WWI German Radio Cipher](https://www.prinzai.com/p/gpt-6-astra-solves-a-wwi-german-radio) | ⭐ 131 | 💬 64 | [HN Thread](https://news.ycombinator.com/item?id=49763987) |
| **5** | [Android 17 is the first since 3.x to add new APIs without releasing to the AOSP](https://grapheneos.social/@GrapheneOS/117282080803799576) | ⭐ 861 | 💬 433 | [HN Thread](https://news.ycombinator.com/item?id=49758736) |
| **6** | [San Francisco Onion Futures Company](https://onionfutures.com/) | ⭐ 202 | 💬 72 | [HN Thread](https://news.ycombinator.com/item?id=49763296) |
| **7** | [“The Secret Life of Circuits” is here](https://blog.coredump.cx/p/the-secret-life-of-circuits-is-here) | ⭐ 40 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=49720143) |
| **8** | [Apple M6 Pro Achieves the Highest Single-Core CPU Score in Geekbench 7](https://browser.geekbench.com/v7/cpu/389219) | ⭐ 69 | 💬 49 | [HN Thread](https://news.ycombinator.com/item?id=49763883) |
| **9** | [Cloudflare Quick Tunnels](https://try.cloudflare.com/) | ⭐ 714 | 💬 285 | [HN Thread](https://news.ycombinator.com/item?id=49754785) |
| **10** | [SDCC – Small Device C Compiler](https://sdcc.sourceforge.net/) | ⭐ 89 | 💬 18 | [HN Thread](https://news.ycombinator.com/item?id=49762744) |

---

## 🗄️ News Archive

- 📅 [2026-09-19](archive/2026-09-19.md)
- 📅 [2026-09-18](archive/2026-09-18.md)
- 📅 [2026-09-16](archive/2026-09-16.md)
- 📅 [2026-09-15](archive/2026-09-15.md)
- 📅 [2026-09-14](archive/2026-09-14.md)
- 📅 [2026-09-13](archive/2026-09-13.md)
- 📅 [2026-09-12](archive/2026-09-12.md)
- 📅 [2026-09-11](archive/2026-09-11.md)
- 📅 [2026-09-10](archive/2026-09-10.md)
- 📅 [2026-09-09](archive/2026-09-09.md)
- 📅 [2026-09-08](archive/2026-09-08.md)
- 📅 [2026-09-07](archive/2026-09-07.md)
- 📅 [2026-09-06](archive/2026-09-06.md)
- 📅 [2026-09-05](archive/2026-09-05.md)

*... and [22 older editions in the archive folder](archive/)*

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
