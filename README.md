# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Amazon saves millions by replacing Sonnet 4.6 with Strands Decider](https://strandsagents.com/blog/amazon-saves-millions-replacing-sonnet-with-strands-decider/) | ⭐ 273 | 💬 87 | [HN Thread](https://news.ycombinator.com/item?id=50436640) |
| **2** | [Claude Fable 5.2 and Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2) | ⭐ 585 | 💬 800 | [HN Thread](https://news.ycombinator.com/item?id=50429068) |
| **3** | [Queens Public library under ransomware attack e-borrowing suspended](https://connect.queenslibrary.org/) | ⭐ 15 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=50437790) |
| **4** | [USPS now offers official ZIP Code boundary polygons](https://postalpro.usps.com/zcb) | ⭐ 620 | 💬 317 | [HN Thread](https://news.ycombinator.com/item?id=50431058) |
| **5** | [Your TV can see through walls](https://maurycyz.com/projects/fading/) | ⭐ 107 | 💬 39 | [HN Thread](https://news.ycombinator.com/item?id=50436410) |
| **6** | [Fireworks AI security breach impacts Notion and their customers](https://www.notion.com/help/security-incident-involving-a-third-party-ai-vendor) | ⭐ 30 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=50437106) |
| **7** | [Locating the source of a mysterious beep](https://simonwillison.net/2026/Nov/9/mysterious-beeps/) | ⭐ 188 | 💬 84 | [HN Thread](https://news.ycombinator.com/item?id=50434310) |
| **8** | [Payments Canada announces launch of Canada's Real-Time Rail (RTR) payment system](https://www.payments.ca/canada-launches-real-time-rail-bringing-247-payment-infrastructure-national-economy) | ⭐ 532 | 💬 286 | [HN Thread](https://news.ycombinator.com/item?id=50427362) |
| **9** | [E-means: Outperforming k-means in one-tenth the epochs](https://e-means.github.io/) | ⭐ 402 | 💬 37 | [HN Thread](https://news.ycombinator.com/item?id=50429734) |
| **10** | [Foldable Flight: The Best Paper Airplanes](https://www.foldableflight.com) | ⭐ 1021 | 💬 151 | [HN Thread](https://news.ycombinator.com/item?id=50424581) |

---

## 🗄️ News Archive

- 📅 [2026-11-10](archive/2026-11-10.md)
- 📅 [2026-11-09](archive/2026-11-09.md)
- 📅 [2026-11-08](archive/2026-11-08.md)
- 📅 [2026-11-07](archive/2026-11-07.md)
- 📅 [2026-11-06](archive/2026-11-06.md)
- 📅 [2026-11-05](archive/2026-11-05.md)
- 📅 [2026-11-04](archive/2026-11-04.md)
- 📅 [2026-11-03](archive/2026-11-03.md)
- 📅 [2026-11-02](archive/2026-11-02.md)
- 📅 [2026-10-31](archive/2026-10-31.md)
- 📅 [2026-10-30](archive/2026-10-30.md)
- 📅 [2026-10-28](archive/2026-10-28.md)
- 📅 [2026-10-27](archive/2026-10-27.md)
- 📅 [2026-10-26](archive/2026-10-26.md)

*... and [68 older editions in the archive folder](archive/)*

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
