# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [iOS 27, iPadOS 27, and macOS 27](https://www.apple.com/newsroom/2026/09/major-updates-for-apples-software-platforms-are-now-available/) | ⭐ 559 | 💬 623 | [HN Thread](https://news.ycombinator.com/item?id=49701004) |
| **2** | [Linux from Scratch](https://www.linuxfromscratch.org/) | ⭐ 116 | 💬 39 | [HN Thread](https://news.ycombinator.com/item?id=49707627) |
| **3** | [OpenArm: An open-source 7DOF humanoid arm](https://github.com/enactic/OpenArm) | ⭐ 56 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49684289) |
| **4** | [4,400-Year-Old Tomb of Egyptian Judge Found at Saqqara with Colors on Walls](https://arkeonews.net/4400-year-old-tomb-of-an-egyptian-judge-found-at-saqqara-with-colors-still-on-the-walls/) | ⭐ 113 | 💬 29 | [HN Thread](https://news.ycombinator.com/item?id=49675817) |
| **5** | [Pion, an agent designed to run any company autonomously](https://andonlabs.com/blog/why-we-built-pion) | ⭐ 380 | 💬 444 | [HN Thread](https://news.ycombinator.com/item?id=49700477) |
| **6** | [When code is a maze, smart developers make maps (2025)](https://medium.com/@simonsmartiom/when-code-is-a-maze-smart-developers-make-maps-fbc452a48c1b) | ⭐ 20 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=49693690) |
| **7** | [Charts built for Chat](https://dbtcharts.com/blog/charts-built-for-chat/) | ⭐ 205 | 💬 64 | [HN Thread](https://news.ycombinator.com/item?id=49704246) |
| **8** | [Lingo.dev (YC F24) is hiring a senior content engineer (Remote, worldwide)](https://lingo.dev/en/careers/ff88132a-cb79-4d35-a6a0-a6230de7a013) | ⭐ 1 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49708774) |
| **9** | [XCancel service is suspended until further notice](https://xcancel.com/#) | ⭐ 590 | 💬 882 | [HN Thread](https://news.ycombinator.com/item?id=49694296) |
| **10** | [Dropping eBPF CPU Cost by About 90% with Memoization (Not AI Gen)](https://nathannaveen.dev/posts/dropping-ebpf-cpu-cost-by-90/) | ⭐ 95 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=49697477) |

---

## 🗄️ News Archive

- 📅 [2026-09-15](archive/2026-09-15.md)
- 📅 [2026-09-14](archive/2026-09-14.md)
- 📅 [2026-09-13](archive/2026-09-13.md)
- 📅 [2026-09-12](archive/2026-09-12.md)
- 📅 [2026-09-11](archive/2026-09-11.md)
- 📅 [2026-09-10](archive/2026-09-10.md)
- 📅 [2026-09-09](archive/2026-09-09.md)
- 📅 [2026-09-08](archive/2026-09-08.md)
- 📅 [2026-09-07](archive/2026-09-07.md)
- 📅 [2026-09-06](archive/2026-09-06.md)
- 📅 [2026-09-05](archive/2026-09-05.md)
- 📅 [2026-09-04](archive/2026-09-04.md)
- 📅 [2026-09-03](archive/2026-09-03.md)
- 📅 [2026-09-02](archive/2026-09-02.md)

*... and [19 older editions in the archive folder](archive/)*

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
