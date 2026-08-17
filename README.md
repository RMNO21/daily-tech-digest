# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Qwen 3.8 27B is excellent, but it defaults to overthinking things](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) | ⭐ 431 | 💬 190 | [HN Thread](https://news.ycombinator.com/item?id=49324985) |
| **2** | [GIMP Development Update](https://www.gimp.org/news/2026/08/16/dev-update-august-2026/) | ⭐ 121 | 💬 56 | [HN Thread](https://news.ycombinator.com/item?id=49326156) |
| **3** | [On A.I. regulation and messaging](https://twitter.com/DarioAmodei/status/2088758816376807762) | ⭐ 43 | 💬 30 | [HN Thread](https://news.ycombinator.com/item?id=49325789) |
| **4** | [A third world engineer responds to “RISC-V: They should have known better”](https://rvembedded.com/blog_post/12/) | ⭐ 495 | 💬 260 | [HN Thread](https://news.ycombinator.com/item?id=49321717) |
| **5** | [Linear algebra done right](https://linear.axler.net/) | ⭐ 56 | 💬 28 | [HN Thread](https://news.ycombinator.com/item?id=49326816) |
| **6** | [Beware the Permanent Periphery](https://asteriskmag.com/issues/15/beware-the-permanent-periphery) | ⭐ 6 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49251775) |
| **7** | [Anthropic's 'watermark' text adulteration in Claude is a perversion of writing](https://daringfireball.net/2026/08/anthropics_watermark_text_adulteration_in_claude_is_a_perversion_of_writing) | ⭐ 226 | 💬 208 | [HN Thread](https://news.ycombinator.com/item?id=49324087) |
| **8** | [Reticulum – Decentralized Mesh Network](https://reticulum.network/) | ⭐ 116 | 💬 27 | [HN Thread](https://news.ycombinator.com/item?id=49325061) |
| **9** | [Claude: System Prompts](https://platform.claude.com/docs/en/release-notes/system-prompts) | ⭐ 644 | 💬 254 | [HN Thread](https://news.ycombinator.com/item?id=49319556) |
| **10** | [AGI-64 Brings Sierra Adventures to the Commodore 64](https://meanhamster.com/news/agi-64-brings-sierra-adventures-to-the-commodore-64) | ⭐ 81 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=49325714) |

---

## 🗄️ News Archive

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
