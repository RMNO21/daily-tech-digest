# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Muse Spark Open](https://research.meta.ai/blog/muse-spark-open) | ⭐ 766 | 💬 389 | [HN Thread](https://news.ycombinator.com/item?id=50107379) |
| **2** | [Meta’s new commercial terms will allow the scraping of news sites: experts](https://www.niemanlab.org/2026/10/metas-new-commercial-terms-will-allow-the-scraping-of-news-sites-legal-experts-say/) | ⭐ 199 | 💬 77 | [HN Thread](https://news.ycombinator.com/item?id=50111852) |
| **3** | ['500-hour' Order of the Sinking Star is as complex and exhausting as it sounds](https://www.polygon.com/order-of-the-sinking-star-impressions/) | ⭐ 100 | 💬 48 | [HN Thread](https://news.ycombinator.com/item?id=50072119) |
| **4** | [RPKI now protects 70% of internet routes](https://ipinfo.io/blog/rpki-protects-70-internet-routes) | ⭐ 118 | 💬 35 | [HN Thread](https://news.ycombinator.com/item?id=50112330) |
| **5** | [Neural networks are clean](https://already-clean.goodfire.com/) | ⭐ 635 | 💬 232 | [HN Thread](https://news.ycombinator.com/item?id=50105647) |
| **6** | [What I self-host](https://viceconsole.fyi/blog/2026/10/10/what-i-self-host/) | ⭐ 424 | 💬 265 | [HN Thread](https://news.ycombinator.com/item?id=50109715) |
| **7** | [Woman who rescued injured crow keeps getting 'thank-you gifts' from birds [video]](https://www.youtube.com/watch?v=sjNpfz4UzqU) | ⭐ 145 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=50065859) |
| **8** | [Wayland desktop for Linux with skeuomorphic design](https://github.com/fyzugx/DEsk) | ⭐ 581 | 💬 229 | [HN Thread](https://news.ycombinator.com/item?id=50103338) |
| **9** | [New Withings Users Must Pay $99/Year for Apple Health Syncing](https://support.withings.com/hc/en-us/community/posts/51887047154577-Unacceptable-Apple-Health-Sync-is-now-behind-a-99-year-paywall-for-new-accounts) | ⭐ 247 | 💬 164 | [HN Thread](https://news.ycombinator.com/item?id=50109375) |
| **10** | [Any window from your Mac, on your iPhone and iPad](https://github.com/Saffsanity/sill) | ⭐ 126 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=50112739) |

---

## 🗄️ News Archive

- 📅 [2026-10-16](archive/2026-10-16.md)
- 📅 [2026-10-15](archive/2026-10-15.md)
- 📅 [2026-10-14](archive/2026-10-14.md)
- 📅 [2026-10-13](archive/2026-10-13.md)
- 📅 [2026-10-10](archive/2026-10-10.md)
- 📅 [2026-10-09](archive/2026-10-09.md)
- 📅 [2026-10-08](archive/2026-10-08.md)
- 📅 [2026-10-07](archive/2026-10-07.md)
- 📅 [2026-10-05](archive/2026-10-05.md)
- 📅 [2026-10-04](archive/2026-10-04.md)
- 📅 [2026-10-03](archive/2026-10-03.md)
- 📅 [2026-10-02](archive/2026-10-02.md)
- 📅 [2026-10-01](archive/2026-10-01.md)
- 📅 [2026-09-30](archive/2026-09-30.md)

*... and [45 older editions in the archive folder](archive/)*

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
