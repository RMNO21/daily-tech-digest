# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Using the railway network as a flatbed scanner](https://philo.gay/linecam/) | ⭐ 226 | 💬 39 | [HN Thread](https://news.ycombinator.com/item?id=49344825) |
| **2** | [Fixing a Bricked Framework Laptop](https://quantum5.ca/2026/08/16/fixing-bricked-amd-7040-series-framework-13-laptop-with-20-tools/) | ⭐ 170 | 💬 88 | [HN Thread](https://news.ycombinator.com/item?id=49345220) |
| **3** | [The Amazon Tax](https://seths.blog/2026/08/the-amazon-tax/) | ⭐ 369 | 💬 267 | [HN Thread](https://news.ycombinator.com/item?id=49345263) |
| **4** | [How I Under-Engineered My Book](https://chriskiehl.com/article/how-i-under-engineered-my-book) | ⭐ 34 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49336392) |
| **5** | [Apple announces changes for apps in the European Union](https://www.apple.com/newsroom/2026/08/apple-announces-changes-for-apps-in-the-european-union/) | ⭐ 12 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49348055) |
| **6** | [Linux 7.3 improves performance when running out of vRAM](https://pixelcluster.dev/VRAM-Overcommit/) | ⭐ 394 | 💬 158 | [HN Thread](https://news.ycombinator.com/item?id=49342719) |
| **7** | [Python Polars Cheatsheet (based on our O'Reilly book)](https://opensource.posit.co/resources/cheatsheets/polars/) | ⭐ 66 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=49345476) |
| **8** | [Claude: Degraded Performance for Multiple Models](https://status.claude.com/incidents/q7txxvbsftgq) | ⭐ 5 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49348163) |
| **9** | [Launch HN: machine0 (YC S26) – Persistent CPU and GPU VMs from the CLI](https://machine0.io) | ⭐ 3 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49348136) |
| **10** | [Teaching my kid to code with a modern MUD](https://tau.dev/2026/08/07/canon) | ⭐ 139 | 💬 45 | [HN Thread](https://news.ycombinator.com/item?id=49272631) |

---

## 🗄️ News Archive

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
