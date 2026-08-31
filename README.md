# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Playa Phone](https://playaphone.com/) | ⭐ 89 | 💬 29 | [HN Thread](https://news.ycombinator.com/item?id=49510514) |
| **2** | [OpenShot 4.0: Record, Edit, and Color Like Never Before](https://www.openshot.org/blog/2026/08/30/openshot-40-record-edit-color-like-never-before/) | ⭐ 380 | 💬 89 | [HN Thread](https://news.ycombinator.com/item?id=49507822) |
| **3** | [Apache Iggy, a message streaming platform in Rust, graduates to an Apache TLP](https://iggy.apache.org/blogs/2026/08/24/apache-iggy-top-level-project-tlp-graduation/) | ⭐ 40 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=49510540) |
| **4** | [ChatGPT Work Tool and Skill Reference](https://codex-tool-reference.simonw.chatgpt.site/) | ⭐ 68 | 💬 36 | [HN Thread](https://news.ycombinator.com/item?id=49510000) |
| **5** | [Launch HN: Almanac (YC S26) – AI that knows your company](https://usealmanac.com/) | ⭐ 9 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49511007) |
| **6** | [Culture Clash](https://aeon.co/essays/at-the-heart-of-the-snow-leavis-two-cultures-clash) | ⭐ 22 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49510489) |
| **7** | [C++26: Standard Library Hardening Experiments](https://www.cppstories.com/2026/hardening-experiments/) | ⭐ 20 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=49510511) |
| **8** | [Launch HN: Hebbian Robotics (YC S26) – Build scalable robotics data pipelines](https://github.com/Hebbian-Robotics/hflow) | ⭐ 9 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49510632) |
| **9** | [Agentic Trust Controls](https://trustcontrols.ai/) | ⭐ 11 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49510612) |
| **10** | [Breaking Claude Code Opus 5 Auto Mode](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/) | ⭐ 266 | 💬 82 | [HN Thread](https://news.ycombinator.com/item?id=49506819) |

---

## 🗄️ News Archive

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
- 📅 [2026-08-19](archive/2026-08-19.md)
- 📅 [2026-08-18](archive/2026-08-18.md)

*... and [4 older editions in the archive folder](archive/)*

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
