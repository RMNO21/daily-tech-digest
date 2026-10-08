# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Whistle: Speech to Text in 16.9 MB](https://cactuscompute.com/blog/whistle) | ⭐ 390 | 💬 98 | [HN Thread](https://news.ycombinator.com/item?id=50008427) |
| **2** | [ADHD as a circadian rhythm disorder: evidence and implications for chronotherapy](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2025.1697900/full) | ⭐ 43 | 💬 22 | [HN Thread](https://news.ycombinator.com/item?id=50011928) |
| **3** | [Why isn't the industry freaking out about DeepSeek 4.1 Flash?](https://www.dgt.is/blog/2026-10-07-deepseek-freek-out/) | ⭐ 237 | 💬 204 | [HN Thread](https://news.ycombinator.com/item?id=50000488) |
| **4** | [Theranos.world](https://www.theranos.world/) | ⭐ 151 | 💬 78 | [HN Thread](https://news.ycombinator.com/item?id=50009295) |
| **5** | [The value of not getting to the point (2015)](https://ken.arneson.name/2015/11/the-value-of-not-getting-to-the-point/) | ⭐ 75 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=50010470) |
| **6** | [AI-ready biological data: $1.8B global commitment](https://biohub.org/news/virtual-biology-initiative-expansion/) | ⭐ 27 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=50011999) |
| **7** | [I hired an illustrator to draw my house. Now it's my Home Assistant dashboard](https://antonfrolov.substack.com/p/i-hired-an-illustrator-to-draw-my) | ⭐ 232 | 💬 29 | [HN Thread](https://news.ycombinator.com/item?id=49986882) |
| **8** | [Man discovers his parents' coffee machine used 1TB of data in 10 days](https://www.dexerto.com/entertainment/man-discovers-his-parents-coffee-machine-used-1tb-of-data-in-10-days-3416399/) | ⭐ 242 | 💬 141 | [HN Thread](https://news.ycombinator.com/item?id=49995495) |
| **9** | [A Terminal Protocol for Program Status (OSC 7501)](https://mitchellh.com/writing/program-status-osc7501) | ⭐ 57 | 💬 16 | [HN Thread](https://news.ycombinator.com/item?id=49984159) |
| **10** | [Show HN: Free open source Adobe Lightroom alternative, completely local with AI](https://github.com/thesnarkitecht/rembrandt) | ⭐ 18 | 💬 16 | [HN Thread](https://news.ycombinator.com/item?id=50012199) |

---

## 🗄️ News Archive

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
- 📅 [2026-09-27](archive/2026-09-27.md)
- 📅 [2026-09-26](archive/2026-09-26.md)
- 📅 [2026-09-25](archive/2026-09-25.md)
- 📅 [2026-09-24](archive/2026-09-24.md)

*... and [39 older editions in the archive folder](archive/)*

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
