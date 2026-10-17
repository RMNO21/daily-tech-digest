# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [GLP-1 may slow biological aging](https://www.universityofcalifornia.edu/news/new-study-shows-popular-glp-1-weight-loss-drug-may-slow-biological-aging) | ⭐ 61 | 💬 35 | [HN Thread](https://news.ycombinator.com/item?id=50132328) |
| **2** | [Making Chicken Transparent Using Dorito Dust](https://chillphysicsenjoyer.substack.com/p/making-chicken-transparent-using) | ⭐ 118 | 💬 42 | [HN Thread](https://news.ycombinator.com/item?id=50131213) |
| **3** | [DeepSeek-v4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) | ⭐ 407 | 💬 419 | [HN Thread](https://news.ycombinator.com/item?id=50129045) |
| **4** | [Solar surpasses nuclear power globally for first time](https://www.pv-magazine.com/2026/09/29/solar-surpasses-nuclear-power-globally-for-first-time/) | ⭐ 226 | 💬 133 | [HN Thread](https://news.ycombinator.com/item?id=50131256) |
| **5** | [Rendering pretty sky in Around The World game](https://frozenfractal.com/blog/2026/10/12/around-the-world-34-a-pretty-sky/) | ⭐ 72 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=50119315) |
| **6** | [Artie (YC S23) Is Hiring Enterprise AES and Senior Engineers](https://www.artie.com/careers) | ⭐ 1 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50132839) |
| **7** | [A Tudor Life in the Time of Plague](https://www.historytoday.com/archive/history-matters/tudor-life-time-plague) | ⭐ 24 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50082358) |
| **8** | [Tesla Roadster](https://www.tesla.com/roadster) | ⭐ 1574 | 💬 2859 | [HN Thread](https://news.ycombinator.com/item?id=50112657) |
| **9** | [The First Candid](https://www.newyorker.com/magazine/2026/10/19/the-first-candid) | ⭐ 30 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=50121506) |
| **10** | [Ultramarine 1 Flash](https://www.paperinstruments.com/ultramarine) | ⭐ 348 | 💬 103 | [HN Thread](https://news.ycombinator.com/item?id=50106747) |

---

## 🗄️ News Archive

- 📅 [2026-10-17](archive/2026-10-17.md)
- 📅 [2026-10-16](archive/2026-10-16.md)
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

*... and [46 older editions in the archive folder](archive/)*

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
