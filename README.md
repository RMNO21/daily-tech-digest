# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [The Emperor Pelican Has No Clothes](https://arcfu.com/post/the-emperor-pelican-has-no-clothes/) | ⭐ 37 | 💬 18 | [HN Thread](https://news.ycombinator.com/item?id=50090443) |
| **2** | [Iosevka is an open-source, sans-serif and slab-serif monospace font](https://typeof.net/Iosevka/) | ⭐ 535 | 💬 218 | [HN Thread](https://news.ycombinator.com/item?id=50084240) |
| **3** | [Americans' Social Activity Has Steeply Declined in the Past 30 Years](https://www.dataforprogress.org/blog/2026/9/29/americans-social-activity-has-steeply-declined-in-the-past-30-years) | ⭐ 22 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=50089921) |
| **4** | [Submarine cable resilience](https://blog.apnic.net/2026/10/14/submarine-cable-resilience/) | ⭐ 36 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=50089229) |
| **5** | [Amsterdam police confisquates server left-wing ISP A/I at American request](https://www.nrc.nl/nieuws/2026/10/14/politie-amsterdam-neemt-op-amerikaans-verzoek-server-in-beslag-van-italiaanse-internetdienstverlener-a-i-a4938960) | ⭐ 83 | 💬 15 | [HN Thread](https://news.ycombinator.com/item?id=50090084) |
| **6** | [Pg_vectorsearch: An index that is faster than pgvector's IVFFlat and HNSW](https://github.com/timescale/pg_vectorsearch) | ⭐ 138 | 💬 40 | [HN Thread](https://news.ycombinator.com/item?id=50086165) |
| **7** | [Show HN: Graphicle, a Rust port of Graphify with memory for coding agents](https://github.com/graphicle-ai/graphicle) | ⭐ 14 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=50088713) |
| **8** | [Running Windows desktop tests from Linux with disposable VMs](https://www.qawolf.com/blog/how-we-solved-windows-desktop-automation) | ⭐ 44 | 💬 19 | [HN Thread](https://news.ycombinator.com/item?id=50088643) |
| **9** | [Amazon pushes up prices across the Internet](https://www.not-ship.com/how-amazon-pushes-up-prices-all-across-the-internet/) | ⭐ 496 | 💬 455 | [HN Thread](https://news.ycombinator.com/item?id=50084757) |
| **10** | [ASML's strong orders ease fears AI spending boom is running out of steam](https://www.reuters.com/business/asml-forecasts-q4-sales-above-expectations-ai-chip-demand-2026-10-14/) | ⭐ 122 | 💬 112 | [HN Thread](https://news.ycombinator.com/item?id=50088430) |

---

## 🗄️ News Archive

- 📅 [2026-10-14](archive/2026-10-14.md)
- 📅 [2026-10-13](archive/2026-10-13.md)
- 📅 [2026-10-10](archive/2026-10-10.md)
- 📅 [2026-10-09](archive/2026-10-09.md)
- 📅 [2026-10-08](archive/2026-10-08.md)
- 📅 [2026-10-07](archive/2026-10-07.md)
- 📅 [2026-10-05](archive/2026-10-05.md)
- 📅 [2026-10-04](archive/2026-10-04.md)
- 📅 [2026-10-03](archive/2026-10-03.md)
- 📅 [2026-10-02](archive/2026-10-02.md)
- 📅 [2026-10-01](archive/2026-10-01.md)
- 📅 [2026-09-30](archive/2026-09-30.md)
- 📅 [2026-09-29](archive/2026-09-29.md)
- 📅 [2026-09-28](archive/2026-09-28.md)

*... and [43 older editions in the archive folder](archive/)*

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
