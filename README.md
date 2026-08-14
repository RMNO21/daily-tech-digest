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
| **1** | [Qwen 3.8 27B](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) | ⭐ 435 | 💬 309 | [HN Thread](https://news.ycombinator.com/item?id=49299605) |
| **2** | [Count Binface receives over a quarter of votes in Clacton by-election](https://www.bbc.com/news/articles/ce97mm3vvemo) | ⭐ 209 | 💬 121 | [HN Thread](https://news.ycombinator.com/item?id=49301260) |
| **3** | [Seven books I keep close because I love them](https://blog.plover.com/2026/08/02/) | ⭐ 183 | 💬 73 | [HN Thread](https://news.ycombinator.com/item?id=49299675) |
| **4** | [RustDesk now supports true unattended remote access on Wayland](https://rustdesk.com/blog/unattended-remote-access-wayland/) | ⭐ 93 | 💬 35 | [HN Thread](https://news.ycombinator.com/item?id=49300759) |
| **5** | [Why does Opus 5 feel worse to work with?](https://mun-logadan.github.io/why-does-opus-5-feel-worse/) | ⭐ 514 | 💬 473 | [HN Thread](https://news.ycombinator.com/item?id=49296740) |
| **6** | [GLM-5.3: Frontier coding with emergent cyber capabilities](https://z.ai/blog/glm-5.3) | ⭐ 946 | 💬 476 | [HN Thread](https://news.ycombinator.com/item?id=49294997) |
| **7** | [Introducing Toast 1](https://www.mixedbread.com/blog/toast-1) | ⭐ 121 | 💬 33 | [HN Thread](https://news.ycombinator.com/item?id=49299746) |
| **8** | [Maximizing the value of your Claude Code sessions](https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions) | ⭐ 55 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=49300800) |
| **9** | [Ultraviolet Bird Photography](https://uvbirds.com/) | ⭐ 46 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=49211375) |
| **10** | [AI by Hand](https://www.byhand.ai/) | ⭐ 67 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49300568) |

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
