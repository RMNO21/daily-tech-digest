# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Claude Fable 5.1 and Claude Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1) | ⭐ 990 | 💬 929 | [HN Thread](https://news.ycombinator.com/item?id=49525378) |
| **2** | [How accurate have Ed Zitron's AI skeptic predictions been?](https://danluu.com/zitron/) | ⭐ 494 | 💬 570 | [HN Thread](https://news.ycombinator.com/item?id=49526069) |
| **3** | [The efficient frontier of LLM inference](https://www.baseten.co/blog/the-efficient-frontier-of-llm-inference/) | ⭐ 59 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=49529898) |
| **4** | [Show HN: Weedout – Safari extension that hides YouTube AI-labeled videos](https://masteranza.github.io/weedout/) | ⭐ 80 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=49528895) |
| **5** | [My local model setup on an M4 Pro Mac Mini](https://lws.io/blog/my-local-model-setup/) | ⭐ 96 | 💬 42 | [HN Thread](https://news.ycombinator.com/item?id=49529132) |
| **6** | [FBI Probes Service Selling 153M+ Drivers Licenses](https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/) | ⭐ 54 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=49529621) |
| **7** | [Introducing Ad Blocker for Firefox on iOS](https://blog.mozilla.org/en/firefox/ad-blocker-on-ios/) | ⭐ 344 | 💬 115 | [HN Thread](https://news.ycombinator.com/item?id=49521973) |
| **8** | [Sonic Pi](https://sonic-pi.net/) | ⭐ 59 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=49482099) |
| **9** | [The ChatGPT/Codex app bundles a full copy of LibreOffice](https://simonwillison.net/2026/Sep/1/codex-libreoffice/) | ⭐ 284 | 💬 122 | [HN Thread](https://news.ycombinator.com/item?id=49527396) |
| **10** | [Launch HN: Nori Robotics (YC S26) – A low-cost humanoid robot for development](https://www.norirobotics.com/) | ⭐ 123 | 💬 41 | [HN Thread](https://news.ycombinator.com/item?id=49525153) |

---

## 🗄️ News Archive

- 📅 [2026-09-02](archive/2026-09-02.md)
- 📅 [2026-09-01](archive/2026-09-01.md)
- 📅 [2026-08-31](archive/2026-08-31.md)
- 📅 [2026-08-30](archive/2026-08-30.md)
- 📅 [2026-08-29](archive/2026-08-29.md)
- 📅 [2026-08-28](archive/2026-08-28.md)
- 📅 [2026-08-27](archive/2026-08-27.md)
- 📅 [2026-08-26](archive/2026-08-26.md)
- 📅 [2026-08-25](archive/2026-08-25.md)
- 📅 [2026-08-24](archive/2026-08-24.md)
- 📅 [2026-08-23](archive/2026-08-23.md)
- 📅 [2026-08-22](archive/2026-08-22.md)
- 📅 [2026-08-21](archive/2026-08-21.md)
- 📅 [2026-08-20](archive/2026-08-20.md)

*... and [6 older editions in the archive folder](archive/)*

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
