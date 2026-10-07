# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Sharing AI progress in mathematics](https://openai.com/index/sharing-ai-progress-in-mathematics/) | ⭐ 870 | 💬 784 | [HN Thread](https://news.ycombinator.com/item?id=49984923) |
| **2** | [Strands Decider 2B: a small, open-source, decision model](https://strandsagents.com/blog/introducing-strands-decider/) | ⭐ 161 | 💬 38 | [HN Thread](https://news.ycombinator.com/item?id=49987076) |
| **3** | [Decisions API is in public beta](https://developers.openai.com/api/docs/guides/decisions) | ⭐ 272 | 💬 130 | [HN Thread](https://news.ycombinator.com/item?id=49984025) |
| **4** | [The art of defusing a second world war bomb](https://www.theguardian.com/news/ng-interactive/2026/oct/06/it-could-knock-a-whole-street-down-the-art-of-defusing-a-second-world-war-bomb) | ⭐ 50 | 💬 16 | [HN Thread](https://news.ycombinator.com/item?id=49987858) |
| **5** | [Mistral Large 4](https://mistral.ai/news/mistral-large-4/\) | ⭐ 1782 | 💬 1055 | [HN Thread](https://news.ycombinator.com/item?id=49977979) |
| **6** | [EmbeddingGemma 2: An open, lightweight multimodal embedding model](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/) | ⭐ 311 | 💬 32 | [HN Thread](https://news.ycombinator.com/item?id=49980487) |
| **7** | [The Legend of the Paper Crane](https://mazdastories.com/en_us/inspire/paper-cranes-into-the-fold/) | ⭐ 11 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49953939) |
| **8** | [ESP32-C3 Adblock](https://github.com/M-Abozaid/esp32-c3-adblock) | ⭐ 86 | 💬 28 | [HN Thread](https://news.ycombinator.com/item?id=49986862) |
| **9** | [What is Codemode](https://lucumr.pocoo.org/2026/10/6/codemode/) | ⭐ 74 | 💬 30 | [HN Thread](https://news.ycombinator.com/item?id=49978333) |
| **10** | [Shaders, WebGPU Components for React, Vue, Svelte, Solid, JavaScript and Framer](https://github.com/shader-effects-inc/shaders) | ⭐ 18 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49988709) |

---

## 🗄️ News Archive

- 📅 [2026-10-07](archive/2026-10-07.md)
- 📅 [2026-10-05](archive/2026-10-05.md)
- 📅 [2026-10-04](archive/2026-10-04.md)
- 📅 [2026-10-03](archive/2026-10-03.md)
- 📅 [2026-10-02](archive/2026-10-02.md)
- 📅 [2026-10-01](archive/2026-10-01.md)
- 📅 [2026-09-30](archive/2026-09-30.md)
- 📅 [2026-09-29](archive/2026-09-29.md)
- 📅 [2026-09-28](archive/2026-09-28.md)
- 📅 [2026-09-27](archive/2026-09-27.md)
- 📅 [2026-09-26](archive/2026-09-26.md)
- 📅 [2026-09-25](archive/2026-09-25.md)
- 📅 [2026-09-24](archive/2026-09-24.md)
- 📅 [2026-09-22](archive/2026-09-22.md)

*... and [38 older editions in the archive folder](archive/)*

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
