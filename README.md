# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [GLM-5.3-Flash](https://z.ai/blog/glm-5.3-flash) | ⭐ 418 | 💬 171 | [HN Thread](https://news.ycombinator.com/item?id=49449507) |
| **2** | [AWS Acquires DuckDB](https://ducklabs.com/news/2026/08/26/ducklabs-to-join-aws) | ⭐ 669 | 💬 181 | [HN Thread](https://news.ycombinator.com/item?id=49448321) |
| **3** | [Qwen3.8-Flash-Next: A New Architecture, Towards Ultimate Cost-Efficiency](https://qwen.ai/blog?id=qwen3.8-flash-next) | ⭐ 388 | 💬 115 | [HN Thread](https://news.ycombinator.com/item?id=49448210) |
| **4** | [Nebula Sans](https://www.nebulasans.com) | ⭐ 112 | 💬 52 | [HN Thread](https://news.ycombinator.com/item?id=49450448) |
| **5** | [France reaches 94.9% fiber coverage in 2026](https://cartefibre.arcep.fr) | ⭐ 145 | 💬 85 | [HN Thread](https://news.ycombinator.com/item?id=49448872) |
| **6** | [Disruption with Some GitHub Services](https://www.githubstatus.com/incidents/hcbtzksccj2f) | ⭐ 111 | 💬 62 | [HN Thread](https://news.ycombinator.com/item?id=49450722) |
| **7** | [GLM-5.3-Flash Intelligence, Performance and Price Analysis](https://artificialanalysis.ai/models/glm-5-3-flash) | ⭐ 83 | 💬 18 | [HN Thread](https://news.ycombinator.com/item?id=49450353) |
| **8** | [Taylor Farms: How One Company's Reach Became a National Risk](https://farmaction.us/taylorfarmsreport/) | ⭐ 88 | 💬 51 | [HN Thread](https://news.ycombinator.com/item?id=49449749) |
| **9** | [Launch HN: Risklytics (YC S26) – Insurance brokerage for frontier tech companies](https://www.risklytics.ai/) | ⭐ 5 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49451495) |
| **10** | [It's so hard to finish an idea that is not yours (and suggested by AI)](https://www.ssp.sh/brain/using-obsidian-with-ai/) | ⭐ 32 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=49450898) |

---

## 🗄️ News Archive

- 📅 [2026-08-26](archive/2026-08-26.md)
- 📅 [2026-08-25](archive/2026-08-25.md)
- 📅 [2026-08-24](archive/2026-08-24.md)
- 📅 [2026-08-23](archive/2026-08-23.md)
- 📅 [2026-08-22](archive/2026-08-22.md)
- 📅 [2026-08-21](archive/2026-08-21.md)
- 📅 [2026-08-20](archive/2026-08-20.md)
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
