# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [GrapheneOS in 2027 available on high-end Motorola phones](https://grapheneos.social/@GrapheneOS/117078064184215730) | ⭐ 106 | 💬 23 | [HN Thread](https://news.ycombinator.com/item?id=49360242) |
| **2** | [OpenLogi](https://openlogi.org/en) | ⭐ 997 | 💬 275 | [HN Thread](https://news.ycombinator.com/item?id=49355606) |
| **3** | [Air Theremin – a browser theremin you play by waving at your webcam](https://theremin.bizibah.com/) | ⭐ 76 | 💬 39 | [HN Thread](https://news.ycombinator.com/item?id=49359425) |
| **4** | [Geolocating a random island using geometry and CUDA programming](https://yassa9.github.io/osint/gralhix-004/) | ⭐ 15 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49360545) |
| **5** | [Cerebras CS-4](https://www.cerebras.ai/cs4) | ⭐ 348 | 💬 214 | [HN Thread](https://news.ycombinator.com/item?id=49354949) |
| **6** | [Rings forged from meteorites may have been fashionable among ancient Greek elite](https://phys.org/news/2026-08-forged-meteorites-fashionable-ancient-greek.html) | ⭐ 32 | 💬 15 | [HN Thread](https://news.ycombinator.com/item?id=49298283) |
| **7** | [Being ambitious and being a dad](https://nicholascharriere.com/blog/being-ambitious-and-being-a-dad/) | ⭐ 649 | 💬 449 | [HN Thread](https://news.ycombinator.com/item?id=49321298) |
| **8** | [Supersonic Trebuchet [video]](https://www.youtube.com/watch?v=Co57SfcT-h0) | ⭐ 161 | 💬 66 | [HN Thread](https://news.ycombinator.com/item?id=49306207) |
| **9** | [Palomar: A registry of Lean verified mathematics](https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics/) | ⭐ 128 | 💬 26 | [HN Thread](https://news.ycombinator.com/item?id=49355968) |
| **10** | [A 3D fruit fly on macOS desktop powered by the real FlyWire connectome](https://github.com/DenisSergeevitch/desktop-fly) | ⭐ 316 | 💬 130 | [HN Thread](https://news.ycombinator.com/item?id=49353221) |

---

## 🗄️ News Archive

- 📅 [2026-08-19](archive/2026-08-19.md)
- 📅 [2026-08-18](archive/2026-08-18.md)
- 📅 [2026-08-17](archive/2026-08-17.md)
- 📅 [2026-08-16](archive/2026-08-16.md)
- 📅 [2026-08-15](archive/2026-08-15.md)
- 📅 [2026-08-14](archive/2026-08-14.md)

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
python scraper.py
```

---

<div align="center">
  <sub>Maintained by <a href="https://github.com/RMNO21">RMNO21</a> • Powered by GitHub Actions & Hacker News API</sub>
</div>
