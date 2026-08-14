# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-2026-08-14-blue.svg)](#-todays-highlights-2026-08-14)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest (Git-Scraper)** powered entirely by **GitHub Actions**. Every day, this repository fetches trending technology and artificial intelligence highlights, creates a persistent date-stamped archive, updates the dashboard below, and commits changes directly.

---

## 🚀 Today's Highlights (2026-08-14)

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [GLM-5.3: Frontier coding with emergent cyber capabilities](https://z.ai/blog/glm-5.3) | ⭐ 774 | 💬 392 | [HN Thread](https://news.ycombinator.com/item?id=49294997) |
| **2** | [Don't classify, hallucinate!](https://softwaredoug.com/blog/2026/08/10/hypothetical-classifications) | ⭐ 96 | 💬 50 | [HN Thread](https://news.ycombinator.com/item?id=49249523) |
| **3** | [In Australia, a Home Battery Boom Has Helped Cut Wholesale Power Prices in Half](https://e360.yale.edu/digest/australia-home-batteries) | ⭐ 38 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=49298910) |
| **4** | [DeepSeek peak/off-peak pricing update](https://api-docs.deepseek.com/news/news260813/) | ⭐ 143 | 💬 77 | [HN Thread](https://news.ycombinator.com/item?id=49296627) |
| **5** | [Show HN: Lambdock – Wayland-native GTK4 dock with a live Lisp REPL](https://codeberg.org/jjba23/lambdock) | ⭐ 9 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49260628) |
| **6** | [Gemini 3.7 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) | ⭐ 917 | 💬 463 | [HN Thread](https://news.ycombinator.com/item?id=49289112) |
| **7** | [Differential Heuristics](https://www.redblobgames.com/blog/2026-08-08-differential-heuristics/) | ⭐ 76 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49231490) |
| **8** | [Why does Opus 5 feel worse to work with?](https://mun-logadan.github.io/why-does-opus-5-feel-worse/) | ⭐ 304 | 💬 289 | [HN Thread](https://news.ycombinator.com/item?id=49296740) |
| **9** | [Protect Your Relays](https://www.iroh.computer/blog/authenticated-relays) | ⭐ 30 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=49242867) |
| **10** | [HashAgent – Share an AI agent as a URL, runs locally via WebGPU](https://hashagent.pages.dev/) | ⭐ 7 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49298088) |

---

## 🗄️ Recent Archives

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
│ Markdown Generator            │ Updates archive/2026-08-14.md & README.md
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
