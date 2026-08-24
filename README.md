# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Everything I own, owned](https://schlarp.com/posts/everything-i-own-owned/) | ⭐ 831 | 💬 242 | [HN Thread](https://news.ycombinator.com/item?id=49413320) |
| **2** | [FDA clears blood test to aid evaluation for Alzheimer's disease](https://medicine.washu.edu/news/fda-clears-blood-test-to-aid-evaluation-for-alzheimers-disease/) | ⭐ 32 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=49415893) |
| **3** | [I were 17, I'd learn how to build LLMs from scratch](https://twitter.com/paulg/status/2091544343589060625) | ⭐ 72 | 💬 149 | [HN Thread](https://news.ycombinator.com/item?id=49412396) |
| **4** | [The Work Number: credit score but for your employment history – by Equifax](https://employees.theworknumber.com) | ⭐ 24 | 💬 29 | [HN Thread](https://news.ycombinator.com/item?id=49416200) |
| **5** | [Anthropic's best AI model struggles to attract users as cheaper tools thrive](https://www.ft.com/content/5ee49718-c258-4f01-aa32-7e5b76ae5245) | ⭐ 482 | 💬 433 | [HN Thread](https://news.ycombinator.com/item?id=49411102) |
| **6** | [How I find problems to solve as a staff engineer](https://lalitm.com/post/find-problems-staff-engineer/) | ⭐ 400 | 💬 127 | [HN Thread](https://news.ycombinator.com/item?id=49411643) |
| **7** | [We are not going anywhere](https://gist.github.com/omeid/a9d6d1e3c25cb3aa577931e60e006f54) | ⭐ 46 | 💬 33 | [HN Thread](https://news.ycombinator.com/item?id=49416366) |
| **8** | [OCR It – pull text out of un-copyable documents for your LLM](https://github.com/thiagotigaz/ocr-it) | ⭐ 18 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49415852) |
| **9** | [Andreessen Horowitz is investing billions into a bleak future](https://www.modelrepublic.org/articles/a16z-portfolio) | ⭐ 86 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=49416055) |
| **10** | [I built a low-latency AI companion that plays Skyrim with me](https://pantel.is/projects/ai-gaming-companion/) | ⭐ 137 | 💬 26 | [HN Thread](https://news.ycombinator.com/item?id=49413561) |

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
