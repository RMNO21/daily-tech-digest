# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Everything I own, owned](https://schlarp.com/posts/everything-i-own-owned/) | ⭐ 474 | 💬 144 | [HN Thread](https://news.ycombinator.com/item?id=49413320) |
| **2** | [How I find problems to solve as a staff engineer](https://lalitm.com/post/find-problems-staff-engineer/) | ⭐ 336 | 💬 118 | [HN Thread](https://news.ycombinator.com/item?id=49411643) |
| **3** | [Anthropic's best AI model struggles to attract users as cheaper tools thrive](https://www.ft.com/content/5ee49718-c258-4f01-aa32-7e5b76ae5245) | ⭐ 336 | 💬 286 | [HN Thread](https://news.ycombinator.com/item?id=49411102) |
| **4** | [Migrating a Synology NAS to a UniFi UNAS Pro 8 with Robocopy, SMB Multichannel](https://www.hanselman.com/blog/migrating-a-synology-nas-to-a-unifi-unas-pro-8-with-robocopy-smb-multichannel-and-surprising-performance-traps) | ⭐ 26 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=49414338) |
| **5** | [Google Workspace thinks my domain is an email provider (2025)](https://blog.elis.cc/articles/google-workspace-thinks-my-domain-is-an-email-provider/) | ⭐ 219 | 💬 62 | [HN Thread](https://news.ycombinator.com/item?id=49411717) |
| **6** | [My agent.md to improve LLM-assisted code quality](https://fabiensanglard.net/agent.md/index.html) | ⭐ 223 | 💬 94 | [HN Thread](https://news.ycombinator.com/item?id=49410932) |
| **7** | [Nearly 3M Teslas recalled in China over hidden door handles](https://www.bbc.com/news/articles/c4g6ggdg030o) | ⭐ 14 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49415187) |
| **8** | [I built a low-latency AI companion that plays Skyrim with me](https://pantel.is/projects/ai-gaming-companion/) | ⭐ 37 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49413561) |
| **9** | [What Is a Harness?](https://earendil.com/posts/what-is-a-harness/) | ⭐ 364 | 💬 142 | [HN Thread](https://news.ycombinator.com/item?id=49409092) |
| **10** | [How Complex Systems Fail (1998)](https://how.complexsystems.fail/) | ⭐ 273 | 💬 66 | [HN Thread](https://news.ycombinator.com/item?id=49409473) |

---

## 🗄️ News Archive

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
