# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Platform-Independent SIMD in Go](https://go.dev/blog/simd-experiment) | ⭐ 276 | 💬 98 | [HN Thread](https://news.ycombinator.com/item?id=49843269) |
| **2** | [Git-bug: Distributed, offline-first bug tracker embedded in Git](https://github.com/git-bug/git-bug) | ⭐ 226 | 💬 74 | [HN Thread](https://news.ycombinator.com/item?id=49843174) |
| **3** | [Yes, Claude can do Nine Loops](https://www.anthropic.com/research/yes-claude-can-do-nine-loops) | ⭐ 8 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49848033) |
| **4** | [First Principles Thinking](https://sunilsadasivan.com/writing/first-principles-thinking/) | ⭐ 120 | 💬 54 | [HN Thread](https://news.ycombinator.com/item?id=49844736) |
| **5** | [Pentium II at 600Mhz with Voodoo 3 Emulated on 86Box with M6 Mac Mini](https://nyaa.sh/reviews/mac-mini-m6-emulation) | ⭐ 217 | 💬 96 | [HN Thread](https://news.ycombinator.com/item?id=49841285) |
| **6** | [F-Droid 2.0](https://f-droid.org/2026/09/24/f-droid-2.0-a-new-chapter-for-android-freedom.html) | ⭐ 1408 | 💬 403 | [HN Thread](https://news.ycombinator.com/item?id=49831968) |
| **7** | [Classified Estimates Show the NSA Is Paying Billions to Test AI Models](https://www.washingtonsun.com/technology/classified-estimates-nsa-paying-billions-to-test-ai-models) | ⭐ 138 | 💬 72 | [HN Thread](https://news.ycombinator.com/item?id=49845952) |
| **8** | [U.S. appeals court upholds designation of Anthropic as supply chain risk](https://www.cnbc.com/2026/09/25/pentagon-anthropic-ai-risk-appeals-court.html) | ⭐ 229 | 💬 323 | [HN Thread](https://news.ycombinator.com/item?id=49845977) |
| **9** | [Ink and Switch Interactive Homepage](https://www.inkandswitch.com/) | ⭐ 173 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=49842270) |
| **10** | [Show HN: Doom or Bloom, map your AI worldview with Jev](https://www.doom-or-bloom.com) | ⭐ 11 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49846953) |

---

## 🗄️ News Archive

- 📅 [2026-09-25](archive/2026-09-25.md)
- 📅 [2026-09-24](archive/2026-09-24.md)
- 📅 [2026-09-22](archive/2026-09-22.md)
- 📅 [2026-09-21](archive/2026-09-21.md)
- 📅 [2026-09-20](archive/2026-09-20.md)
- 📅 [2026-09-19](archive/2026-09-19.md)
- 📅 [2026-09-18](archive/2026-09-18.md)
- 📅 [2026-09-16](archive/2026-09-16.md)
- 📅 [2026-09-15](archive/2026-09-15.md)
- 📅 [2026-09-14](archive/2026-09-14.md)
- 📅 [2026-09-13](archive/2026-09-13.md)
- 📅 [2026-09-12](archive/2026-09-12.md)
- 📅 [2026-09-11](archive/2026-09-11.md)
- 📅 [2026-09-10](archive/2026-09-10.md)

*... and [27 older editions in the archive folder](archive/)*

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
