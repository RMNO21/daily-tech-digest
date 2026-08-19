# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [OpenLogi](https://openlogi.org/en) | ⭐ 536 | 💬 150 | [HN Thread](https://news.ycombinator.com/item?id=49355606) |
| **2** | [Where Human Sleep Went Wrong](https://nautil.us/where-human-sleep-went-wrong-1283797) | ⭐ 27 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=49358259) |
| **3** | [Cerebras CS-4](https://www.cerebras.ai/cs4) | ⭐ 255 | 💬 179 | [HN Thread](https://news.ycombinator.com/item?id=49354949) |
| **4** | [Palomar: A registry of Lean verified mathematics](https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics/) | ⭐ 93 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=49355968) |
| **5** | [Supersonic Trebuchet [video]](https://www.youtube.com/watch?v=Co57SfcT-h0) | ⭐ 88 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=49306207) |
| **6** | [Being ambitious and being a dad](https://nicholascharriere.com/blog/being-ambitious-and-being-a-dad/) | ⭐ 464 | 💬 273 | [HN Thread](https://news.ycombinator.com/item?id=49321298) |
| **7** | [Scientists stunned by children's lung recovery in ultra low emission zone](https://www.bbc.com/news/articles/c1l1r1zne1ro) | ⭐ 226 | 💬 163 | [HN Thread](https://news.ycombinator.com/item?id=49355105) |
| **8** | [A 3D fruit fly on macOS desktop powered by the real FlyWire connectome](https://github.com/DenisSergeevitch/desktop-fly) | ⭐ 260 | 💬 102 | [HN Thread](https://news.ycombinator.com/item?id=49353221) |
| **9** | [The Vietnam Binh Chau (Chau Tan) Late Tang Wreck](https://www.koh-antique.com/client/tangwreck/tangwreck.html) | ⭐ 36 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49355451) |
| **10** | [Solo – a .so loader for static Linux binaries](https://github.com/pg83/solo) | ⭐ 138 | 💬 135 | [HN Thread](https://news.ycombinator.com/item?id=49354613) |

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
