# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Muse Spark 1.3](https://developer.meta.com/ai/models/muse-spark/) | ⭐ 275 | 💬 173 | [HN Thread](https://news.ycombinator.com/item?id=49541256) |
| **2** | [Gemini 3.8 Flash and 3.8 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) | ⭐ 740 | 💬 429 | [HN Thread](https://news.ycombinator.com/item?id=49537553) |
| **3** | [Google avoids a breakup of its ad tech business](https://www.nytimes.com/2026/09/02/technology/google-ad-tech-remedies.html) | ⭐ 172 | 💬 93 | [HN Thread](https://news.ycombinator.com/item?id=49537131) |
| **4** | [Reverse Engineering Unknown File Formats with ImHex](https://werwolv.net/posts/file_format_reverse_engineering/) | ⭐ 46 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49508608) |
| **5** | [Fable 5.1 World Modeling](https://github.com/PhiloLabs/fable51-worlds) | ⭐ 83 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=49541458) |
| **6** | [Three sites made 215,128 “best software” pages for AI. Perplexity cites them](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/) | ⭐ 260 | 💬 121 | [HN Thread](https://news.ycombinator.com/item?id=49536375) |
| **7** | [Altair Basic Interpreter Source Code (1975) [pdf]](https://images.gatesnotes.com/12514eb8-7b51-008e-41a9-512542cf683b/34d561c8-cf5c-4e69-af47-3782ea11482e/Original-Microsoft-Source-Code.pdf) | ⭐ 29 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=49541754) |
| **8** | [Wendell Berry has died](https://www.nytimes.com/2026/08/31/us/wendell-berry-dead.html) | ⭐ 103 | 💬 49 | [HN Thread](https://news.ycombinator.com/item?id=49517018) |
| **9** | [Nango (YC W23) is hiring across eng, product and GTM (SF and remote)](https://nango.dev/careers) | ⭐ 1 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49542486) |
| **10** | [Can I opt out of my input or output data being used for training?](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training) | ⭐ 346 | 💬 149 | [HN Thread](https://news.ycombinator.com/item?id=49535284) |

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
