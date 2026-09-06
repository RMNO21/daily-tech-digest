# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Isar Aerospace reaches orbit and deploys payloads on second flight](https://isaraerospace.com/press/history-for-european-spaceflight-isar-aerospace-reaches-orbit-and-deploys-payloads-on-second-flight) | ⭐ 69 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49584083) |
| **2** | [Cloud in a Bottle: making self-hosting accessible to everyone](https://cloudinabottle.org/blog/launch-post) | ⭐ 386 | 💬 173 | [HN Thread](https://news.ycombinator.com/item?id=49582000) |
| **3** | [Play GTA Vice City in the Browser](https://quenq.com/apps/vice-city-online/) | ⭐ 26 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=49584123) |
| **4** | [Music Theory for Programmers](https://runjs.app/blog/music-theory-for-programmers) | ⭐ 116 | 💬 49 | [HN Thread](https://news.ycombinator.com/item?id=49541888) |
| **5** | [The revolt of the reader](https://bcantrill.dtrace.org/2026/09/05/the-revolt-of-the-reader/) | ⭐ 348 | 💬 138 | [HN Thread](https://news.ycombinator.com/item?id=49580939) |
| **6** | [The ColorChecker, photography's most important 24 squares, turns 50](https://www.dpreview.com/news/the-colorchecker-photographys-most-important-24-squares-turns-50/) | ⭐ 60 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=49529398) |
| **7** | [OpenBSD Stories: Strange Medieval Devices](http://miod.online.fr/software/openbsd/stories/smd.html) | ⭐ 60 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49539759) |
| **8** | [AI, Tools and Transformation](https://www.ben-evans.com/benedictevans/2026/9/3/ai-tools-and-transformation) | ⭐ 54 | 💬 19 | [HN Thread](https://news.ycombinator.com/item?id=49582656) |
| **9** | [Watch the 'Eclipse of the Century' Next Year When Spain, Egypt and More Go Dark](https://www.nytimes.com/2026/08/13/travel/solar-eclipse-2027-morocco-egypt.html) | ⭐ 24 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=49535634) |
| **10** | [AMD Based FreeBSD Desktop Reloaded](https://vermaden.wordpress.com/2026/09/06/amd-based-freebsd-desktop-reloaded/) | ⭐ 47 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49582719) |

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
