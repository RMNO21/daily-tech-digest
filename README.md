# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Muse Spark Open](https://research.meta.ai/blog/muse-spark-open) | ⭐ 519 | 💬 297 | [HN Thread](https://news.ycombinator.com/item?id=50107379) |
| **2** | [What I Self-Host](https://viceconsole.fyi/blog/2026/10/10/what-i-self-host/) | ⭐ 104 | 💬 47 | [HN Thread](https://news.ycombinator.com/item?id=50109715) |
| **3** | [Neural networks are clean](https://already-clean.goodfire.com/) | ⭐ 414 | 💬 146 | [HN Thread](https://news.ycombinator.com/item?id=50105647) |
| **4** | [Call Center Jobs Are Declining, but 14,000 Calls Show Humans Still Outperform AI](https://boldagents.co/blog/call-center-jobs-declining-14000-calls-humans-outperform-ai) | ⭐ 20 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=50111112) |
| **5** | [Someone on Torrent Sites Kept Fucking with My Sonarr](https://thereallo.dev/blog/someone-on-torrent-sites-kept-fucking-with-my-sonarr-setup) | ⭐ 117 | 💬 56 | [HN Thread](https://news.ycombinator.com/item?id=50108872) |
| **6** | [Wayland desktop for Linux with skeuomorphic design](https://github.com/fyzugx/DEsk) | ⭐ 449 | 💬 176 | [HN Thread](https://news.ycombinator.com/item?id=50103338) |
| **7** | [Krea 3 – An image model built for editing at scale](https://www.krea.ai/krea-3) | ⭐ 217 | 💬 73 | [HN Thread](https://news.ycombinator.com/item?id=50105648) |
| **8** | [Jev meets the Trolley Problem](https://zachlandes.com/trolley-problem/) | ⭐ 217 | 💬 103 | [HN Thread](https://news.ycombinator.com/item?id=50106023) |
| **9** | [AdFection: Targeted ads turned into a pipeline for zero-click mercenary spyware](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/) | ⭐ 334 | 💬 494 | [HN Thread](https://news.ycombinator.com/item?id=50101813) |
| **10** | [E Ink Kaleido 4](https://www.eink.com/news/detail/EInk-Launches-Latest-Version-of-Color-ePaper-Platform-E-Ink-Kaleido-4) | ⭐ 93 | 💬 59 | [HN Thread](https://news.ycombinator.com/item?id=50108229) |

---

## 🗄️ News Archive

- 📅 [2026-10-15](archive/2026-10-15.md)
- 📅 [2026-10-14](archive/2026-10-14.md)
- 📅 [2026-10-13](archive/2026-10-13.md)
- 📅 [2026-10-10](archive/2026-10-10.md)
- 📅 [2026-10-09](archive/2026-10-09.md)
- 📅 [2026-10-08](archive/2026-10-08.md)
- 📅 [2026-10-07](archive/2026-10-07.md)
- 📅 [2026-10-05](archive/2026-10-05.md)
- 📅 [2026-10-04](archive/2026-10-04.md)
- 📅 [2026-10-03](archive/2026-10-03.md)
- 📅 [2026-10-02](archive/2026-10-02.md)
- 📅 [2026-10-01](archive/2026-10-01.md)
- 📅 [2026-09-30](archive/2026-09-30.md)
- 📅 [2026-09-29](archive/2026-09-29.md)

*... and [44 older editions in the archive folder](archive/)*

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
