# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [The Life and Death of Direct File [pdf]](https://www.ischool.berkeley.edu/sites/default/files/vinton_report_5.pdf) | ⭐ 35 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49325185) |
| **2** | [A 3rd World Embedded Engineer Responds to "RISC-V They Should Have Known Better"](https://rvembedded.com/blog_post/12/) | ⭐ 370 | 💬 193 | [HN Thread](https://news.ycombinator.com/item?id=49321717) |
| **3** | [Claude: System Prompts](https://platform.claude.com/docs/en/release-notes/system-prompts) | ⭐ 537 | 💬 224 | [HN Thread](https://news.ycombinator.com/item?id=49319556) |
| **4** | [Rhombus 1.1 is now available](https://blog.racket-lang.org/2026/08/rhombus-v1.1.html) | ⭐ 7 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49325384) |
| **5** | [Qwen 3.8 27B is excellent, but it defaults to overthinking things](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) | ⭐ 18 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49324985) |
| **6** | [SIMD in the 90s: Programming Intel's Pentium MMX](https://pikuma.com/blog/programming-intel-pentium-mmx-simd) | ⭐ 70 | 💬 32 | [HN Thread](https://news.ycombinator.com/item?id=49285096) |
| **7** | [Low-Tech Ceramic Water Filter](https://wiki.lowtechlab.org/wiki/Filtre_%C3%A0_eau_c%C3%A9ramique/en) | ⭐ 90 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=49259980) |
| **8** | [Models Are Getting Dumber on Purpose](https://w4g1.dev/blog/models-are-getting-dumber-on-purpose) | ⭐ 264 | 💬 148 | [HN Thread](https://news.ycombinator.com/item?id=49322695) |
| **9** | [The AI Credit Resale Economy](https://vectoral.com/blog/who-are-the-token-brokers) | ⭐ 224 | 💬 88 | [HN Thread](https://news.ycombinator.com/item?id=49320611) |
| **10** | [A quick look at zero-knowledge proofs](https://bernsteinbear.com/blog/zkp/) | ⭐ 43 | 💬 15 | [HN Thread](https://news.ycombinator.com/item?id=49303776) |

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
