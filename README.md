# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Hurried Announcement: Alessandro Masullo GRH](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/) | ⭐ 2122 | 💬 980 | [HN Thread](https://news.ycombinator.com/item?id=50579568) |
| **2** | [Levent Alpöge claims proof of the Generalized Riemann Hypothesis [pdf]](https://alpo.ge/remark.pdf) | ⭐ 2665 | 💬 1844 | [HN Thread](https://news.ycombinator.com/item?id=50574968) |
| **3** | [Inkling 2 Mini](https://thinkingmachines.ai/news/inkling-2-mini/) | ⭐ 1036 | 💬 194 | [HN Thread](https://news.ycombinator.com/item?id=50581260) |
| **4** | [ClawDOS – An AI coding agent for DOS](http://ricapar.net/ClawDOS/) | ⭐ 74 | 💬 21 | [HN Thread](https://news.ycombinator.com/item?id=50586292) |
| **5** | [Surprisingly Adorable Insect Portraits](https://amateurphotographer.com/latest/these-astonishing-insect-portraits-reveal-a-hidden-world-you-never-knew-existed/) | ⭐ 54 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=50586648) |
| **6** | [We promoted developers into architects without informing them](https://manidoraisamy.com/developer-to-architect.html) | ⭐ 445 | 💬 247 | [HN Thread](https://news.ycombinator.com/item?id=50579331) |
| **7** | [NINLIVE: The Nine Inch Nails live archive](https://ninlive.com/) | ⭐ 269 | 💬 70 | [HN Thread](https://news.ycombinator.com/item?id=50583274) |
| **8** | [Clojure will affect the way you think about programming (2017)](https://eli.thegreenplace.net/2017/clojure-the-perfect-language-to-expand-your-brain/) | ⭐ 106 | 💬 32 | [HN Thread](https://news.ycombinator.com/item?id=50585376) |
| **9** | [Unforced Navier-Stokes Singularity and the Generalized Riemann Hypothesis](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/) | ⭐ 454 | 💬 187 | [HN Thread](https://news.ycombinator.com/item?id=50578358) |
| **10** | [RCE in Gnupg](https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html) | ⭐ 22 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=50587208) |

---

## 🗄️ News Archive

- 📅 [2026-11-21](archive/2026-11-21.md)
- 📅 [2026-11-19](archive/2026-11-19.md)
- 📅 [2026-11-18](archive/2026-11-18.md)
- 📅 [2026-11-17](archive/2026-11-17.md)
- 📅 [2026-11-16](archive/2026-11-16.md)
- 📅 [2026-11-15](archive/2026-11-15.md)
- 📅 [2026-11-14](archive/2026-11-14.md)
- 📅 [2026-11-11](archive/2026-11-11.md)
- 📅 [2026-11-10](archive/2026-11-10.md)
- 📅 [2026-11-09](archive/2026-11-09.md)
- 📅 [2026-11-08](archive/2026-11-08.md)
- 📅 [2026-11-07](archive/2026-11-07.md)
- 📅 [2026-11-06](archive/2026-11-06.md)
- 📅 [2026-11-05](archive/2026-11-05.md)

*... and [76 older editions in the archive folder](archive/)*

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
