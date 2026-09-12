# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Make your first edit to OpenStreetMap](https://high5apps.github.io/josm-plugin-website-wizard/) | ⭐ 238 | 💬 66 | [HN Thread](https://news.ycombinator.com/item?id=49674050) |
| **2** | [Nvidia is the central bank of AI](https://www.economist.com/interactive/briefing/2026/09/03/nvidia-is-the-central-bank-of-ai) | ⭐ 319 | 💬 215 | [HN Thread](https://news.ycombinator.com/item?id=49673098) |
| **3** | [Real-SWE: Benchmarking AI models on private, real-world, enterprise codebases](https://withspecific.com/benchmarks/real-swe) | ⭐ 35 | 💬 26 | [HN Thread](https://news.ycombinator.com/item?id=49676820) |
| **4** | [Apple iPod Engraver (2019)](https://dunstanorchard.com/apple-ipod-engraver/) | ⭐ 43 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49619848) |
| **5** | [Stabilizing Rust's Never Type](https://lwn.net/SubscriberLink/1091015/d9e48318ed242b41/) | ⭐ 99 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=49625056) |
| **6** | [Benchmark: CadQuery vs. OpenSCAD for agentic CAD work](https://modelrift.com/blog/cadquery-vs-openscad/) | ⭐ 22 | 💬 27 | [HN Thread](https://news.ycombinator.com/item?id=49676577) |
| **7** | [LG denies TV spying claims, says tracking and snooping concerns 'not true'](https://www.tomshardware.com/tech-industry/big-tech/lg-strongly-denies-tv-security-claims-says-tracking-and-snooping-concerns-not-true-online-investigation-claims-216-000-000-spy-tvs-record-audio) | ⭐ 339 | 💬 295 | [HN Thread](https://news.ycombinator.com/item?id=49645480) |
| **8** | [Will There Be a 7G?](https://arxiv.org/abs/2609.01877) | ⭐ 64 | 💬 110 | [HN Thread](https://news.ycombinator.com/item?id=49674498) |
| **9** | [IKEA made a mod for Skyrim [video]](https://www.youtube.com/watch?v=iZODN0QUgjI) | ⭐ 528 | 💬 136 | [HN Thread](https://news.ycombinator.com/item?id=49639647) |
| **10** | [I made a build visualizer to understand Bun's compile times](https://lalitm.com/post/buildprof/) | ⭐ 70 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=49672842) |

---

## 🗄️ News Archive

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
- 📅 [2026-09-01](archive/2026-09-01.md)
- 📅 [2026-08-31](archive/2026-08-31.md)
- 📅 [2026-08-30](archive/2026-08-30.md)

*... and [16 older editions in the archive folder](archive/)*

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
