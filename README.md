# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Goldman Sachs Is Pulling Claude Code from Its Bankers and Traders](https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers) | ⭐ 292 | 💬 176 | [HN Thread](https://news.ycombinator.com/item?id=50415628) |
| **2** | [Dux: Free, open-source Wayland desktop shell with file manager and theming](https://duxlabs.dev/) | ⭐ 46 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=50416053) |
| **3** | [How I Fight AI Brain Fry](https://sergeykuhne.com/blog/fighting-ai-brain-fry) | ⭐ 24 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=50416363) |
| **4** | [Outlook.com Is Quietly Rejecting Email from Domains Without DMARC](https://mailroute.net/blog/outlook-rejecting-email-without-dmarc) | ⭐ 61 | 💬 42 | [HN Thread](https://news.ycombinator.com/item?id=50416158) |
| **5** | [Declarative Dragging](https://declarative-dragging.github.io/) | ⭐ 92 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=50368481) |
| **6** | [Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU](https://github.com/synchopate/llama-modchip) | ⭐ 292 | 💬 104 | [HN Thread](https://news.ycombinator.com/item?id=50411961) |
| **7** | [RAM Altman: Linux Script Emails Sam Altman Daily How Much Unused RAM in Your PC](https://respawnfirst.com/linux-script-emails-sam-altman-unused-ram-ram-altman/) | ⭐ 66 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=50415172) |
| **8** | [Writing as a thinking tool](http://muratbuffalo.blogspot.com/2026/11/writing-as-thinking-tool.html) | ⭐ 205 | 💬 71 | [HN Thread](https://news.ycombinator.com/item?id=50412067) |
| **9** | [A Little Snitch for Windows](https://packethound.app/) | ⭐ 50 | 💬 26 | [HN Thread](https://news.ycombinator.com/item?id=50415135) |
| **10** | [The Reconstruction of Torn Documents](https://www.bundesarchiv.de/en/stasi-records-archive/the-reconstruction-of-torn-documents/) | ⭐ 68 | 💬 42 | [HN Thread](https://news.ycombinator.com/item?id=50389923) |

---

## 🗄️ News Archive

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
- 📅 [2026-10-24](archive/2026-10-24.md)

*... and [66 older editions in the archive folder](archive/)*

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
