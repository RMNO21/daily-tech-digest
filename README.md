# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Why is Google still serving dodgy ads?](https://www.atomic14.com/2026/09/13/why-is-google-still-serving-dodgy-ads) | ⭐ 182 | 💬 81 | [HN Thread](https://news.ycombinator.com/item?id=49686445) |
| **2** | [Astra and Fable still hack on simple variants of alignment evals from 2025](https://www.lesswrong.com/posts/munJKF7iWMsWJLAH2/astra-and-fable-still-hack-on-simple-variants-of-alignment) | ⭐ 262 | 💬 109 | [HN Thread](https://news.ycombinator.com/item?id=49684393) |
| **3** | [Data collected by cars and sold to third parties](https://www.theverge.com/column/994172/your-car-is-selling-your-data) | ⭐ 136 | 💬 85 | [HN Thread](https://news.ycombinator.com/item?id=49683953) |
| **4** | [JetKVM Mini](https://jetkvm.com/blog/introducing-jetkvm-mini) | ⭐ 441 | 💬 171 | [HN Thread](https://news.ycombinator.com/item?id=49681152) |
| **5** | [I'm being cyberattacked by Tesla, Inc](https://dreamstation.systems/personal/tesla.html) | ⭐ 251 | 💬 68 | [HN Thread](https://news.ycombinator.com/item?id=49686766) |
| **6** | [CUDA for AMD on Windows](https://github.com/Speedstu/CUDA-for-AMD-Windows) | ⭐ 98 | 💬 51 | [HN Thread](https://news.ycombinator.com/item?id=49684356) |
| **7** | [Why is the x86 undefined instruction called ud2? Why 2?](https://devblogs.microsoft.com/oldnewthing/20260910-00/?p=112689) | ⭐ 128 | 💬 34 | [HN Thread](https://news.ycombinator.com/item?id=49683262) |
| **8** | [Sean Carroll explains the biggest ideas in the universe – Full Interview [video]](https://www.youtube.com/watch?v=_TBNJyztai0) | ⭐ 29 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49651567) |
| **9** | [Global Shortage Has Led to Motor Oil Rationing at Costco](https://guessingheadlights.com/global-shortage-has-led-to-motor-oil-rationing-at-costco/) | ⭐ 14 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49686697) |
| **10** | [Flock cameras used to arrest a child for playing on a swing](https://www.youtube.com/watch?v=koclOnlde0E) | ⭐ 44 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=49687312) |

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
