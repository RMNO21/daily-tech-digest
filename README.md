# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Payments Canada announces launch of Canada's Real-Time Rail (RTR) payment system](https://www.payments.ca/canada-launches-real-time-rail-bringing-247-payment-infrastructure-national-economy) | ⭐ 251 | 💬 149 | [HN Thread](https://news.ycombinator.com/item?id=50427362) |
| **2** | [Too many men suffering in silence, national health report finds (Canada)](https://www.westcentralonline.com/articles/too-many-men-suffering-in-silence-national-health-report-finds) | ⭐ 19 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=50429475) |
| **3** | [Our Smallest, Most Efficient Model: Muse Ember](https://research.meta.ai/blog/muse-ember) | ⭐ 31 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=50429024) |
| **4** | [Fold Epic Paper Airplanes](https://www.foldableflight.com) | ⭐ 603 | 💬 96 | [HN Thread](https://news.ycombinator.com/item?id=50424581) |
| **5** | [Magenta solar panels may be agrivoltaics' cleverest trick yet](https://www.anthropocenemagazine.org/2026/10/magenta-solar-panels-may-be-agrivoltaics-cleverest-trick-yet/) | ⭐ 140 | 💬 54 | [HN Thread](https://news.ycombinator.com/item?id=50426175) |
| **6** | [Infineon marks innovation milestone with 300mm power silicon carbide wafer](https://www.infineon.com/press-release/2026/infpr202611-028) | ⭐ 11 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50429430) |
| **7** | [When will this stop? The Raspberry Pi 5 16GB SBC now sells for $385](https://www.cnx-software.com/2026/11/03/when-will-this-stop-the-raspberry-pi-5-16gb-sbc-now-sells-for-385/) | ⭐ 113 | 💬 82 | [HN Thread](https://news.ycombinator.com/item?id=50428801) |
| **8** | [Show HN: DBDelve – Open-Source DB Client Made with Rust and GPUI](https://news.ycombinator.com/item?id=50427934) | ⭐ 39 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=50427934) |
| **9** | [Show HN: MeowDisplay Is iPhone Mirroring, but in Reverse](https://meowdisplay.app/) | ⭐ 5 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=50429636) |
| **10** | [Y/N (YC S23) is hiring a growth lead to distribute superhuman A.I. storytelling](https://www.ycombinator.com/companies/yn/jobs/TjDn3YZ-founding-growth-marketer) | ⭐ 1 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50428266) |

---

## 🗄️ News Archive

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
- 📅 [2026-10-25](archive/2026-10-25.md)

*... and [67 older editions in the archive folder](archive/)*

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
