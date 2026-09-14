# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Pion, an agent designed to run any company autonomously](https://andonlabs.com/blog/why-we-built-pion) | ⭐ 237 | 💬 249 | [HN Thread](https://news.ycombinator.com/item?id=49700477) |
| **2** | [Amazon vs. Perplexity – U.S. Court of Appeals for the Ninth Circuit](https://law.justia.com/cases/federal/appellate-courts/ca9/26-1444/26-1444-2026-08-04.html) | ⭐ 138 | 💬 142 | [HN Thread](https://news.ycombinator.com/item?id=49704008) |
| **3** | [Distributed Systems Classics (2017)](https://nvartolomei.com/dist-sys-classics/) | ⭐ 212 | 💬 42 | [HN Thread](https://news.ycombinator.com/item?id=49699158) |
| **4** | [Compressing a Flag to 11 Bits](https://read.vantezzen.io/miniflags) | ⭐ 24 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=49673689) |
| **5** | [OpenAI bots knew about the RubyGems caching vulnerability](https://tenderlovemaking.com/2026/09/11/what-a-time-to-be-alive/) | ⭐ 338 | 💬 289 | [HN Thread](https://news.ycombinator.com/item?id=49695876) |
| **6** | [A Beginning for Mathematics](https://www.daniellitt.com/blog/2026/9/13/a-beginning-for-mathematics/) | ⭐ 151 | 💬 87 | [HN Thread](https://news.ycombinator.com/item?id=49698699) |
| **7** | [Charts built for Chat](https://dbtcharts.com/blog/charts-built-for-chat/) | ⭐ 29 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=49704246) |
| **8** | [Show HN: Macros with a Behringer FCB1010 MIDI Pedalboard in macOS](https://github.com/JamesRyanATX/fcbnerd) | ⭐ 3 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49705442) |
| **9** | [How my e-reader lost its stripes](https://www.serpentine.com/posts/2026/x3-stripes/) | ⭐ 128 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=49699489) |
| **10** | [US coal 'biggest contributor by far' to rise in global emissions](https://www.thechemicalengineer.com/news/us-coal-biggest-contributor-by-far-to-rise-in-global-emissions/) | ⭐ 12 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49704001) |

---

## 🗄️ News Archive

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
- 📅 [2026-09-04](archive/2026-09-04.md)
- 📅 [2026-09-03](archive/2026-09-03.md)
- 📅 [2026-09-02](archive/2026-09-02.md)
- 📅 [2026-09-01](archive/2026-09-01.md)

*... and [18 older editions in the archive folder](archive/)*

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
