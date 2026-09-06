# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Intellectual Fly Is Open](https://bcantrill.dtrace.org/2025/12/05/your-intellectual-fly-is-open/) | ⭐ 120 | 💬 71 | [HN Thread](https://news.ycombinator.com/item?id=49585644) |
| **2** | [Isar Aerospace reaches orbit and deploys payloads on second flight](https://isaraerospace.com/press/history-for-european-spaceflight-isar-aerospace-reaches-orbit-and-deploys-payloads-on-second-flight) | ⭐ 324 | 💬 87 | [HN Thread](https://news.ycombinator.com/item?id=49584083) |
| **3** | [Doomscrolling Ourselves to Death](https://www.edwest.co.uk/p/doomscrolling-ourselves-to-death) | ⭐ 70 | 💬 40 | [HN Thread](https://news.ycombinator.com/item?id=49585627) |
| **4** | [M-DISC – DVD/Blu-ray compatible discs that may last up to 1000 years](https://en.wikipedia.org/wiki/M-DISC) | ⭐ 70 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=49531619) |
| **5** | [Cloud in a Bottle: making self-hosting accessible to everyone](https://cloudinabottle.org/blog/launch-post) | ⭐ 489 | 💬 242 | [HN Thread](https://news.ycombinator.com/item?id=49582000) |
| **6** | [The revolt of the reader](https://bcantrill.dtrace.org/2026/09/05/the-revolt-of-the-reader/) | ⭐ 441 | 💬 200 | [HN Thread](https://news.ycombinator.com/item?id=49580939) |
| **7** | [I Changed My License](https://bergie.iki.fi/blog/eupl/) | ⭐ 98 | 💬 93 | [HN Thread](https://news.ycombinator.com/item?id=49585161) |
| **8** | [The pencil case model of creativity](https://dub.uu.nl/en/column/pencil-case-model-creativity) | ⭐ 16 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49585703) |
| **9** | [Music Theory for Programmers](https://runjs.app/blog/music-theory-for-programmers) | ⭐ 212 | 💬 114 | [HN Thread](https://news.ycombinator.com/item?id=49541888) |
| **10** | [IBM Quantum Nighthawk R2](https://www.ibm.com/quantum/blog/nighthawk-r2) | ⭐ 38 | 💬 19 | [HN Thread](https://news.ycombinator.com/item?id=49546198) |

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
