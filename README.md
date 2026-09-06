# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Cloud in a Bottle: making self-hosting accessible to everyone](https://cloudinabottle.org/blog/launch-post) | ⭐ 240 | 💬 100 | [HN Thread](https://news.ycombinator.com/item?id=49582000) |
| **2** | [GPT-6 Astra on robot arms](https://openai.robocurve.org/gpt-6-astra/) | ⭐ 98 | 💬 54 | [HN Thread](https://news.ycombinator.com/item?id=49582582) |
| **3** | [The revolt of the reader](https://bcantrill.dtrace.org/2026/09/05/the-revolt-of-the-reader/) | ⭐ 202 | 💬 74 | [HN Thread](https://news.ycombinator.com/item?id=49580939) |
| **4** | [OpenBSD Stories: Strange Medieval Devices](http://miod.online.fr/software/openbsd/stories/smd.html) | ⭐ 19 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49539759) |
| **5** | [Chrome again exempts Google from user site data settings](https://lapcatsoftware.com/articles/2026/9/1.html) | ⭐ 189 | 💬 28 | [HN Thread](https://news.ycombinator.com/item?id=49581870) |
| **6** | [Learn Programming with OCaml](https://usr.lmf.cnrs.fr/lpo/) | ⭐ 205 | 💬 81 | [HN Thread](https://news.ycombinator.com/item?id=49578280) |
| **7** | [Private German rocket makes history, reaches orbit from European soil](https://www.space.com/space-exploration/launches-spacecraft/isar-aerospace-second-launch-norway-andoya-spaceport-spectrum-rocket) | ⭐ 430 | 💬 236 | [HN Thread](https://news.ycombinator.com/item?id=49580369) |
| **8** | [The "$60 Gaming PC" – AMD BC-250 (2025)](https://devquasar.com/hardware/the-60-gaming-pc-amd-bc-250/) | ⭐ 313 | 💬 93 | [HN Thread](https://news.ycombinator.com/item?id=49576386) |
| **9** | [Discovery of a new OpenAI agent message board](https://collusion.wiki/) | ⭐ 2149 | 💬 1528 | [HN Thread](https://news.ycombinator.com/item?id=49563355) |
| **10** | [The ColorChecker, photography's most important 24 squares, turns 50](https://www.dpreview.com/news/the-colorchecker-photographys-most-important-24-squares-turns-50/) | ⭐ 5 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49529398) |

---

## 🗄️ News Archive

- 📅 [2026-09-06](archive/2026-09-06.md)
- 📅 [2026-09-05](archive/2026-09-05.md)
- 📅 [2026-09-04](archive/2026-09-04.md)
- 📅 [2026-09-03](archive/2026-09-03.md)
- 📅 [2026-09-02](archive/2026-09-02.md)
- 📅 [2026-09-01](archive/2026-09-01.md)
- 📅 [2026-08-31](archive/2026-08-31.md)
- 📅 [2026-08-30](archive/2026-08-30.md)
- 📅 [2026-08-29](archive/2026-08-29.md)
- 📅 [2026-08-28](archive/2026-08-28.md)
- 📅 [2026-08-27](archive/2026-08-27.md)
- 📅 [2026-08-26](archive/2026-08-26.md)
- 📅 [2026-08-25](archive/2026-08-25.md)
- 📅 [2026-08-24](archive/2026-08-24.md)

*... and [10 older editions in the archive folder](archive/)*

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
