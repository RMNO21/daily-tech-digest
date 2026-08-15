# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-2026-08-15-blue.svg)](#-todays-highlights-2026-08-15)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest (Git-Scraper)** powered entirely by **GitHub Actions**. Every day, this repository fetches trending technology and artificial intelligence highlights, creates a persistent date-stamped archive, updates the dashboard below, and commits changes directly.

---

## 🚀 Today's Highlights (2026-08-15)

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Semaglutide linked to 26% lower 5-year predicted dementia risk](https://alz-journals.onlinelibrary.wiley.com/doi/10.1002/dad2.70432) | ⭐ 132 | 💬 74 | [HN Thread](https://news.ycombinator.com/item?id=49311651) |
| **2** | [AI Isn't Outthinking Mathematicians. It's Out-Remembering Them](https://davidepiffer.com/p/ai-isnt-outthinking-mathematicians) | ⭐ 27 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=49312845) |
| **3** | [The First At-Home Test for Infected Ticks Could Improve Lyme Disease Diagnosis](https://www.smithsonianmag.com/innovation/the-first-at-home-test-for-infected-ticks-could-improve-lyme-disease-diagnosis-180989235/) | ⭐ 119 | 💬 44 | [HN Thread](https://news.ycombinator.com/item?id=49310682) |
| **4** | [Auto-research with codex: How I achieved a 232x Faster Kernel](https://sankalp.bearblog.dev/autoresearch/) | ⭐ 286 | 💬 75 | [HN Thread](https://news.ycombinator.com/item?id=49309549) |
| **5** | [RISC-V: They Should Have Known Better](https://dmitry.gr/?r=06.%20Thoughts&proj=12.%20RV) | ⭐ 87 | 💬 227 | [HN Thread](https://news.ycombinator.com/item?id=49298035) |
| **6** | [A Spectre Is Haunting Unicode](https://www.dampfkraft.com/ghost-characters.html) | ⭐ 50 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=49310926) |
| **7** | [A controversial Alzheimer's surgery is said to reverse symptoms](https://www.nature.com/articles/d41586-026-02448-x) | ⭐ 74 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=49312008) |
| **8** | [Working with AI Feels More Like Leadership Than Coding](https://allen.bargi.org/notes/working-with-ai-feels-like-leadership/) | ⭐ 170 | 💬 122 | [HN Thread](https://news.ycombinator.com/item?id=49309451) |
| **9** | [2D Gaussian Splatting for Bézier Spline Line Art Vectorization](https://studios.disneyresearch.com/2026/07/16/2d-gaussian-splatting-for-bezier-spline-line-art-vectorization/) | ⭐ 28 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49306333) |
| **10** | [Could a computer scientist build a brain?](https://stankerstjens.github.io/could-a-computer-scientist-build-a-brain/) | ⭐ 38 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=49310362) |

---

## 🗄️ Recent Archives

- 📅 [2026-08-15](archive/2026-08-15.md)
- 📅 [2026-08-14](archive/2026-08-14.md)

---

## ⚙️ How It Works

```
┌───────────────────────────────┐
│ GitHub Actions Cron (Every 6h)│ 00:00, 06:00, 12:00, 18:00 UTC
└──────────────┬────────────────┘
               ▼
┌───────────────────────────────┐
│ scraper.py (Hacker News API)  │ Fetches Top Tech & AI Stories
└──────────────┬────────────────┘
               ▼
┌───────────────────────────────┐
│ Markdown Generator            │ Updates archive/2026-08-15.md & README.md
└──────────────┬────────────────┘
               ▼
┌───────────────────────────────┐
│ Git Auto-Commit & Push        │ Signed with RMNO21 identity
└───────────────────────────────┘
```

1. **Scheduled Trigger:** GitHub Actions runs every 6 hours (`00:00`, `06:00`, `12:00`, `18:00` UTC) and supports manual triggering via `workflow_dispatch`.
2. **Data Scraping:** `scraper.py` queries Hacker News API for the highest-ranked stories and discussions.
3. **Archive Generation:** Saves a full snapshot into `archive/YYYY-MM-DD.md`.
4. **Dashboard Update:** Re-renders this `README.md` with live highlights and table of contents.
5. **Auto Commit & Push:** Commits changes using the author's verified credentials, contributing to the GitHub activity graph.

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
  <sub>Maintained automatically by <a href="https://github.com/RMNO21">RMNO21</a> • Powered by GitHub Actions & Hacker News API</sub>
</div>
