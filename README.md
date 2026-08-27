# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Nvidia agrees to acquire Hugging Face for $13B](https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8) | ⭐ 982 | 💬 420 | [HN Thread](https://news.ycombinator.com/item?id=49458161) |
| **2** | [Mechanical Turk shutting down September 30](https://www.mturk.com/) | ⭐ 320 | 💬 87 | [HN Thread](https://news.ycombinator.com/item?id=49457545) |
| **3** | [GLM-5.3-Flash](https://z.ai/blog/glm-5.3-flash) | ⭐ 1009 | 💬 505 | [HN Thread](https://news.ycombinator.com/item?id=49449507) |
| **4** | [Asahi Linux Progress Report: Linux 7.2](https://asahilinux.org/2026/08/progress-report-7-2/) | ⭐ 252 | 💬 79 | [HN Thread](https://news.ycombinator.com/item?id=49456851) |
| **5** | [Tailcat – Like netcat, but over Tailscale’s data plane](https://github.com/tailscale/tailcat) | ⭐ 562 | 💬 99 | [HN Thread](https://news.ycombinator.com/item?id=49452990) |
| **6** | [CEO fired developers to make room for AI. Developers create open source AI CEO](https://github.com/SenteLabsAI/OpenExecutive) | ⭐ 521 | 💬 340 | [HN Thread](https://news.ycombinator.com/item?id=49458418) |
| **7** | [Worst-case glacial lake flood scenarios in a transboundary Himalayan basin 2022](https://nhess.copernicus.org/articles/22/3765/2022/nhess-22-3765-2022.html) | ⭐ 157 | 💬 70 | [HN Thread](https://news.ycombinator.com/item?id=49456929) |
| **8** | [U.S. State Department pauses immigrant visa applications](https://www.wsj.com/politics/policy/u-s-state-department-pauses-immigrant-visa-applications-25b31b23) | ⭐ 481 | 💬 716 | [HN Thread](https://news.ycombinator.com/item?id=49452709) |
| **9** | [An ongoing 3D-printer AGPL violation](https://lwn.net/SubscriberLink/1089390/46116614cc74b814/) | ⭐ 396 | 💬 177 | [HN Thread](https://news.ycombinator.com/item?id=49452980) |
| **10** | [Stripe acquires Clerky](https://www.clerky.com/blog/clerky-is-joining-stripe) | ⭐ 163 | 💬 26 | [HN Thread](https://news.ycombinator.com/item?id=49455956) |

---

## 🗄️ News Archive

- 📅 [2026-08-27](archive/2026-08-27.md)
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
