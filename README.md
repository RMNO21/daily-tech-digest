# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [A 10-year-old CNN outperforms frontier LLMs for skin cancer diagnosis](https://lynchlab.net/llm-skin-cancer) | ⭐ 96 | 💬 47 | [HN Thread](https://news.ycombinator.com/item?id=50233779) |
| **2** | [I refuse to accept a censored Internet. Join Me at FOSDEM 27](https://talkweb.eu/openweb/4558/) | ⭐ 99 | 💬 22 | [HN Thread](https://news.ycombinator.com/item?id=50233929) |
| **3** | [Oregon Police Are Charging a Local News Outlet $2.5M for Records About One Cop](https://theintercept.com/2026/10/01/oregon-police-misconduct-public-records-cost-fee/) | ⭐ 33 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=50234232) |
| **4** | [VCF Southwest 2026, but Edited on Silicon Graphics for '90s TV [video]](https://www.youtube.com/watch?v=46wxttvq9qY) | ⭐ 18 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=50223435) |
| **5** | [We should be more ambitious with the software we build](https://danluu.com/ambitious/) | ⭐ 652 | 💬 622 | [HN Thread](https://news.ycombinator.com/item?id=50225695) |
| **6** | [AI use leads UC Berkeley math professor to see 'no point' in grading homework](https://www.dailycal.org/news/campus/academics/ai-use-leads-uc-berkeley-math-professor-to-see-no-point-in-grading-homework/article_bdf1eae2-c08b-491f-b9f1-81a7cea177de.html) | ⭐ 56 | 💬 78 | [HN Thread](https://news.ycombinator.com/item?id=50233304) |
| **7** | [Active incident at Dreamhost forcing password reset](https://www.dreamhoststatus.com/) | ⭐ 37 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=50231166) |
| **8** | [Sabre Wulf Remastered](https://gp-64.com/swr/) | ⭐ 33 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=50233775) |
| **9** | [Show HN: I put employees inside S&P 500 market-cap bubbles](https://bigwhalehunting.com/workforce/) | ⭐ 133 | 💬 43 | [HN Thread](https://news.ycombinator.com/item?id=50232312) |
| **10** | [Cerebras Deploys Trillion-Parameter AI Models](https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras) | ⭐ 315 | 💬 112 | [HN Thread](https://news.ycombinator.com/item?id=50227356) |

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
