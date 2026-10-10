# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [`123456' password used in Danish CPR data breach](https://cphpost.dk/2026-10-10/news/round-up/123456-password-used-in-massive-danish-cpr-data-breach/) | ⭐ 212 | 💬 134 | [HN Thread](https://news.ycombinator.com/item?id=50031269) |
| **2** | [I Would Like the Value of My Home to Rise, While My Property Taxes Fall](https://conversableeconomist.com/2026/09/28/i-would-like-the-value-of-my-home-to-rise-while-my-property-taxes-fall/) | ⭐ 23 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=50032758) |
| **3** | [Talorys – A self-hosted personal AI agent on Cloudflare's free tier](https://github.com/rociiu/talorys) | ⭐ 73 | 💬 32 | [HN Thread](https://news.ycombinator.com/item?id=50031614) |
| **4** | [Lobbying Is Corruption](https://carette.xyz/posts/lobbying_and_corruption/) | ⭐ 87 | 💬 30 | [HN Thread](https://news.ycombinator.com/item?id=50032556) |
| **5** | [REA Reverse – Engineer Anything](https://rea.tools/) | ⭐ 511 | 💬 219 | [HN Thread](https://news.ycombinator.com/item?id=50028275) |
| **6** | [Cloudflare acquires Deno](https://deno.com/blog/cloudflare) | ⭐ 1272 | 💬 654 | [HN Thread](https://news.ycombinator.com/item?id=50019911) |
| **7** | [Telegram Desktop vulnerability allowed any user's file to be stolen](https://beaksec.github.io/posts/telegram-desktop-one-click-account-takeover/) | ⭐ 240 | 💬 127 | [HN Thread](https://news.ycombinator.com/item?id=50029123) |
| **8** | [C for Rust Programmers](https://bd103.dev/blog/2026-10-07-c-for-rust-programmers/) | ⭐ 38 | 💬 16 | [HN Thread](https://news.ycombinator.com/item?id=50005743) |
| **9** | [Triple-A Minesweeper](https://minesweeper.mikelacher.com/) | ⭐ 1111 | 💬 216 | [HN Thread](https://news.ycombinator.com/item?id=50022292) |
| **10** | [Eye of Sauron: Long-Range Hidden Spy Camera Detection (2024)](https://www.usenix.org/conference/usenixsecurity24/presentation/zhang-qibo) | ⭐ 208 | 💬 43 | [HN Thread](https://news.ycombinator.com/item?id=49997481) |

---

## 🗄️ News Archive

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
- 📅 [2026-09-27](archive/2026-09-27.md)
- 📅 [2026-09-26](archive/2026-09-26.md)

*... and [41 older editions in the archive folder](archive/)*

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
