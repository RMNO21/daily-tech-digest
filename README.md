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
| **1** | [Qwen 3.8 27B](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) | ⭐ 878 | 💬 573 | [HN Thread](https://news.ycombinator.com/item?id=49299605) |
| **2** | [Going Dark, and the era of law enforcement hacking](https://blog.cryptographyengineering.com/2026/08/14/everything-is-about-to-go-dark/) | ⭐ 180 | 💬 109 | [HN Thread](https://news.ycombinator.com/item?id=49304447) |
| **3** | [RISC-V: They should have known better](https://dmitry.gr/?r=06.%20Thoughts&proj=12.%20RV) | ⭐ 104 | 💬 54 | [HN Thread](https://news.ycombinator.com/item?id=49305492) |
| **4** | [The case for overhauling American science](https://www.economist.com/by-invitation/2026/08/13/the-case-for-overhauling-american-science) | ⭐ 26 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49305708) |
| **5** | [Why does Opus 5 feel worse to work with?](https://mun-logadan.github.io/why-does-opus-5-feel-worse/) | ⭐ 773 | 💬 708 | [HN Thread](https://news.ycombinator.com/item?id=49296740) |
| **6** | [Google is making private AI practical with homomorphic encryption](https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/) | ⭐ 271 | 💬 165 | [HN Thread](https://news.ycombinator.com/item?id=49300314) |
| **7** | [Stop sending me huge PRs; a rant](https://getsmall.xyz/post/cmstjfl9l000if70ljmpzr4va) | ⭐ 47 | 💬 27 | [HN Thread](https://news.ycombinator.com/item?id=49305558) |
| **8** | [RustDesk now supports true unattended remote access on Wayland](https://rustdesk.com/blog/unattended-remote-access-wayland/) | ⭐ 216 | 💬 94 | [HN Thread](https://news.ycombinator.com/item?id=49300759) |
| **9** | [Super Mario Derivations](https://fzakaria.com/2026/08/05/super-mario-derivations) | ⭐ 43 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=49215682) |
| **10** | [Jane Street suffers $15B hit after meltdown at Situational Awareness](https://www.ft.com/content/47dd5308-dd17-404a-a615-61046defd697) | ⭐ 64 | 💬 19 | [HN Thread](https://news.ycombinator.com/item?id=49305927) |

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
