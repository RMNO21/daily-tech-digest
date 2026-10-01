# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Clef: Open-source decision models, and new RL fine-tuning platform](https://blog.cloudflare.com/clef-decision-models/) | ⭐ 277 | 💬 105 | [HN Thread](https://news.ycombinator.com/item?id=49923692) |
| **2** | [RIP, vector database](https://turbopuffer.com/blog/rip-vector-database) | ⭐ 184 | 💬 51 | [HN Thread](https://news.ycombinator.com/item?id=49923466) |
| **3** | [Big Tech's Capex Is Half of Wall Street's Profit Growth](https://inlevel9.com/en/issues/half-the-growth-was-capex) | ⭐ 9 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49925836) |
| **4** | [StreetComplete on iOS is now in public beta](https://github.com/streetcomplete/StreetComplete/issues/5421) | ⭐ 441 | 💬 101 | [HN Thread](https://news.ycombinator.com/item?id=49920160) |
| **5** | [Bez: Generating a browser engine from specs and tests](https://tangled.org/burrito.space/bez) | ⭐ 28 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49925036) |
| **6** | [Ask HN: Who is hiring? (October 2026)](https://news.ycombinator.com/item?id=49922569) | ⭐ 90 | 💬 93 | [HN Thread](https://news.ycombinator.com/item?id=49922569) |
| **7** | [RacketCon Is Saturday](https://con.racket-lang.org/) | ⭐ 98 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=49922515) |
| **8** | [Oxygen-deprived underwater zones may not be "dead zones" but clue to early life](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2026AV002570) | ⭐ 7 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49925742) |
| **9** | [Show HN: Open-source model routing for coding agents at Astra-level performance](https://news.ycombinator.com/item?id=49911500) | ⭐ 36 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49911500) |
| **10** | [Cloudflare K2: serverless event streams](https://blog.cloudflare.com/cloudflare-k2-streams/) | ⭐ 125 | 💬 44 | [HN Thread](https://news.ycombinator.com/item?id=49921923) |

---

## 🗄️ News Archive

- 📅 [2026-10-01](archive/2026-10-01.md)
- 📅 [2026-09-30](archive/2026-09-30.md)
- 📅 [2026-09-29](archive/2026-09-29.md)
- 📅 [2026-09-28](archive/2026-09-28.md)
- 📅 [2026-09-27](archive/2026-09-27.md)
- 📅 [2026-09-26](archive/2026-09-26.md)
- 📅 [2026-09-25](archive/2026-09-25.md)
- 📅 [2026-09-24](archive/2026-09-24.md)
- 📅 [2026-09-22](archive/2026-09-22.md)
- 📅 [2026-09-21](archive/2026-09-21.md)
- 📅 [2026-09-20](archive/2026-09-20.md)
- 📅 [2026-09-19](archive/2026-09-19.md)
- 📅 [2026-09-18](archive/2026-09-18.md)
- 📅 [2026-09-16](archive/2026-09-16.md)

*... and [33 older editions in the archive folder](archive/)*

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
