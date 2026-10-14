# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Felix Rieseberg Homepage](https://felixrieseberg.com/) | ⭐ 80 | 💬 26 | [HN Thread](https://news.ycombinator.com/item?id=50082470) |
| **2** | [Gemini 4 Argon](https://deepmind.google/models/gemini/) | ⭐ 1179 | 💬 838 | [HN Thread](https://news.ycombinator.com/item?id=50073879) |
| **3** | [Sound – Bartosz Ciechanowski (2022)](https://ciechanow.ski/sound/) | ⭐ 58 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=50045147) |
| **4** | [Ledger confirms spy chip implant behind wallet crypto thefts](https://www.bleepingcomputer.com/news/security/ledger-confirms-hardware-wallet-spy-implant-behind-crypto-thefts/) | ⭐ 597 | 💬 392 | [HN Thread](https://news.ycombinator.com/item?id=50054092) |
| **5** | [Is 'Attention' the Essence of Intelligence?](https://www.quantamagazine.org/is-attention-the-essence-of-intelligence-20261012/) | ⭐ 49 | 💬 37 | [HN Thread](https://news.ycombinator.com/item?id=50081930) |
| **6** | [Show HN: Guitoro, a virtual guitar you strum with your keyboard](https://guitoro.com/) | ⭐ 375 | 💬 99 | [HN Thread](https://news.ycombinator.com/item?id=50077020) |
| **7** | [Redesigning source control at Anthropic](https://www.anthropic.com/engineering/redesigning-source-control) | ⭐ 677 | 💬 648 | [HN Thread](https://news.ycombinator.com/item?id=50073633) |
| **8** | [900-Page Pre-Pantone Guide to Color from 1692 (With Complete High-Res Scan)](https://www.openculture.com/2026/10/a-900-page-pre-pantone-guide-to-color-from-1692.html) | ⭐ 119 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=50053487) |
| **9** | [Grace Hopper Celebration Cancelled](https://anitab.org/press-release) | ⭐ 101 | 💬 26 | [HN Thread](https://news.ycombinator.com/item?id=50080007) |
| **10** | [I built a tool to track what AI leaders say and how their views change on video](https://blumify.io/people) | ⭐ 67 | 💬 47 | [HN Thread](https://news.ycombinator.com/item?id=50081151) |

---

## 🗄️ News Archive

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
- 📅 [2026-09-28](archive/2026-09-28.md)

*... and [43 older editions in the archive folder](archive/)*

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
