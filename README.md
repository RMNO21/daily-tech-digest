# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Meta Ignores Brazilian Court Order to End Bolsonaro Favoritism](https://www.panamericandispatch.org/p/meta-ignores-brazilian-court-order) | ⭐ 67 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=50229587) |
| **2** | [We should be more ambitious with the software we build](https://danluu.com/ambitious/) | ⭐ 431 | 💬 367 | [HN Thread](https://news.ycombinator.com/item?id=50225695) |
| **3** | [Cerebras Deploys Trillion-Parameter AI Models](https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras) | ⭐ 161 | 💬 57 | [HN Thread](https://news.ycombinator.com/item?id=50227356) |
| **4** | [How Japanese Dried Bonito Is Made](https://kottke.org/26/10/how-japanese-dried-bonito-is-made) | ⭐ 38 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=50193936) |
| **5** | [The Goose Programming Language](https://aardappel.github.io/goose/) | ⭐ 395 | 💬 249 | [HN Thread](https://news.ycombinator.com/item?id=50224100) |
| **6** | [Online censorship is crushing indie webcomics](https://xtramagazine.com/culture/online-censorship-indie-webcomics-284463) | ⭐ 22 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50229599) |
| **7** | [Rewriting a Commercial Engine in Jai](https://polygonjs.com/blog/why-i-rewrote-polygon-from-scratch) | ⭐ 18 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=50194645) |
| **8** | [SpeedCrunch 1.1](https://www.speedcrunch.org/) | ⭐ 147 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=50224210) |
| **9** | [Small Programs and Languages](https://ratfactor.com/cards/pl-small) | ⭐ 109 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=50225674) |
| **10** | [Why Gopher in 2026?](https://gopher.muffinlabs.com/sdf.org/users/nervtoji/phlog/001.txt) | ⭐ 76 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=50226577) |

---

## 🗄️ News Archive

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
- 📅 [2026-10-10](archive/2026-10-10.md)

*... and [54 older editions in the archive folder](archive/)*

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
