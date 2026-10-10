# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [REA Reverse – Engineer Anything](https://rea.tools/) | ⭐ 313 | 💬 103 | [HN Thread](https://news.ycombinator.com/item?id=50028275) |
| **2** | [Telegram Desktop vulnerability allowed any user's file to be stolen](https://beaksec.github.io/posts/telegram-desktop-one-click-account-takeover/) | ⭐ 87 | 💬 36 | [HN Thread](https://news.ycombinator.com/item?id=50029123) |
| **3** | [Cloudflare acquires Deno](https://deno.com/blog/cloudflare) | ⭐ 1167 | 💬 602 | [HN Thread](https://news.ycombinator.com/item?id=50019911) |
| **4** | [Triple-A Minesweeper](https://minesweeper.mikelacher.com/) | ⭐ 869 | 💬 169 | [HN Thread](https://news.ycombinator.com/item?id=50022292) |
| **5** | [Eye of Sauron: Long-Range Hidden Spy Camera Detection](https://www.usenix.org/conference/usenixsecurity24/presentation/zhang-qibo) | ⭐ 108 | 💬 22 | [HN Thread](https://news.ycombinator.com/item?id=49997481) |
| **6** | [How to head into VR without wearing a headset](https://www.kyushu-u.ac.jp/en/researches/view/414/) | ⭐ 16 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49981264) |
| **7** | [Typesafe AI raises $870M at $7.5B](https://typesafe.ai/blog/series-ai) | ⭐ 341 | 💬 246 | [HN Thread](https://news.ycombinator.com/item?id=50023450) |
| **8** | [Show HN: Carrier-Explode: iPhone, Pixel and Galaxy carrier settings decoded](https://carrierexplode.com/) | ⭐ 286 | 💬 39 | [HN Thread](https://news.ycombinator.com/item?id=50024499) |
| **9** | [Can you use autoregressive diffusion to generate market data?](https://blog.janestreet.com/can-you-use-autoregressive-diffusion-to-generate-market-data/) | ⭐ 63 | 💬 23 | [HN Thread](https://news.ycombinator.com/item?id=50021410) |
| **10** | [Compiling Rust to readable C with Eurydice](https://lwn.net/Articles/1055211/) | ⭐ 60 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=50027853) |

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
