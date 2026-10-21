# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [PHP 8.2.35](https://github.com/php/php-src/releases/tag/php-8.2.35) | ⭐ 832 | 💬 469 | [HN Thread](https://news.ycombinator.com/item?id=50180873) |
| **2** | [Today's PHP security release, and how we're strengthening security](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/) | ⭐ 294 | 💬 151 | [HN Thread](https://news.ycombinator.com/item?id=50182987) |
| **3** | [Compromised LiteLLM 1.107.0 on PyPI Installs a Credential Stealer and Backdoor](https://safedep.io/litellm-pypi-compromise-credential-stealer-backdoor/) | ⭐ 231 | 💬 90 | [HN Thread](https://news.ycombinator.com/item?id=50181114) |
| **4** | [Eight Bits of Trust; eMudhra's CA keys cracked in milliseconds](https://scotthelme.co.uk/eight-bits-of-trust-emudhras-ca-keys-cracked-in-milliseconds/) | ⭐ 685 | 💬 323 | [HN Thread](https://news.ycombinator.com/item?id=50177916) |
| **5** | [DuckDB 2.0.0 LTS “Cinnamon Teal”](https://duckdb.org/2026/10/21/announcing-duckdb-200) | ⭐ 258 | 💬 29 | [HN Thread](https://news.ycombinator.com/item?id=50181136) |
| **6** | [Patch the Planet: global response coordination as agents uncover vulnerabilities](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/) | ⭐ 170 | 💬 101 | [HN Thread](https://news.ycombinator.com/item?id=50181175) |
| **7** | [Tiny possum and glider thought extinct for 6000 years found in remote West Papua](https://www.bbc.com/news/articles/cp814l80pw2o) | ⭐ 71 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=50162044) |
| **8** | [EA is shutting down BioWare](https://www.theverge.com/games/1015647/ea-is-shutting-down-bioware) | ⭐ 125 | 💬 56 | [HN Thread](https://news.ycombinator.com/item?id=50184586) |
| **9** | [OpenAI models are coming to Google Cloud](https://openai.com/index/openai-models-google-cloud/) | ⭐ 119 | 💬 35 | [HN Thread](https://news.ycombinator.com/item?id=50180079) |
| **10** | [Oregon lawmakers approve money to buy an iconic waterfall listed on Redfin](https://apnews.com/article/oregon-waterfall-for-sale-lawmakers-996de63462d49ec3ad9bee1629fb9488) | ⭐ 98 | 💬 61 | [HN Thread](https://news.ycombinator.com/item?id=50182526) |

---

## 🗄️ News Archive

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
- 📅 [2026-10-09](archive/2026-10-09.md)
- 📅 [2026-10-08](archive/2026-10-08.md)
- 📅 [2026-10-07](archive/2026-10-07.md)
- 📅 [2026-10-05](archive/2026-10-05.md)

*... and [50 older editions in the archive folder](archive/)*

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
