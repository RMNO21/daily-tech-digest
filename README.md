# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [The Lost Treasure of Sid Meier's Pirates](https://remapradio.com/articles/the-lost-treasure-of-sid-meiers-pirates/) | ⭐ 42 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=49384896) |
| **2** | [We Rebuilt the Linux MicroVM Stack on Apple Silicon](https://encore.dev/blog/firecracker-apple-silicon) | ⭐ 37 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49384716) |
| **3** | [The August 17 outage](https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/) | ⭐ 495 | 💬 565 | [HN Thread](https://news.ycombinator.com/item?id=49378957) |
| **4** | [I like 'em thick: an apology to my English teachers](https://www.experimental-history.com/p/i-like-em-thick) | ⭐ 717 | 💬 294 | [HN Thread](https://news.ycombinator.com/item?id=49347543) |
| **5** | [HTML Can Do That](https://chrisburnell.com/html-can-do-that/) | ⭐ 778 | 💬 188 | [HN Thread](https://news.ycombinator.com/item?id=49362689) |
| **6** | [Version Control for Everything](https://tyoverby.com/posts/version-control-for-everything-else/) | ⭐ 28 | 💬 16 | [HN Thread](https://news.ycombinator.com/item?id=49336358) |
| **7** | [Malicious Rust crate Arrayref runs a build-time payload](https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/) | ⭐ 486 | 💬 413 | [HN Thread](https://news.ycombinator.com/item?id=49374269) |
| **8** | [The Religious Experience of Philip K. Dick by R. Crumb (1986)](https://philipdick.com/resources/miscellaneous/the-religious-experience-of-philip-k-dick-by-r-crumb-from-weirdo-17/) | ⭐ 29 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49384224) |
| **9** | [Ox Alpha](https://openrouter.ai/stealth/ox-alpha) | ⭐ 132 | 💬 98 | [HN Thread](https://news.ycombinator.com/item?id=49381896) |
| **10** | [I should have loved biology (2020)](https://jsomers.net/i-should-have-loved-biology/) | ⭐ 272 | 💬 104 | [HN Thread](https://news.ycombinator.com/item?id=49377853) |

---

## 🗄️ News Archive

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
