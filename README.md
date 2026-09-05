# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Private German rocket makes history, reaches orbit from European soil](https://www.space.com/space-exploration/launches-spacecraft/isar-aerospace-second-launch-norway-andoya-spaceport-spectrum-rocket) | ⭐ 293 | 💬 147 | [HN Thread](https://news.ycombinator.com/item?id=49580369) |
| **2** | [Falsehoods Programmers Believe About LANs](https://dreamstation.systems/personal/lanfalsehoods.html) | ⭐ 42 | 💬 34 | [HN Thread](https://news.ycombinator.com/item?id=49581179) |
| **3** | [Finite time blowup for an averaged three-dimensional Navier-Stokes equation (2014)](https://terrytao.wordpress.com/2014/02/04/finite-time-blowup-for-an-averaged-three-dimensional-navier-stokes-equation/) | ⭐ 51 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=49580329) |
| **4** | [Learn Programming with OCaml](https://usr.lmf.cnrs.fr/lpo/) | ⭐ 148 | 💬 67 | [HN Thread](https://news.ycombinator.com/item?id=49578280) |
| **5** | [OKF Agent Memory – Git-native persistent memory for AI coding agents](https://github.com/okf-memory/okf-agent-memory) | ⭐ 10 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49581240) |
| **6** | [The "$60 Gaming PC" – AMD BC-250 (2025)](https://devquasar.com/hardware/the-60-gaming-pc-amd-bc-250/) | ⭐ 261 | 💬 78 | [HN Thread](https://news.ycombinator.com/item?id=49576386) |
| **7** | [Show HN: Fly By – retro biplane flying game](https://michaelteter.com/flyby.html) | ⭐ 28 | 💬 23 | [HN Thread](https://news.ycombinator.com/item?id=49519101) |
| **8** | [How Swiss tables work in Go built-in map](https://victoriametrics.com/blog/go-swiss-table-map/index.html) | ⭐ 27 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49548852) |
| **9** | [Visualizing Rust's Vtables: How dyn Trait Works In Memory](https://sofiabelen.github.io/projects/visualizing-rusts-vtables-how-dyn-trait-works-in-memory/) | ⭐ 121 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=49576343) |
| **10** | [Balrogg: Demonically compacting (up to 15%) lossless Vorbis/Opus recompressor](https://github.com/iczelia/balrogg) | ⭐ 49 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=49549778) |

---

## 🗄️ News Archive

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
- 📅 [2026-08-25](archive/2026-08-25.md)
- 📅 [2026-08-24](archive/2026-08-24.md)
- 📅 [2026-08-23](archive/2026-08-23.md)

*... and [9 older editions in the archive folder](archive/)*

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
