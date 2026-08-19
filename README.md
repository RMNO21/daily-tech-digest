# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Civic Hygiene – avoid building technologies that could be used by a police state](https://shkspr.mobi/blog/2013/11/civic-hygiene/) | ⭐ 76 | 💬 22 | [HN Thread](https://news.ycombinator.com/item?id=49363433) |
| **2** | [Geolocating a random island using geometry and CUDA programming](https://yassa9.github.io/osint/gralhix-004/) | ⭐ 226 | 💬 46 | [HN Thread](https://news.ycombinator.com/item?id=49360545) |
| **3** | [A joke domain purchase turned in geopolitical warfare](https://sprocketfox.io/xssfox/2026/08/19/sondehub-and-war/) | ⭐ 300 | 💬 40 | [HN Thread](https://news.ycombinator.com/item?id=49360015) |
| **4** | [OpenLogi](https://openlogi.org/en) | ⭐ 1284 | 💬 355 | [HN Thread](https://news.ycombinator.com/item?id=49355606) |
| **5** | [PostgreSQL for Everything](https://www.raphaelbauer.com:443/posts/postgresql-everything/) | ⭐ 151 | 💬 103 | [HN Thread](https://news.ycombinator.com/item?id=49361279) |
| **6** | [Microgpt in pure C hits 10M tps on Apple m5](https://github.com/vixhal-baraiya/microgpt-c) | ⭐ 42 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49347477) |
| **7** | [Devices with GrapheneOS support should be available in 2027](https://grapheneos.social/@GrapheneOS/117078064184215730) | ⭐ 443 | 💬 265 | [HN Thread](https://news.ycombinator.com/item?id=49360242) |
| **8** | [Moderna reports first positive Phase 3 for mRNA neoantigen therapy in melanoma](https://twitter.com/NoubarAfeyan/status/2090050162441752787) | ⭐ 257 | 💬 106 | [HN Thread](https://news.ycombinator.com/item?id=49361395) |
| **9** | [Launch HN: OneCLI (YC S26) – OSS sandboxed agent harness for teams](https://github.com/onecli/onecli) | ⭐ 3 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49363710) |
| **10** | [Ornith-1.5: From Self-Scaffolding to Self-Improvement](https://ornith.ai/ornith_1_5.html) | ⭐ 21 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49362401) |

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
