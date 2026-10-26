# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [OLED iPad Mini](https://www.apple.com/shop/buy-ipad/ipad-mini) | ⭐ 46 | 💬 27 | [HN Thread](https://news.ycombinator.com/item?id=50243646) |
| **2** | [The new iPad mini](https://www.apple.com/newsroom/2026/10/apple-gives-ipad-mini-its-biggest-update-ever/) | ⭐ 31 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=50243061) |
| **3** | [Fixing Tool-Call Accuracy in vLLM](https://www.ubicloud.com/blog/fixing-tool-call-accuracy-in-vllm) | ⭐ 39 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=50242870) |
| **4** | [Switzerland. Block by block. At 1:1 scale](https://blocks.manifold3d.ch/) | ⭐ 319 | 💬 140 | [HN Thread](https://news.ycombinator.com/item?id=50240922) |
| **5** | [Birdwatching rewires the brain and slows cognitive decline](https://www.bbc.com/future/article/20261019-birdwatching-rewires-the-brain-and-slows-cognitive-decline) | ⭐ 225 | 💬 94 | [HN Thread](https://news.ycombinator.com/item?id=50215997) |
| **6** | [Anthropic S-1](https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm) | ⭐ 425 | 💬 335 | [HN Thread](https://news.ycombinator.com/item?id=50242939) |
| **7** | [One of the Greatest Inventions in the History of Human Transport](https://humantransit.org/2024/12/one-of-the-greatest-inventions-in-the-history-of-human-transport.html) | ⭐ 47 | 💬 13 | [HN Thread](https://news.ycombinator.com/item?id=50200152) |
| **8** | [Show HN: TitleArt – Make text like it's 1997](https://titleart.dvy.io/) | ⭐ 315 | 💬 56 | [HN Thread](https://news.ycombinator.com/item?id=50238708) |
| **9** | [Behind the scenes at the NeXT Computer office](https://exhibits.stanford.edu/menuez/browse/next-computer-inc?per_page=96&sort=pub_year_isi+asc%2C+title_sort+asc&view=masonry) | ⭐ 180 | 💬 100 | [HN Thread](https://news.ycombinator.com/item?id=50238763) |
| **10** | [Tasks as Code: Move Your Tickets into the Repository](https://typemill.net/knowledge-hub/tasks-as-code) | ⭐ 37 | 💬 35 | [HN Thread](https://news.ycombinator.com/item?id=50241924) |

---

## 🗄️ News Archive

- 📅 [2026-10-26](archive/2026-10-26.md)
- 📅 [2026-10-25](archive/2026-10-25.md)
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

*... and [55 older editions in the archive folder](archive/)*

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
