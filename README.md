# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Postgres 19 is late because so many more bugs are being found now](http://rhaas.blogspot.com/2026/10/postgres-19-is-late-and-its-ais-fault.html) | ⭐ 721 | 💬 434 | [HN Thread](https://news.ycombinator.com/item?id=50312408) |
| **2** | [Show HN: I've updated my Linux System Call website and API](https://syscall.sh/) | ⭐ 145 | 💬 42 | [HN Thread](https://news.ycombinator.com/item?id=50334704) |
| **3** | [WTF Ubuntu?](https://chalmovsky.com/posts/wtf-ubuntu) | ⭐ 514 | 💬 232 | [HN Thread](https://news.ycombinator.com/item?id=50337608) |
| **4** | [If you love a website, back it up](https://blog.mistys-internet.website/post/2026/10/29/if-you-love-a-website-back-it-up/) | ⭐ 17 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=50336518) |
| **5** | [LongCat-2.5: Native Multimodality for Agentic Tasks](https://longcat.ai/blog/longcat-2.5/) | ⭐ 13 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=50337716) |
| **6** | [Bones may release proteins that slow aging and extend life span](https://www.science.org/content/article/bones-may-release-proteins-slow-aging-and-extend-life-span) | ⭐ 240 | 💬 87 | [HN Thread](https://news.ycombinator.com/item?id=50331957) |
| **7** | [Show HN: Aulico, my free tradingview alternative](https://www.aulico.com) | ⭐ 5 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=50337410) |
| **8** | [Ask HN: Which TV do you recommend for privacy?](https://news.ycombinator.com/item?id=50328896) | ⭐ 594 | 💬 700 | [HN Thread](https://news.ycombinator.com/item?id=50328896) |
| **9** | [Anthropic reports $17B in Q3 revenue, commitments of $895B in revised S-1](https://www.cnbc.com/2026/11/02/anthropic-ant-s-1-quarter-financials.html) | ⭐ 117 | 💬 95 | [HN Thread](https://news.ycombinator.com/item?id=50337439) |
| **10** | [Napping characteristics and incident dementia](https://academic.oup.com/biomedgerontology/article/81/10/glag208/8769491?login=false) | ⭐ 17 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=50337635) |

---

## 🗄️ News Archive

- 📅 [2026-11-02](archive/2026-11-02.md)
- 📅 [2026-10-31](archive/2026-10-31.md)
- 📅 [2026-10-30](archive/2026-10-30.md)
- 📅 [2026-10-28](archive/2026-10-28.md)
- 📅 [2026-10-27](archive/2026-10-27.md)
- 📅 [2026-10-26](archive/2026-10-26.md)
- 📅 [2026-10-25](archive/2026-10-25.md)
- 📅 [2026-10-24](archive/2026-10-24.md)
- 📅 [2026-10-23](archive/2026-10-23.md)
- 📅 [2026-10-22](archive/2026-10-22.md)
- 📅 [2026-10-21](archive/2026-10-21.md)
- 📅 [2026-10-20](archive/2026-10-20.md)
- 📅 [2026-10-19](archive/2026-10-19.md)
- 📅 [2026-10-18](archive/2026-10-18.md)

*... and [60 older editions in the archive folder](archive/)*

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
