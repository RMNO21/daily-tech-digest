# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [I Don't Understand Quantum Physics](https://www.southampton.ac.uk/~doug/quantum_physics/index.html) | ⭐ 69 | 💬 32 | [HN Thread](https://news.ycombinator.com/item?id=50219666) |
| **2** | [OBS Studio 33](https://github.com/obsproject/obs-studio/releases/tag/33.0.0) | ⭐ 172 | 💬 53 | [HN Thread](https://news.ycombinator.com/item?id=50218430) |
| **3** | [Kimi K3.1 Pro and K3.1 Pro Highspeed](https://www.kimi.ai/blog/kimi-k3-1-pro) | ⭐ 927 | 💬 550 | [HN Thread](https://news.ycombinator.com/item?id=50212065) |
| **4** | [Today, we hacked what we'd set out to hack: the iPhone](https://blog.calif.io/p/iphone) | ⭐ 901 | 💬 589 | [HN Thread](https://news.ycombinator.com/item?id=50211474) |
| **5** | [Physicists trap a single antimatter particle for a month](https://www.scientificamerican.com/article/physicists-trap-a-single-antimatter-particle-for-a-month/) | ⭐ 64 | 💬 23 | [HN Thread](https://news.ycombinator.com/item?id=50186450) |
| **6** | [Twelve years of distributed SQLite](https://philipotoole.com/twelve-years-of-distributed-sqlite/) | ⭐ 218 | 💬 32 | [HN Thread](https://news.ycombinator.com/item?id=50217500) |
| **7** | [How close can pure functional programming get to C?](https://rtfeldman.com/fp-vs-c) | ⭐ 133 | 💬 19 | [HN Thread](https://news.ycombinator.com/item?id=50218195) |
| **8** | [Around a dozen banking apps began specifically permitting GrapheneOS](https://grapheneos.social/@GrapheneOS/117492375462459244) | ⭐ 128 | 💬 21 | [HN Thread](https://news.ycombinator.com/item?id=50217495) |
| **9** | [Apple Music 404 Not Found](https://music.apple.com/this-url-doesnt-exist) | ⭐ 780 | 💬 237 | [HN Thread](https://news.ycombinator.com/item?id=50207910) |
| **10** | [How to run a city builder on 16 MHz](https://larstofus.com/2025/11/16/how-to-run-a-city-builder-on-12-5-mhz/) | ⭐ 24 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=50194536) |

---

## 🗄️ News Archive

- 📅 [2026-10-24](archive/2026-10-24.md)
- 📅 [2026-10-23](archive/2026-10-23.md)
- 📅 [2026-10-22](archive/2026-10-22.md)
- 📅 [2026-10-21](archive/2026-10-21.md)
- 📅 [2026-10-20](archive/2026-10-20.md)
- 📅 [2026-10-19](archive/2026-10-19.md)
- 📅 [2026-10-18](archive/2026-10-18.md)
- 📅 [2026-10-17](archive/2026-10-17.md)
- 📅 [2026-10-16](archive/2026-10-16.md)
- 📅 [2026-10-15](archive/2026-10-15.md)
- 📅 [2026-10-14](archive/2026-10-14.md)
- 📅 [2026-10-13](archive/2026-10-13.md)
- 📅 [2026-10-10](archive/2026-10-10.md)
- 📅 [2026-10-09](archive/2026-10-09.md)

*... and [53 older editions in the archive folder](archive/)*

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
