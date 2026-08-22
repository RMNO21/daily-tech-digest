# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [A Kantian Critique of "Sorry" by Justin Bieber](https://decodingvibes.com/blog/a-kantian-critique-of-sorry-by-justin-bieber/) | ⭐ 131 | 💬 48 | [HN Thread](https://news.ycombinator.com/item?id=49399524) |
| **2** | [ElevenLabs, TwelveLabs, ThirteenLabs](https://quantumi.sh/public/labs.html) | ⭐ 56 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=49400408) |
| **3** | [A Friendly Introduction to Racket](https://geometridae.bearblog.dev/a-friendly-introduction-to-racket/) | ⭐ 34 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49399898) |
| **4** | [The New MCP Roadmap](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/) | ⭐ 85 | 💬 65 | [HN Thread](https://news.ycombinator.com/item?id=49399591) |
| **5** | [Munder Difflin – Agent harness to run an office of your clones](https://munderdiffl.in/) | ⭐ 173 | 💬 70 | [HN Thread](https://news.ycombinator.com/item?id=49398152) |
| **6** | [Z80 – The 1970s Microprocessor Still Alive (2021)](https://www.computer.org/csdl/magazine/mi/2021/06/09623402/1yJTvlRLmhi) | ⭐ 78 | 💬 35 | [HN Thread](https://news.ycombinator.com/item?id=49398158) |
| **7** | [Show HN: Rotation via Double Reflection](https://static.laszlokorte.de/rotor-reflect/) | ⭐ 23 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49391168) |
| **8** | [Rust Glancer: Rust LSP using 100x less RAM](https://rust-glancer.github.io/blog/hello-world/) | ⭐ 351 | 💬 70 | [HN Thread](https://news.ycombinator.com/item?id=49393052) |
| **9** | [Hook, hold, harvest and hide: Meta's alleged strategy laid out in first week](https://www.theguardian.com/technology/2026/aug/22/meta-trial-children-privacy) | ⭐ 144 | 💬 92 | [HN Thread](https://news.ycombinator.com/item?id=49398904) |
| **10** | [Felony Bench](https://www.felonybench.com/) | ⭐ 791 | 💬 311 | [HN Thread](https://news.ycombinator.com/item?id=49389430) |

---

## 🗄️ News Archive

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
