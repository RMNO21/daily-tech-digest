# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Qwen 3.8 27B is excellent, but it defaults to overthinking things](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) | ⭐ 197 | 💬 80 | [HN Thread](https://news.ycombinator.com/item?id=49324985) |
| **2** | [The Life and Death of Direct File [pdf]](https://www.ischool.berkeley.edu/sites/default/files/vinton_report_5.pdf) | ⭐ 128 | 💬 51 | [HN Thread](https://news.ycombinator.com/item?id=49325185) |
| **3** | [Gmail might partially be to blame for receiving emails from other Sean Conners](https://boston.conman.org/2026/08/11.1) | ⭐ 17 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=49326229) |
| **4** | [AGI-64 Brings Sierra Adventures to the Commodore 64](https://meanhamster.com/news/agi-64-brings-sierra-adventures-to-the-commodore-64) | ⭐ 33 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49325714) |
| **5** | [A 3rd World Embedded Engineer Responds to "RISC-V They Should Have Known Better"](https://rvembedded.com/blog_post/12/) | ⭐ 414 | 💬 226 | [HN Thread](https://news.ycombinator.com/item?id=49321717) |
| **6** | [Claude: System Prompts](https://platform.claude.com/docs/en/release-notes/system-prompts) | ⭐ 584 | 💬 240 | [HN Thread](https://news.ycombinator.com/item?id=49319556) |
| **7** | [Rhombus 1.1 is now available](https://blog.racket-lang.org/2026/08/rhombus-v1.1.html) | ⭐ 38 | 💬 13 | [HN Thread](https://news.ycombinator.com/item?id=49325384) |
| **8** | [Reticulum – Decentralized Mesh Network](https://reticulum.network/) | ⭐ 43 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49325061) |
| **9** | [Low-Tech Ceramic Water Filter](https://wiki.lowtechlab.org/wiki/Filtre_%C3%A0_eau_c%C3%A9ramique/en) | ⭐ 130 | 💬 33 | [HN Thread](https://news.ycombinator.com/item?id=49259980) |
| **10** | [Interview with Amit Patel, Creator of "Solar Realms Elite"](https://breakintochat.com/blog/2013/02/18/amit-patel-creator-of-solar-realms-elite/) | ⭐ 29 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49231418) |

---

## 🗄️ News Archive

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
