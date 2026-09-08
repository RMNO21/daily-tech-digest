# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Google DeepMind Releases AlphaGenome Atlas](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/) | ⭐ 311 | 💬 76 | [HN Thread](https://news.ycombinator.com/item?id=49611251) |
| **2** | [DaVinci Resolve 21.1](https://www.blackmagicdesign.com/media/release/20260908-03) | ⭐ 266 | 💬 111 | [HN Thread](https://news.ycombinator.com/item?id=49610181) |
| **3** | [On the Navier–Stokes Millennium Prize Problem](https://openai.com/index/navier-stokes-solution/) | ⭐ 485 | 💬 335 | [HN Thread](https://news.ycombinator.com/item?id=49613262) |
| **4** | [Benchmarking Qwen3.8 27B quantizations: 4-bit holds up, 1-bit collapses](https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/) | ⭐ 113 | 💬 72 | [HN Thread](https://news.ycombinator.com/item?id=49611128) |
| **5** | [OUI-1: world's first model for Generative UI](https://www.openui.com/blog/oui-1) | ⭐ 36 | 💬 30 | [HN Thread](https://news.ycombinator.com/item?id=49613182) |
| **6** | [The Helicopter with Radioactive Blades](https://hackaday.com/2026/09/07/the-helicopter-with-radioactive-blades/) | ⭐ 86 | 💬 18 | [HN Thread](https://news.ycombinator.com/item?id=49600901) |
| **7** | [Show HN: LLM Attention Visualization](https://ishamf.dev/p/llm-attention-visualizer/) | ⭐ 31 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49613068) |
| **8** | [Connecting the Machines](https://herdr.dev/blog/connecting-the-machines/) | ⭐ 34 | 💬 13 | [HN Thread](https://news.ycombinator.com/item?id=49612818) |
| **9** | [LG TVs caught spying even when offline or on standby](https://www.theverge.com/tech/991190/lg-tv-spying-standby-recording-wi-fi-scanning-gamers-nexus) | ⭐ 246 | 💬 124 | [HN Thread](https://news.ycombinator.com/item?id=49612329) |
| **10** | [I-have-ADHD: A skill to stop coding agents from burying the answer](https://github.com/ayghri/i-have-adhd) | ⭐ 139 | 💬 107 | [HN Thread](https://news.ycombinator.com/item?id=49610631) |

---

## 🗄️ News Archive

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
- 📅 [2026-08-29](archive/2026-08-29.md)
- 📅 [2026-08-28](archive/2026-08-28.md)
- 📅 [2026-08-27](archive/2026-08-27.md)
- 📅 [2026-08-26](archive/2026-08-26.md)

*... and [12 older editions in the archive folder](archive/)*

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
