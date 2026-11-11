# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Protecting SSH Keys with macOS Secure Enclave](https://gatezh.com/posts/macos-secure-enclave-ssh-keys/) | ⭐ 75 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=50449748) |
| **2** | [Greg Kurtzer's Ginux is now a userspace kernel](https://github.com/gmkurtzer/ginux) | ⭐ 28 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=50450007) |
| **3** | [Scion is back and is going to sell a kei truck in America](https://www.theautopian.com/scion-is-back-and-its-going-to-sell-a-freaking-kei-truck-in-america/) | ⭐ 431 | 💬 291 | [HN Thread](https://news.ycombinator.com/item?id=50445401) |
| **4** | [.name Grandfathered](https://neil.fraser.name/news/2026/11/10/) | ⭐ 761 | 💬 169 | [HN Thread](https://news.ycombinator.com/item?id=50442736) |
| **5** | [Smart home devices should work without the internet](https://docodethatmatters.com/home-automation-overnight-success/) | ⭐ 841 | 💬 300 | [HN Thread](https://news.ycombinator.com/item?id=50441707) |
| **6** | [A great old-timey game-programming hack (2013)](https://blog.moertel.com/posts/2013-12-14-great-old-timey-game-programming-hack.html) | ⭐ 95 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=50448921) |
| **7** | [To deter bioterrorism, U.S. imposes new rules on ordering synthetic DNA](https://www.science.org/content/article/deter-bioterrorism-u-s-imposes-new-rules-ordering-synthetic-dna) | ⭐ 53 | 💬 28 | [HN Thread](https://news.ycombinator.com/item?id=50449275) |
| **8** | [Six Math Essentials](https://teorth.github.io/tao-web/six-math-essentials.html) | ⭐ 203 | 💬 37 | [HN Thread](https://news.ycombinator.com/item?id=50446246) |
| **9** | [A Compendium of Abandoned Greenhouses](https://www.messynessychic.com/2015/01/15/a-compendium-of-abandoned-greenhouses/) | ⭐ 7 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50414657) |
| **10** | [Synaptics patent claims stop work on DisplayLink drivers](https://lwn.net/SubscriberLink/1102549/acbc92e00cee3a3f/) | ⭐ 358 | 💬 213 | [HN Thread](https://news.ycombinator.com/item?id=50443824) |

---

## 🗄️ News Archive

- 📅 [2026-11-11](archive/2026-11-11.md)
- 📅 [2026-11-10](archive/2026-11-10.md)
- 📅 [2026-11-09](archive/2026-11-09.md)
- 📅 [2026-11-08](archive/2026-11-08.md)
- 📅 [2026-11-07](archive/2026-11-07.md)
- 📅 [2026-11-06](archive/2026-11-06.md)
- 📅 [2026-11-05](archive/2026-11-05.md)
- 📅 [2026-11-04](archive/2026-11-04.md)
- 📅 [2026-11-03](archive/2026-11-03.md)
- 📅 [2026-11-02](archive/2026-11-02.md)
- 📅 [2026-10-31](archive/2026-10-31.md)
- 📅 [2026-10-30](archive/2026-10-30.md)
- 📅 [2026-10-28](archive/2026-10-28.md)
- 📅 [2026-10-27](archive/2026-10-27.md)

*... and [69 older editions in the archive folder](archive/)*

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
