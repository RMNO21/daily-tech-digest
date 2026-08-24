# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Xiaomi: New CPU matches Apple cores single threaded, much faster multithreaded](https://twitter.com/lemire/status/2091894299289874926) | ⭐ 555 | 💬 373 | [HN Thread](https://news.ycombinator.com/item?id=49420873) |
| **2** | [MS Paint and Photos inivisibly watermark even locally generated output with GUID](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) | ⭐ 389 | 💬 154 | [HN Thread](https://news.ycombinator.com/item?id=49421158) |
| **3** | [The entire city of San Francisco as a video game](https://sf.thijs.gg/) | ⭐ 188 | 💬 62 | [HN Thread](https://news.ycombinator.com/item?id=49422784) |
| **4** | [IPFS Maintainers Winding Down](https://ipshipyard.com/blog/2026-the-end-of-ipfs-at-shipyard/) | ⭐ 256 | 💬 124 | [HN Thread](https://news.ycombinator.com/item?id=49421489) |
| **5** | [A Claude Code skill that recovers export-blocked Kindle highlights](https://github.com/l3a0/claude-plugins) | ⭐ 20 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49424758) |
| **6** | [LLMs could control their host machines by exploiting inference engines](https://boydkane.com/essays/llms-could-control-their-host-machines-by-exploiting-inference-engines) | ⭐ 33 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49424387) |
| **7** | [How Europe is killing makers and micro-entrepreneurs](https://lectronz.com/u/lectronz/articles/how-europe-is-killing-makers-and-micro-entrepreneurs) | ⭐ 852 | 💬 569 | [HN Thread](https://news.ycombinator.com/item?id=49419237) |
| **8** | [Oceans hit highest temperature on record](https://www.bbc.com/news/articles/c62m4gpnp78o) | ⭐ 133 | 💬 45 | [HN Thread](https://news.ycombinator.com/item?id=49424606) |
| **9** | [Jabber/XMPP: 25 Years of Digital Independence](https://gultsch.de/posts/25-years-of-digital-independence/) | ⭐ 95 | 💬 39 | [HN Thread](https://news.ycombinator.com/item?id=49421536) |
| **10** | [Hot Chips 2026: CUDA Targets RISC-V – By Chester Lam](https://chipsandcheese.com/p/hot-chips-2026-cuda-targets-risc) | ⭐ 52 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49422548) |

---

## 🗄️ News Archive

- 📅 [2026-08-24](archive/2026-08-24.md)
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
