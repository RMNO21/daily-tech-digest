# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [AMD Specific Patches for Llama.cpp](https://devnull.land/amd-specific-llama-cpp) | ⭐ 125 | 💬 38 | [HN Thread](https://news.ycombinator.com/item?id=50657265) |
| **2** | [CTO of 'RansomwareHelp' Indicted for Wire Fraud](https://krebsonsecurity.com/2026/11/cto-of-ransomwarehelp-indicted-for-wire-fraud/) | ⭐ 70 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=50657645) |
| **3** | [Show HN: Three Linux VMs in a browser tab, each running a different browser](https://michidk.github.io/sidebyside/) | ⭐ 75 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=50656036) |
| **4** | [Intel One Mono font (2023)](https://github.com/intel/intel-one-mono) | ⭐ 388 | 💬 220 | [HN Thread](https://news.ycombinator.com/item?id=50653667) |
| **5** | [George Whitesides, 1939-2026](https://www.science.org/content/blog-post/george-whitesides-1939-2026) | ⭐ 12 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=50657936) |
| **6** | [NP_R ≠ PAR_R](https://github.com/samueleverett01/bss-permanent-separations) | ⭐ 109 | 💬 116 | [HN Thread](https://news.ycombinator.com/item?id=50657059) |
| **7** | [Curiosity Is No Solo Act](https://thereader.mitpress.mit.edu/curiosity-is-no-solo-act/) | ⭐ 90 | 💬 22 | [HN Thread](https://news.ycombinator.com/item?id=50636931) |
| **8** | [Tell HN: Happy Thanksgiving](https://news.ycombinator.com/item?id=50655664) | ⭐ 471 | 💬 121 | [HN Thread](https://news.ycombinator.com/item?id=50655664) |
| **9** | [Nextcloud Office Desktop app](https://nextcloud.com/blog/euro-office-comes-to-your-desktop-with-the-nextcloud-office-desktop-app/) | ⭐ 358 | 💬 167 | [HN Thread](https://news.ycombinator.com/item?id=50654289) |
| **10** | [The New York Times warns photographers not to update Photoshop over AI features](https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features) | ⭐ 606 | 💬 488 | [HN Thread](https://news.ycombinator.com/item?id=50647673) |

---

## 🗄️ News Archive

- 📅 [2026-11-26](archive/2026-11-26.md)
- 📅 [2026-11-23](archive/2026-11-23.md)
- 📅 [2026-11-22](archive/2026-11-22.md)
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

*... and [79 older editions in the archive folder](archive/)*

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
