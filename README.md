# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Claude Fable 5.1 and Claude Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1) | ⭐ 388 | 💬 322 | [HN Thread](https://news.ycombinator.com/item?id=49525378) |
| **2** | [Play Store blocks AuroraStore, hurting GrapheneOS users](https://gitlab.com/AuroraOSS/AuroraStore/-/work_items/1566) | ⭐ 319 | 💬 119 | [HN Thread](https://news.ycombinator.com/item?id=49523754) |
| **3** | [The creator of Jujutsu has joined ERSC](https://ersc.io/blog/martin-joins-ersc) | ⭐ 73 | 💬 47 | [HN Thread](https://news.ycombinator.com/item?id=49525297) |
| **4** | [Launch HN: Nori Robotics (YC S26) – A low-cost humanoid robot for development](https://www.norirobotics.com/) | ⭐ 49 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49525153) |
| **5** | [AnkiDroid: Google Play no longer allowing Open Collective donation link](https://github.com/ankidroid/Anki-Android/issues/21656) | ⭐ 716 | 💬 199 | [HN Thread](https://news.ycombinator.com/item?id=49520022) |
| **6** | [Ambient CSS v3 – Blender meets CSS](https://ambientcss.vercel.app/) | ⭐ 112 | 💬 45 | [HN Thread](https://news.ycombinator.com/item?id=49523387) |
| **7** | [Ask HN: Who is hiring? (September 2026)](https://news.ycombinator.com/item?id=49522897) | ⭐ 138 | 💬 134 | [HN Thread](https://news.ycombinator.com/item?id=49522897) |
| **8** | [UEFA's Champions League draw creates unfair clusters; a Cayley graph fixes it](https://sariyuce.com/blog/2026/UEFA-Draw/) | ⭐ 27 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49525420) |
| **9** | [I trained a small transformer in 1.5hrs and it beats many LLMs](https://mvakde.github.io/blog/44-on-arc-1/) | ⭐ 404 | 💬 117 | [HN Thread](https://news.ycombinator.com/item?id=49519939) |
| **10** | [Show HN: Running 104GB Qwen3.8-Flash-Next on 48GB Mac with at ~12 tok/s](https://github.com/carloslfu/slotstream) | ⭐ 63 | 💬 50 | [HN Thread](https://news.ycombinator.com/item?id=49524447) |

---

## 🗄️ News Archive

- 📅 [2026-09-01](archive/2026-09-01.md)
- 📅 [2026-08-31](archive/2026-08-31.md)
- 📅 [2026-08-30](archive/2026-08-30.md)
- 📅 [2026-08-29](archive/2026-08-29.md)
- 📅 [2026-08-28](archive/2026-08-28.md)
- 📅 [2026-08-27](archive/2026-08-27.md)
- 📅 [2026-08-26](archive/2026-08-26.md)
- 📅 [2026-08-25](archive/2026-08-25.md)
- 📅 [2026-08-24](archive/2026-08-24.md)
- 📅 [2026-08-23](archive/2026-08-23.md)
- 📅 [2026-08-22](archive/2026-08-22.md)
- 📅 [2026-08-21](archive/2026-08-21.md)
- 📅 [2026-08-20](archive/2026-08-20.md)
- 📅 [2026-08-19](archive/2026-08-19.md)

*... and [5 older editions in the archive folder](archive/)*

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
python scraper.py
```

---

<div align="center">
  <sub>Maintained by <a href="https://github.com/RMNO21">RMNO21</a> • Powered by GitHub Actions & Hacker News API</sub>
</div>
