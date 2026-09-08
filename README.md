# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [I've factored the RSA keys of a Certificate Authority from the 90s](https://mcpherrin.ca/2026/09/07/rsa.html) | ⭐ 180 | 💬 33 | [HN Thread](https://news.ycombinator.com/item?id=49604637) |
| **2** | [TALA Is Open-Source](https://d2lang.com/blog/tala-is-open-source/) | ⭐ 136 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=49604150) |
| **3** | [Arm Mali G2-Ultra NX GPU: desktop-class mobile gameplay with AI-native graphics](https://newsroom.arm.com/blog/arm-mali-g2-ultra-nx-ai-native-mobile-graphics) | ⭐ 7 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49605511) |
| **4** | [How well do agents use test/verification techniques?](https://danluu.com/agentic-testing/) | ⭐ 15 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49605246) |
| **5** | [Jellyfin 12.0](https://jellyfin.org/posts/jellyfin-release-12.0/) | ⭐ 179 | 💬 72 | [HN Thread](https://news.ycombinator.com/item?id=49604861) |
| **6** | [Watch Los Angeles get built, one building at a time (1880–2026)](https://lax-skyline.parcelscope.net/) | ⭐ 252 | 💬 131 | [HN Thread](https://news.ycombinator.com/item?id=49601655) |
| **7** | [John Margolies' photographs of roadside America](https://publicdomainreview.org/collection/john-margolies-photographs-of-roadside-america/) | ⭐ 53 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=49560682) |
| **8** | [Leaving VMware just got harder after Broadcom pulled VDDK downloads](https://www.virtualizationhowto.com/2026/09/leaving-vmware-just-got-harder-after-broadcom-pulled-vddk-downloads/) | ⭐ 141 | 💬 59 | [HN Thread](https://news.ycombinator.com/item?id=49602699) |
| **9** | [WeatherNext 3](https://deepmind.google/science/weathernext/) | ⭐ 278 | 💬 65 | [HN Thread](https://news.ycombinator.com/item?id=49552299) |
| **10** | [Scientists observe Einstein's gravity in the quantum world](https://www.ox.ac.uk/news/2026-08-28-scientists-observe-einsteins-gravity-in-the-quantum-world) | ⭐ 181 | 💬 44 | [HN Thread](https://news.ycombinator.com/item?id=49569838) |

---

## 🗄️ News Archive

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
- 📅 [2026-08-26](archive/2026-08-26.md)

*... and [12 older editions in the archive folder](archive/)*

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
