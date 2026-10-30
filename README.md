# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [My favourite PowerMac is a Nintendo Wii](https://virtuallyfun.com/2026/10/29/my-favourite-powermac-is-a-nintendo-wii/) | ⭐ 100 | 💬 19 | [HN Thread](https://news.ycombinator.com/item?id=50307190) |
| **2** | [GitHub Incident with Actions, Pages, and Webhooks](https://www.githubstatus.com/incidents/pwxsjgnvrk6b) | ⭐ 96 | 💬 35 | [HN Thread](https://news.ycombinator.com/item?id=50307723) |
| **3** | [Northflank Breached](https://status.northflank.com) | ⭐ 226 | 💬 137 | [HN Thread](https://news.ycombinator.com/item?id=50305025) |
| **4** | [A Working Nintendo in ~1GB of Qwen Weights](https://github.com/dbreunig/nesformer) | ⭐ 104 | 💬 83 | [HN Thread](https://news.ycombinator.com/item?id=50306442) |
| **5** | [Backdoor in Claude Code for VS Code extension on the Cursor Marketplace](https://phorion.io/blog/offical-claude-code-vsx-compromise/) | ⭐ 547 | 💬 396 | [HN Thread](https://news.ycombinator.com/item?id=50300683) |
| **6** | [Florilegium: Procedural Flowers in LaTeX](https://github.com/kevinraymond/florilegium) | ⭐ 106 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=50305637) |
| **7** | [Breaking the open web won't stop the bad bots](https://www.techpolicy.press/breaking-the-open-web-wont-stop-the-bad-bots/) | ⭐ 72 | 💬 26 | [HN Thread](https://news.ycombinator.com/item?id=50263837) |
| **8** | [The federated code forge](https://tangled.org/blog/forge/) | ⭐ 129 | 💬 48 | [HN Thread](https://news.ycombinator.com/item?id=50305573) |
| **9** | [Anthropic may not secure investment-grade rating after IPO, Blackstone says](https://www.ft.com/content/59383c7f-8d82-493f-bf01-d2e862a1018f) | ⭐ 112 | 💬 37 | [HN Thread](https://news.ycombinator.com/item?id=50307219) |
| **10** | [AI isn't replacing SREs, it's deskilling them](https://newsletter.signoz.io/p/ai-isnt-replacing-sres-its-deskilling) | ⭐ 338 | 💬 259 | [HN Thread](https://news.ycombinator.com/item?id=50305693) |

---

## 🗄️ News Archive

- 📅 [2026-10-30](archive/2026-10-30.md)
- 📅 [2026-10-28](archive/2026-10-28.md)
- 📅 [2026-10-27](archive/2026-10-27.md)
- 📅 [2026-10-26](archive/2026-10-26.md)
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

*... and [58 older editions in the archive folder](archive/)*

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
