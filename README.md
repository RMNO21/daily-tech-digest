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
| **1** | [Qwen 3.8 27B](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) | ⭐ 1040 | 💬 661 | [HN Thread](https://news.ycombinator.com/item?id=49299605) |
| **2** | [The other Sean Byrne doesn't exist](https://conic.al/writing/the-other-sean-byrne-doesnt-exist/) | ⭐ 40 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49307592) |
| **3** | [Coin-sized device can hack a Boeing 737](https://www.wired.com/story/this-coin-sized-device-can-hack-a-boeing-737/) | ⭐ 33 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49282951) |
| **4** | [Going Dark, and the era of law enforcement hacking](https://blog.cryptographyengineering.com/2026/08/14/everything-is-about-to-go-dark/) | ⭐ 293 | 💬 139 | [HN Thread](https://news.ycombinator.com/item?id=49304447) |
| **5** | [Magnitude 7.7 Earthquake – 68 km NNW of Ende, Indonesia](https://earthquake.usgs.gov/earthquakes/eventpage/us6000tkt2/executive) | ⭐ 170 | 💬 35 | [HN Thread](https://news.ycombinator.com/item?id=49306577) |
| **6** | [The Ploopy A+ Trackball Is Here](https://blog.ploopy.co/the-aplus-is-finally-here-499) | ⭐ 89 | 💬 39 | [HN Thread](https://news.ycombinator.com/item?id=49306443) |
| **7** | ["That's not SoC 2 compliant"](https://ampcode.com/notes/thats-not-soc-2-compliant) | ⭐ 7 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49308073) |
| **8** | [Ask HN: How do you keep up with HN these days?](https://news.ycombinator.com/item?id=49308059) | ⭐ 12 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=49308059) |
| **9** | [Google is making private AI practical with homomorphic encryption](https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/) | ⭐ 349 | 💬 205 | [HN Thread](https://news.ycombinator.com/item?id=49300314) |
| **10** | [eigendrum](https://eigendrum.com/#p=circle) | ⭐ 108 | 💬 23 | [HN Thread](https://news.ycombinator.com/item?id=49305250) |

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
