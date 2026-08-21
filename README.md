# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Codex on AWS bedrock bug causing 10x charges](https://github.com/openai/codex/issues/37674) | ⭐ 29 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=49383326) |
| **2** | [The August 17 outage](https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/) | ⭐ 401 | 💬 441 | [HN Thread](https://news.ycombinator.com/item?id=49378957) |
| **3** | [I like 'em thick: an apology to my English teachers](https://www.experimental-history.com/p/i-like-em-thick) | ⭐ 627 | 💬 270 | [HN Thread](https://news.ycombinator.com/item?id=49347543) |
| **4** | [HTML Can Do That](https://chrisburnell.com/html-can-do-that/) | ⭐ 641 | 💬 170 | [HN Thread](https://news.ycombinator.com/item?id=49362689) |
| **5** | [Malicious Rust crate Arrayref runs a build-time payload](https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/) | ⭐ 425 | 💬 377 | [HN Thread](https://news.ycombinator.com/item?id=49374269) |
| **6** | [I should have loved biology (2020)](https://jsomers.net/i-should-have-loved-biology/) | ⭐ 218 | 💬 82 | [HN Thread](https://news.ycombinator.com/item?id=49377853) |
| **7** | [Captain Zilog](https://www.zilog.com/captain_zilog/) | ⭐ 21 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49329919) |
| **8** | [Ox Alpha](https://openrouter.ai/stealth/ox-alpha) | ⭐ 63 | 💬 49 | [HN Thread](https://news.ycombinator.com/item?id=49381896) |
| **9** | [AI companies destroy physical books – let's scan rare books before it's too late](https://annas-archive.gl/blog/physical-destruction.html) | ⭐ 153 | 💬 99 | [HN Thread](https://news.ycombinator.com/item?id=49383026) |
| **10** | [Make a 6-Tesla-class high-temperature superconducting dipole magnet at 4.2 K](https://journals.aps.org/prab/abstract/10.1103/4nhs-bkwh) | ⭐ 20 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49304409) |

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
