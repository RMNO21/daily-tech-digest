# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [JetKVM Mini](https://jetkvm.com/blog/introducing-jetkvm-mini) | ⭐ 181 | 💬 79 | [HN Thread](https://news.ycombinator.com/item?id=49681152) |
| **2** | [Nvidia dismisses "circular financing", says every $1 it invests brings back $100](https://invezz.com/news/2026/09/11/nvidia-says-every-1-it-invests-brings-back-100-so-why-does-the-stock-keep-falling/) | ⭐ 56 | 💬 43 | [HN Thread](https://news.ycombinator.com/item?id=49682319) |
| **3** | [Why are AI agents lying, cheating and coordinating?](https://yoshuabengio.org/en/publication/why-are-ai-agents-lying-cheating-and-coordinating) | ⭐ 291 | 💬 345 | [HN Thread](https://news.ycombinator.com/item?id=49678969) |
| **4** | [Make your first edit to OpenStreetMap](https://high5apps.github.io/josm-plugin-website-wizard/) | ⭐ 490 | 💬 126 | [HN Thread](https://news.ycombinator.com/item?id=49674050) |
| **5** | [The Interim Computer Museum](https://icm.museum/) | ⭐ 126 | 💬 13 | [HN Thread](https://news.ycombinator.com/item?id=49679459) |
| **6** | [I Added a Non-Wi-Fi Mitsubishi AC to Home Assistant](https://medium.com/@ivangomezarnedo/how-i-added-a-non-wi-fi-mitsubishi-ac-to-home-assistant-22770661dd77) | ⭐ 104 | 💬 50 | [HN Thread](https://news.ycombinator.com/item?id=49640913) |
| **7** | [How to Use Three.js's New Native Gaussian Splats](https://ben3d.ca/blog/how-to-use-threejs-native-gaussian-splats) | ⭐ 18 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49624366) |
| **8** | [Homebrew 7.0.0](https://brew.sh/2026/09/13/homebrew-7.0.0/) | ⭐ 88 | 💬 33 | [HN Thread](https://news.ycombinator.com/item?id=49681545) |
| **9** | [Apple iPod Engraver (2019)](https://dunstanorchard.com/apple-ipod-engraver/) | ⭐ 237 | 💬 61 | [HN Thread](https://news.ycombinator.com/item?id=49619848) |
| **10** | [Revolut confirms customer data breach through fake government requests](https://techcrunch.com/2026/09/12/revolut-confirms-customer-data-breach-through-fake-government-requests/) | ⭐ 32 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=49682087) |

---

## 🗄️ News Archive

- 📅 [2026-09-13](archive/2026-09-13.md)
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

*... and [17 older editions in the archive folder](archive/)*

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
