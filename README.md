# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [A Deterministic Subexponential-Time Algorithm for the Discrete Logarithm Problem [pdf]](https://eprint.iacr.org/2026/3020.pdf) | ⭐ 11 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50665968) |
| **2** | [The group chat where your AI talks behind your back](https://construct22.com/) | ⭐ 362 | 💬 162 | [HN Thread](https://news.ycombinator.com/item?id=50663595) |
| **3** | [AI made self-hosting fun again](https://janlukas.blog/posts/ai-self-hosting) | ⭐ 788 | 💬 398 | [HN Thread](https://news.ycombinator.com/item?id=50660180) |
| **4** | [Kamil Khan Mumtaz: Pakistani architect, admired at home, almost invisible abroad](https://worksinprogress.co/issue/the-greatest-architect-youve-never-heard-of-is-in-pakistan/) | ⭐ 399 | 💬 100 | [HN Thread](https://news.ycombinator.com/item?id=50659841) |
| **5** | [YouTube Ad Punisher – Auto-reloads YouTube pages when an ad plays](https://github.com/antonpictures/youtube-punisher) | ⭐ 434 | 💬 501 | [HN Thread](https://news.ycombinator.com/item?id=50657530) |
| **6** | [AMD-specific fork of llama.cpp](https://devnull.land/amd-specific-llama-cpp) | ⭐ 384 | 💬 91 | [HN Thread](https://news.ycombinator.com/item?id=50657265) |
| **7** | [Hard Drive pricing has gotten bad](https://blog.ktz.me/black-friday-hard-drive-prices-are-messed-up/) | ⭐ 397 | 💬 322 | [HN Thread](https://news.ycombinator.com/item?id=50661646) |
| **8** | [CTO of 'RansomwareHelp' indicted for wire fraud](https://krebsonsecurity.com/2026/11/cto-of-ransomwarehelp-indicted-for-wire-fraud/) | ⭐ 284 | 💬 141 | [HN Thread](https://news.ycombinator.com/item?id=50657645) |
| **9** | [Company Culture = Slack Emoji ÷ √Headcount](https://lia.mg/posts/measuring-company-culture-with-slack-emoji/) | ⭐ 416 | 💬 195 | [HN Thread](https://news.ycombinator.com/item?id=50659640) |
| **10** | [European Commission Declares Browser Competition a Digital Markets Act Priority](https://open-web-advocacy.org/es/blog/commission-responds-declares-browser-competition-a-dma-priority/) | ⭐ 92 | 💬 54 | [HN Thread](https://news.ycombinator.com/item?id=50664191) |

---

## 🗄️ News Archive

- 📅 [2026-11-27](archive/2026-11-27.md)
- 📅 [2026-11-26](archive/2026-11-26.md)
- 📅 [2026-11-23](archive/2026-11-23.md)
- 📅 [2026-11-22](archive/2026-11-22.md)
- 📅 [2026-11-21](archive/2026-11-21.md)
- 📅 [2026-11-19](archive/2026-11-19.md)
- 📅 [2026-11-18](archive/2026-11-18.md)
- 📅 [2026-11-17](archive/2026-11-17.md)
- 📅 [2026-11-16](archive/2026-11-16.md)
- 📅 [2026-11-15](archive/2026-11-15.md)
- 📅 [2026-11-14](archive/2026-11-14.md)
- 📅 [2026-11-11](archive/2026-11-11.md)
- 📅 [2026-11-10](archive/2026-11-10.md)
- 📅 [2026-11-09](archive/2026-11-09.md)

*... and [80 older editions in the archive folder](archive/)*

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
