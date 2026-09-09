# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [iPhone Duo](https://www.apple.com/iphone-duo/) | ⭐ 325 | 💬 777 | [HN Thread](https://news.ycombinator.com/item?id=49630931) |
| **2** | [AirPods 5](https://www.apple.com/newsroom/2026/09/apple-introduces-airpods-5-with-best-in-class-open-ear-active-noise-cancellation/) | ⭐ 177 | 💬 138 | [HN Thread](https://news.ycombinator.com/item?id=49630253) |
| **3** | [Tailwind Labs is joining Shopify](https://tailwindcss.com/blog/tailwind-is-joining-shopify) | ⭐ 675 | 💬 285 | [HN Thread](https://news.ycombinator.com/item?id=49626190) |
| **4** | [What do Visa and Mastercard do? An intro to card networks](https://tautology.town/2026/06/01/card-networks.html) | ⭐ 153 | 💬 76 | [HN Thread](https://news.ycombinator.com/item?id=49614280) |
| **5** | [Apple Watch Series 12](https://www.apple.com/newsroom/2026/09/introducing-apple-watch-series-12-with-the-all-new-health-sensing-system/) | ⭐ 108 | 💬 94 | [HN Thread](https://news.ycombinator.com/item?id=49630566) |
| **6** | [iPhone 18 Pro and iPhone 18 Pro Max](https://www.apple.com/newsroom/2026/09/apple-debuts-iphone-18-pro-and-iphone-18-pro-max/) | ⭐ 99 | 💬 73 | [HN Thread](https://news.ycombinator.com/item?id=49630151) |
| **7** | [Qwen 3.8 follows GPT-5.5 Pro reasoning prefills](https://gist.github.com/wsxiaoys/e0286dc6bb624ff5fdf49e7f4c528ba3) | ⭐ 86 | 💬 30 | [HN Thread](https://news.ycombinator.com/item?id=49630026) |
| **8** | [GPT-6 Astra, looped transformers, and hidden reasoning](https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and) | ⭐ 234 | 💬 91 | [HN Thread](https://news.ycombinator.com/item?id=49627370) |
| **9** | [GNU Radio in the browser](https://gnuradioworld.com/) | ⭐ 123 | 💬 16 | [HN Thread](https://news.ycombinator.com/item?id=49628576) |
| **10** | [Understanding the recent DDoS attack against Read the Docs](https://about.readthedocs.com/blog/2026/09/2026-ddos-attack/) | ⭐ 95 | 💬 30 | [HN Thread](https://news.ycombinator.com/item?id=49628614) |

---

## 🗄️ News Archive

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
- 📅 [2026-08-30](archive/2026-08-30.md)
- 📅 [2026-08-29](archive/2026-08-29.md)
- 📅 [2026-08-28](archive/2026-08-28.md)
- 📅 [2026-08-27](archive/2026-08-27.md)

*... and [13 older editions in the archive folder](archive/)*

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
