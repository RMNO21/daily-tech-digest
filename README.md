# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Claude Fable 5.1 and Claude Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1) | ⭐ 763 | 💬 722 | [HN Thread](https://news.ycombinator.com/item?id=49525378) |
| **2** | [How accurate have Ed Zitron's AI skeptic predictions been?](https://danluu.com/zitron/) | ⭐ 237 | 💬 255 | [HN Thread](https://news.ycombinator.com/item?id=49526069) |
| **3** | [The ChatGPT/Codex app bundles a full copy of LibreOffice](https://simonwillison.net/2026/Sep/1/codex-libreoffice/) | ⭐ 163 | 💬 84 | [HN Thread](https://news.ycombinator.com/item?id=49527396) |
| **4** | [Show HN: Weedout – Safari extension that hides YouTube AI-labeled videos](https://masteranza.github.io/weedout/) | ⭐ 9 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49528895) |
| **5** | [Refurbishing a Tektronix TDS7104 Oscilloscope](https://tomverbeure.github.io/2026/08/23/Tektronix-TDS7104-Refurbishing.html) | ⭐ 54 | 💬 22 | [HN Thread](https://news.ycombinator.com/item?id=49527232) |
| **6** | [Path to Astra: critical capabilities and frontier safeguards](https://openai.com/index/path-to-astra/) | ⭐ 52 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49527595) |
| **7** | [The creator of Jujutsu has joined ERSC](https://ersc.io/blog/martin-joins-ersc) | ⭐ 150 | 💬 116 | [HN Thread](https://news.ycombinator.com/item?id=49525297) |
| **8** | [AnkiDroid: Google Play no longer allowing Open Collective donation link](https://github.com/ankidroid/Anki-Android/issues/21656) | ⭐ 794 | 💬 228 | [HN Thread](https://news.ycombinator.com/item?id=49520022) |
| **9** | [Launch HN: Nori Robotics (YC S26) – A low-cost humanoid robot for development](https://www.norirobotics.com/) | ⭐ 97 | 💬 36 | [HN Thread](https://news.ycombinator.com/item?id=49525153) |
| **10** | [Introducing Ad Blocker for Firefox on iOS](https://blog.mozilla.org/en/firefox/ad-blocker-on-ios/) | ⭐ 248 | 💬 87 | [HN Thread](https://news.ycombinator.com/item?id=49521973) |

---

## 🗄️ News Archive

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
- 📅 [2026-08-19](archive/2026-08-19.md)

*... and [5 older editions in the archive folder](archive/)*

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
