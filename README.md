# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [“I just chose words carefully”](https://unsung.aresluna.org/i-just-chose-words-carefully/) | ⭐ 446 | 💬 109 | [HN Thread](https://news.ycombinator.com/item?id=49503601) |
| **2** | [Creepy Crawlies](https://people.kernel.org/monsieuricon/creepy-crawlies) | ⭐ 991 | 💬 489 | [HN Thread](https://news.ycombinator.com/item?id=49491791) |
| **3** | [P99 0 ms* autocomplete for 240M domain names](https://ruurtjan.com/articles/p99-0ms-autocomplete-for-240-million-domain-names) | ⭐ 16 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=49505219) |
| **4** | [The EU has begun enforcing the AI Act: first RFIs to model providers](https://tokenstead.ai/guides/eu-ai-act-first-enforcement-security-rfis) | ⭐ 15 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49505351) |
| **5** | [It takes 5 cloud services to hear my doorbell](https://blog.vghaisas.com/rube-goldberg-doorbell/) | ⭐ 52 | 💬 38 | [HN Thread](https://news.ycombinator.com/item?id=49480091) |
| **6** | [Understanding ChatGPT Work](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/) | ⭐ 95 | 💬 31 | [HN Thread](https://news.ycombinator.com/item?id=49504625) |
| **7** | [Matrox: Graphics for Professionals](https://www.abortretry.fail/p/matrox) | ⭐ 55 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49503934) |
| **8** | [Haiku R1/beta6 has been released](https://www.haiku-os.org/news/2026-08-26_haiku_r1_beta6) | ⭐ 272 | 💬 83 | [HN Thread](https://news.ycombinator.com/item?id=49499867) |
| **9** | [UC Berkeley indefinitely suspends international student work authorizations](https://www.dailycal.org/news/campus/after-second-ice-threat-uc-berkeley-indefinitely-suspends-international-student-work-authorizations/article_0e9ae0c0-dd4d-4455-a25b-e8be7b47e350.html) | ⭐ 46 | 💬 33 | [HN Thread](https://news.ycombinator.com/item?id=49505288) |
| **10** | [CobaltC – The Successor to C?](https://strawberry9.github.io/the-wrong-memory/Appendix_06.html) | ⭐ 12 | 💬 16 | [HN Thread](https://news.ycombinator.com/item?id=49504922) |

---

## 🗄️ News Archive

- 📅 [2026-08-31](archive/2026-08-31.md)
- 📅 [2026-08-30](archive/2026-08-30.md)
- 📅 [2026-08-29](archive/2026-08-29.md)
- 📅 [2026-08-28](archive/2026-08-28.md)
- 📅 [2026-08-27](archive/2026-08-27.md)
- 📅 [2026-08-26](archive/2026-08-26.md)
- 📅 [2026-08-25](archive/2026-08-25.md)
- 📅 [2026-08-24](archive/2026-08-24.md)
- 📅 [2026-08-23](archive/2026-08-23.md)
- 📅 [2026-08-22](archive/2026-08-22.md)
- 📅 [2026-08-21](archive/2026-08-21.md)
- 📅 [2026-08-20](archive/2026-08-20.md)
- 📅 [2026-08-19](archive/2026-08-19.md)
- 📅 [2026-08-18](archive/2026-08-18.md)

*... and [4 older editions in the archive folder](archive/)*

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
