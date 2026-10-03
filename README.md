# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [The Escalation of War in Ethiopia](https://www.africanistperspective.com/p/on-the-escalation-of-war-in-ethiopia) | ⭐ 15 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49943451) |
| **2** | [Show HN: Germany's new sovereign AI model Kolibri](https://tej.as/blog/aleph-alpha-kolibri) | ⭐ 48 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=49943034) |
| **3** | [Newgrounds.com – A community of games, music, and art](https://www.newgrounds.com/) | ⭐ 304 | 💬 84 | [HN Thread](https://news.ycombinator.com/item?id=49940394) |
| **4** | [C++ Insights – See your source code with the eyes of a Compiler](https://github.com/andreasfertig/cppinsights) | ⭐ 16 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49928361) |
| **5** | [Court agrees with EFF: Utah's VPN law demands a technical impossibility](https://www.eff.org/deeplinks/2026/10/court-agrees-eff-utahs-vpn-law-demands-technical-impossibility) | ⭐ 687 | 💬 326 | [HN Thread](https://news.ycombinator.com/item?id=49927754) |
| **6** | [Apple Pass Designer](https://developer.apple.com/pass-designer/) | ⭐ 466 | 💬 287 | [HN Thread](https://news.ycombinator.com/item?id=49937276) |
| **7** | [Mike Tomlin spent 12 years building a Minecraft city](https://www.nytimes.com/athletic/7648198/2026/10/01/mike-tomlin-minecraft-nfl-coach/) | ⭐ 527 | 💬 121 | [HN Thread](https://news.ycombinator.com/item?id=49925184) |
| **8** | [Show HN: Offrun – manage every coding agent from one workspace](https://offrun.dev/) | ⭐ 20 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=49942434) |
| **9** | [Great Question (YC W21) Is Hiring Product Engineers in Canada (Remote)](https://www.ycombinator.com/companies/great-question/jobs/agEqBYD-product-engineer-ai-full-stack) | ⭐ 1 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49943524) |
| **10** | [Cloudflare OHTTP gateway](https://blog.cloudflare.com/announcing-cloudflare-ohttp-gateway/) | ⭐ 112 | 💬 39 | [HN Thread](https://news.ycombinator.com/item?id=49941091) |

---

## 🗄️ News Archive

- 📅 [2026-10-03](archive/2026-10-03.md)
- 📅 [2026-10-02](archive/2026-10-02.md)
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

*... and [35 older editions in the archive folder](archive/)*

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
