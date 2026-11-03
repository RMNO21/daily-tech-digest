# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [I Dumped Apple's Fucking Word List](https://helgesver.re/articles/macos-vulgar-word-flags) | ⭐ 58 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=50357782) |
| **2** | [Preparing for the Flipper One Kickstarter and opening pre-orders](https://flipper.net/pages/flipper-one) | ⭐ 98 | 💬 44 | [HN Thread](https://news.ycombinator.com/item?id=50356994) |
| **3** | [Jailbreaking my car's navigation system just so I can change the time](https://blog.nns.ee/2026/11/02/renault-hack/) | ⭐ 438 | 💬 172 | [HN Thread](https://news.ycombinator.com/item?id=50339288) |
| **4** | [Qwen 3.8 27B on my laptop can interpret model weights, too](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/) | ⭐ 341 | 💬 110 | [HN Thread](https://news.ycombinator.com/item?id=50355251) |
| **5** | [Stringman, an $800 open-source room scale gripper robot](https://neufangled.com/) | ⭐ 163 | 💬 80 | [HN Thread](https://news.ycombinator.com/item?id=50354358) |
| **6** | [Postman silently auto-installs AI plugins and attempts to share all API data](https://github.com/postmanlabs/postman-app-support/issues/14370) | ⭐ 753 | 💬 252 | [HN Thread](https://news.ycombinator.com/item?id=50354960) |
| **7** | [Fujifilm to boost tape production 5x as AI fuels archiving demand](https://arstechnica.com/gadgets/2026/10/fujifilm-to-boost-tape-production-5x-as-ai-fuels-archiving-demand/) | ⭐ 309 | 💬 125 | [HN Thread](https://news.ycombinator.com/item?id=50336918) |
| **8** | [Introduction to Programming in ATS](https://ats-lang.sourceforge.net/DOCUMENT/INT2PROGINATS/HTML/book1.html) | ⭐ 27 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=50356913) |
| **9** | [Mac at Any Scale](https://namespace.so/blog/mac-at-any-scale) | ⭐ 253 | 💬 135 | [HN Thread](https://news.ycombinator.com/item?id=50352758) |
| **10** | [Show HN: HackerTV – HN's most-recommended Youtube videos as 24/7 TV channels](https://hackertv.org) | ⭐ 20 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=50346755) |

---

## 🗄️ News Archive

- 📅 [2026-11-03](archive/2026-11-03.md)
- 📅 [2026-11-02](archive/2026-11-02.md)
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

*... and [61 older editions in the archive folder](archive/)*

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
