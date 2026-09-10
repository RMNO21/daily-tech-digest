# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [iPhone Duo](https://www.apple.com/iphone-duo/) | ⭐ 1079 | 💬 1914 | [HN Thread](https://news.ycombinator.com/item?id=49630931) |
| **2** | [Show HN: What if the speed of light was 5 km/h?](https://rivendell.dmitrybrant.com/relativity/) | ⭐ 168 | 💬 75 | [HN Thread](https://news.ycombinator.com/item?id=49637385) |
| **3** | [Version Control Second Coming](https://psantosl.github.io/posts/version-control-second-coming/) | ⭐ 34 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49603265) |
| **4** | [ESP32 Bit Pirate Hardware Hacking Kit with Web Tools That Speaks Every Protocol](https://geo-tp.github.io/ESP32-Bit-Pirate/) | ⭐ 52 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49587465) |
| **5** | [Shopify acquires Tailwind](https://tailwindcss.com/blog/tailwind-is-joining-shopify) | ⭐ 974 | 💬 382 | [HN Thread](https://news.ycombinator.com/item?id=49626190) |
| **6** | [All grown-ups were once children… but only few of them remember it](https://mathstodon.xyz/@tao/117244102901892965) | ⭐ 16 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49638280) |
| **7** | [What do Visa and Mastercard do? An intro to card networks](https://tautology.town/2026/06/01/card-networks.html) | ⭐ 465 | 💬 255 | [HN Thread](https://news.ycombinator.com/item?id=49614280) |
| **8** | [Growing proof that autonomous cars save lives](https://spectrum.ieee.org/are-self-driving-cars-safe) | ⭐ 305 | 💬 500 | [HN Thread](https://news.ycombinator.com/item?id=49629886) |
| **9** | [Training a 3.8B LLM to 0.384 CORE for $998 – Hugo Vergnes](https://hugovergnes.github.io/little-lm-3-8b/) | ⭐ 39 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49637435) |
| **10** | [AirPods 5](https://www.apple.com/newsroom/2026/09/apple-introduces-airpods-5-with-best-in-class-open-ear-active-noise-cancellation/) | ⭐ 426 | 💬 334 | [HN Thread](https://news.ycombinator.com/item?id=49630253) |

---

## 🗄️ News Archive

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
- 📅 [2026-08-30](archive/2026-08-30.md)
- 📅 [2026-08-29](archive/2026-08-29.md)
- 📅 [2026-08-28](archive/2026-08-28.md)

*... and [14 older editions in the archive folder](archive/)*

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
