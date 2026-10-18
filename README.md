# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [RepRapMicron](https://github.com/VikOlliver/RepRapMicron/wiki) | ⭐ 38 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=50141076) |
| **2** | [DeepSeek search and fetch – $0.75 per 1000 successful requests](https://api-docs.deepseek.com/guides/search/) | ⭐ 357 | 💬 179 | [HN Thread](https://news.ycombinator.com/item?id=50138531) |
| **3** | [Legal experts warn Meta's new terms still grant broad scraping permissions](https://www.niemanlab.org/2026/10/legal-experts-warn-metas-new-terms-still-grant-broad-scraping-permissions-despite-language-changes/) | ⭐ 89 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=50139692) |
| **4** | [Open MicroManipulator – A sub-micrometer 3D motion control plattform](https://github.com/0x23/MicroManipulatorStepper) | ⭐ 62 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=50140001) |
| **5** | [Parser Combinators](https://t3.at/blog/2026-10-17-parser-combinators/) | ⭐ 102 | 💬 48 | [HN Thread](https://news.ycombinator.com/item?id=50139067) |
| **6** | [How the Elizabeth Holmes documentary “You Can See Everything” is deceiving](https://www.readtheprofile.com/p/elizabeth-holmes-documentary-you-can-see-everything) | ⭐ 227 | 💬 276 | [HN Thread](https://news.ycombinator.com/item?id=50137620) |
| **7** | [Hatching (Heraldry)](https://en.wikipedia.org/wiki/Hatching_(heraldry)) | ⭐ 23 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=50093081) |
| **8** | [Show HN: Sphinx – A hook that quizzes you on your AI's code before shipping](https://sphinx-six-theta.vercel.app/) | ⭐ 188 | 💬 60 | [HN Thread](https://news.ycombinator.com/item?id=50137950) |
| **9** | [Bleached corals thrive within days when touching healthy neighbour](https://www.nature.com/articles/d41586-026-03266-x) | ⭐ 504 | 💬 106 | [HN Thread](https://news.ycombinator.com/item?id=50126253) |
| **10** | [Teal – A statically-typed dialect of Lua](https://teal-language.org/) | ⭐ 82 | 💬 34 | [HN Thread](https://news.ycombinator.com/item?id=50124730) |

---

## 🗄️ News Archive

- 📅 [2026-10-18](archive/2026-10-18.md)
- 📅 [2026-10-17](archive/2026-10-17.md)
- 📅 [2026-10-16](archive/2026-10-16.md)
- 📅 [2026-10-15](archive/2026-10-15.md)
- 📅 [2026-10-14](archive/2026-10-14.md)
- 📅 [2026-10-13](archive/2026-10-13.md)
- 📅 [2026-10-10](archive/2026-10-10.md)
- 📅 [2026-10-09](archive/2026-10-09.md)
- 📅 [2026-10-08](archive/2026-10-08.md)
- 📅 [2026-10-07](archive/2026-10-07.md)
- 📅 [2026-10-05](archive/2026-10-05.md)
- 📅 [2026-10-04](archive/2026-10-04.md)
- 📅 [2026-10-03](archive/2026-10-03.md)
- 📅 [2026-10-02](archive/2026-10-02.md)

*... and [47 older editions in the archive folder](archive/)*

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
