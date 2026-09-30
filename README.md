# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Pi.dev: You Said No MCP](https://earendil.com/posts/you-said-no-mcp/) | ⭐ 255 | 💬 122 | [HN Thread](https://news.ycombinator.com/item?id=49906637) |
| **2** | [The last time my family was replaced by technology](https://manuel.darcemont.fr/posts/the-last-time-my-family-was-replaced-by-technology/) | ⭐ 29 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=49908394) |
| **3** | [Show HN: JBR-001 – An open-source 3D printable desktop robot](https://projecthub.arduino.cc/syntheticaidata/jbr-001-a-desktop-companion-robot-powered-by-arduino-uno-q-b11c96) | ⭐ 60 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=49890707) |
| **4** | [Livenerf: Has Opus 5.5 been nerfed yet?](https://github.com/ninjahawk/livenerf) | ⭐ 738 | 💬 301 | [HN Thread](https://news.ycombinator.com/item?id=49901736) |
| **5** | [Solving Factorio Quality](https://exyr.org/2026/solving-factorio-quality/) | ⭐ 154 | 💬 44 | [HN Thread](https://news.ycombinator.com/item?id=49887343) |
| **6** | [Mathematical Origami](https://mathigon.org/origami) | ⭐ 23 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49889140) |
| **7** | [Dots: Always-on agents](https://openai.com/index/introducing-dots/) | ⭐ 680 | 💬 534 | [HN Thread](https://news.ycombinator.com/item?id=49896604) |
| **8** | [Vermont replacing power plants with home batteries](https://www.bbc.com/future/article/20260928-a-virtual-power-plant-hidden-in-vermont-homes-is-keeping-the-lights-on-during-storms) | ⭐ 266 | 💬 210 | [HN Thread](https://news.ycombinator.com/item?id=49897993) |
| **9** | [America.gov](https://america.gov/) | ⭐ 655 | 💬 541 | [HN Thread](https://news.ycombinator.com/item?id=49893509) |
| **10** | [NASA asked several former SR-71A staffers to help secret restart](https://aviationweek.com/defense/aircraft-propulsion/nasa-asked-several-former-sr-71a-staffers-help-secret-restart) | ⭐ 225 | 💬 219 | [HN Thread](https://news.ycombinator.com/item?id=49890733) |

---

## 🗄️ News Archive

- 📅 [2026-09-30](archive/2026-09-30.md)
- 📅 [2026-09-29](archive/2026-09-29.md)
- 📅 [2026-09-28](archive/2026-09-28.md)
- 📅 [2026-09-27](archive/2026-09-27.md)
- 📅 [2026-09-26](archive/2026-09-26.md)
- 📅 [2026-09-25](archive/2026-09-25.md)
- 📅 [2026-09-24](archive/2026-09-24.md)
- 📅 [2026-09-22](archive/2026-09-22.md)
- 📅 [2026-09-21](archive/2026-09-21.md)
- 📅 [2026-09-20](archive/2026-09-20.md)
- 📅 [2026-09-19](archive/2026-09-19.md)
- 📅 [2026-09-18](archive/2026-09-18.md)
- 📅 [2026-09-16](archive/2026-09-16.md)
- 📅 [2026-09-15](archive/2026-09-15.md)

*... and [32 older editions in the archive folder](archive/)*

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
