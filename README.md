# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Serbia just elected the world's brainiest parliament](https://www.science.org/content/article/serbia-just-elected-world-s-brainiest-parliament) | ⭐ 284 | 💬 174 | [HN Thread](https://news.ycombinator.com/item?id=50314654) |
| **2** | [Molly(Signal fork) has not been updated since 3 months and is vulnerable](https://piefed.world/post/1503394) | ⭐ 57 | 💬 15 | [HN Thread](https://news.ycombinator.com/item?id=50314666) |
| **3** | [Switch Lowering in GCC](https://xoranth.net/gcc-switch/) | ⭐ 93 | 💬 16 | [HN Thread](https://news.ycombinator.com/item?id=50314085) |
| **4** | [We Took over ChatGPT Accounts](https://www.parameter.ai/labs/we-found-a-gap-at-openai) | ⭐ 36 | 💬 23 | [HN Thread](https://news.ycombinator.com/item?id=50314699) |
| **5** | [Show HN: Marelleo, an open-source story box I built for my kids using ESP32](https://zebra.rodeo/en/blog/marelleo/) | ⭐ 90 | 💬 27 | [HN Thread](https://news.ycombinator.com/item?id=50260753) |
| **6** | [Digital Minimalism](https://vitalik.eth.limo/general/2026/10/31/digital_minimalism.html) | ⭐ 94 | 💬 62 | [HN Thread](https://news.ycombinator.com/item?id=50313661) |
| **7** | [AI, Lean, and the Future of Formal Verification, with Lean Creator Leo de Moura](https://thedataexchange.media/leo-de-moura-lean-aws/) | ⭐ 67 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=50290652) |
| **8** | [My favourite PowerMac is a Nintendo Wii](https://virtuallyfun.com/2026/10/29/my-favourite-powermac-is-a-nintendo-wii/) | ⭐ 324 | 💬 95 | [HN Thread](https://news.ycombinator.com/item?id=50307190) |
| **9** | [The $6.3B Binance hack was pulled off in just 20 minutes](https://www.wired.com/story/the-dollar63-billion-binance-hack-was-pulled-off-in-just-20-minutes/) | ⭐ 484 | 💬 337 | [HN Thread](https://news.ycombinator.com/item?id=50303172) |
| **10** | [Cloudflare Turnstile solver library (no headless browser required)](https://github.com/chris124567/cfsolve) | ⭐ 240 | 💬 68 | [HN Thread](https://news.ycombinator.com/item?id=50277379) |

---

## 🗄️ News Archive

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
- 📅 [2026-10-17](archive/2026-10-17.md)

*... and [59 older editions in the archive folder](archive/)*

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
