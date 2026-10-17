# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [DeepSeek: DeepSeek v4.1 Flash 1017](https://openrouter.ai/deepseek/deepseek-v4.1-flash-1017) | ⭐ 55 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=50129121) |
| **2** | [Ultramarine 1 Flash](https://www.paperinstruments.com/ultramarine) | ⭐ 239 | 💬 68 | [HN Thread](https://news.ycombinator.com/item?id=50106747) |
| **3** | [Tesla Roadster](https://www.tesla.com/roadster) | ⭐ 1419 | 💬 2491 | [HN Thread](https://news.ycombinator.com/item?id=50112657) |
| **4** | [Show HN: Llmspeed – feel how fast a local LLM runs before you buy the hardware](https://llmspeed.dev/) | ⭐ 68 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=50127979) |
| **5** | [DeepSeek-v4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) | ⭐ 82 | 💬 31 | [HN Thread](https://news.ycombinator.com/item?id=50129045) |
| **6** | ["Tame" boar and deer are instinctively adapting to the wolf in the Netherlands](https://nos.nl/video/2635315-wildcamera-s-tonen-hoe-zwijnen-en-herten-zich-aanpassen-aan-de-wolf) | ⭐ 3 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50129274) |
| **7** | [Intuitive concurrent programming in any language](https://www.lf-lang.org/) | ⭐ 35 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=50103255) |
| **8** | [Llama.cpp on a jailbroken PS5: run any GGUF model natively on the console](https://github.com/cobanov/PS5LM) | ⭐ 287 | 💬 72 | [HN Thread](https://news.ycombinator.com/item?id=50122431) |
| **9** | [You could have invented transformers from memory](https://alexwang.ai/posts/associative-memory/) | ⭐ 298 | 💬 69 | [HN Thread](https://news.ycombinator.com/item?id=50122878) |
| **10** | [Claude reveals ECDSA curve origins](https://www.anthropic.com/research/ecdsa-curve-origins) | ⭐ 865 | 💬 323 | [HN Thread](https://news.ycombinator.com/item?id=50122800) |

---

## 🗄️ News Archive

- 📅 [2026-10-17](archive/2026-10-17.md)
- 📅 [2026-10-16](archive/2026-10-16.md)
- 📅 [2026-10-15](archive/2026-10-15.md)
- 📅 [2026-10-14](archive/2026-10-14.md)
- 📅 [2026-10-13](archive/2026-10-13.md)
- 📅 [2026-10-10](archive/2026-10-10.md)
- 📅 [2026-10-09](archive/2026-10-09.md)
- 📅 [2026-10-08](archive/2026-10-08.md)
- 📅 [2026-10-07](archive/2026-10-07.md)
- 📅 [2026-10-05](archive/2026-10-05.md)
- 📅 [2026-10-04](archive/2026-10-04.md)
- 📅 [2026-10-03](archive/2026-10-03.md)
- 📅 [2026-10-02](archive/2026-10-02.md)
- 📅 [2026-10-01](archive/2026-10-01.md)

*... and [46 older editions in the archive folder](archive/)*

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
