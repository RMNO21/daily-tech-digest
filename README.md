# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Residential proxies detected on White House network](https://layer3intel.com/blog/residential-proxies-white-house-network) | ⭐ 911 | 💬 276 | [HN Thread](https://news.ycombinator.com/item?id=50371246) |
| **2** | [Lemmings CSS Animation](https://markblah.github.io/lemmings/) | ⭐ 56 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=50375354) |
| **3** | [Images 2.6](https://openai.com/index/introducing-images-2-6/) | ⭐ 227 | 💬 147 | [HN Thread](https://news.ycombinator.com/item?id=50372945) |
| **4** | [A thousand fewer paths to root](https://openai.com/index/a-thousand-fewer-paths-to-root/) | ⭐ 266 | 💬 161 | [HN Thread](https://news.ycombinator.com/item?id=50372929) |
| **5** | [Starfall – Affordable, routine access to microgravity](https://www.spacex.com/starfall) | ⭐ 189 | 💬 120 | [HN Thread](https://news.ycombinator.com/item?id=50373308) |
| **6** | [Ripple-65B Preview: U.S. Open-Weight SOTA on Agentic Coding](https://www.ricursive.com/ripple) | ⭐ 274 | 💬 99 | [HN Thread](https://news.ycombinator.com/item?id=50369925) |
| **7** | [Kimi K3.1 Pro model weights are out](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) | ⭐ 474 | 💬 134 | [HN Thread](https://news.ycombinator.com/item?id=50366999) |
| **8** | [Spreading Liquid with Three.js](https://mofu-dev.com/en/blog/fluid-foundation/) | ⭐ 41 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=50341576) |
| **9** | [Insects don't swarm at LED lights](https://www.birdsoutsidemywindow.org/2026/11/03/insects-dont-swarm-at-led-lights/) | ⭐ 225 | 💬 119 | [HN Thread](https://news.ycombinator.com/item?id=50370610) |
| **10** | [A new Go API for JSON](https://go.dev/blog/jsonv2) | ⭐ 278 | 💬 126 | [HN Thread](https://news.ycombinator.com/item?id=50369106) |

---

## 🗄️ News Archive

- 📅 [2026-11-05](archive/2026-11-05.md)
- 📅 [2026-11-04](archive/2026-11-04.md)
- 📅 [2026-11-03](archive/2026-11-03.md)
- 📅 [2026-11-02](archive/2026-11-02.md)
- 📅 [2026-10-31](archive/2026-10-31.md)
- 📅 [2026-10-30](archive/2026-10-30.md)
- 📅 [2026-10-28](archive/2026-10-28.md)
- 📅 [2026-10-27](archive/2026-10-27.md)
- 📅 [2026-10-26](archive/2026-10-26.md)
- 📅 [2026-10-25](archive/2026-10-25.md)
- 📅 [2026-10-24](archive/2026-10-24.md)
- 📅 [2026-10-23](archive/2026-10-23.md)
- 📅 [2026-10-22](archive/2026-10-22.md)
- 📅 [2026-10-21](archive/2026-10-21.md)

*... and [63 older editions in the archive folder](archive/)*

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
