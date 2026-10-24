# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Show HN: Steal My Bitcoin](https://stealmybitcoin.com/) | ⭐ 320 | 💬 160 | [HN Thread](https://news.ycombinator.com/item?id=50224916) |
| **2** | [We should be more ambitious with the software we build](https://danluu.com/ambitious/) | ⭐ 30 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=50225695) |
| **3** | [The Goose Programming Language](https://aardappel.github.io/goose/) | ⭐ 166 | 💬 129 | [HN Thread](https://news.ycombinator.com/item?id=50224100) |
| **4** | [Listen and read USA nuclear forces Emergency Action Messages, heard on 11175 kHz](https://missileer.watch) | ⭐ 89 | 💬 56 | [HN Thread](https://news.ycombinator.com/item?id=50224422) |
| **5** | [Roku developer repositories moved from GitHub to GitLab](https://blog.roku.com/developer/gitlab-move) | ⭐ 232 | 💬 155 | [HN Thread](https://news.ycombinator.com/item?id=50222622) |
| **6** | [Free Software Is a Failure](http://www.paritybit.ca/blog/free-software-is-an-abject-failure/) | ⭐ 5 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50226261) |
| **7** | [SpeedCrunch 1.1](https://www.speedcrunch.org/) | ⭐ 42 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=50224210) |
| **8** | [Small Programs and Languages](https://ratfactor.com/cards/pl-small) | ⭐ 9 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50225674) |
| **9** | [The St. Helena 5 pence coin shows Jonathan, a roughly 190 year old tortoise](https://de.numista.com/9866) | ⭐ 82 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=50222927) |
| **10** | [Full Disk Encryption on Fedora with TPM2](https://www.apalrd.net/posts/2026/ent_luks/) | ⭐ 18 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=50194602) |

---

## 🗄️ News Archive

- 📅 [2026-10-24](archive/2026-10-24.md)
- 📅 [2026-10-23](archive/2026-10-23.md)
- 📅 [2026-10-22](archive/2026-10-22.md)
- 📅 [2026-10-21](archive/2026-10-21.md)
- 📅 [2026-10-20](archive/2026-10-20.md)
- 📅 [2026-10-19](archive/2026-10-19.md)
- 📅 [2026-10-18](archive/2026-10-18.md)
- 📅 [2026-10-17](archive/2026-10-17.md)
- 📅 [2026-10-16](archive/2026-10-16.md)
- 📅 [2026-10-15](archive/2026-10-15.md)
- 📅 [2026-10-14](archive/2026-10-14.md)
- 📅 [2026-10-13](archive/2026-10-13.md)
- 📅 [2026-10-10](archive/2026-10-10.md)
- 📅 [2026-10-09](archive/2026-10-09.md)

*... and [53 older editions in the archive folder](archive/)*

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
