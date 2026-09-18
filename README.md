# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Hacking OpenAI](https://www.hacktron.ai/blog/hacking-openai) | ⭐ 199 | 💬 54 | [HN Thread](https://news.ycombinator.com/item?id=49749656) |
| **2** | [Waymo in Singapore](https://waymo.com/waymo-in-singapore/) | ⭐ 66 | 💬 33 | [HN Thread](https://news.ycombinator.com/item?id=49749981) |
| **3** | [Astra for Law](https://openai.com/index/astra-for-law/) | ⭐ 423 | 💬 454 | [HN Thread](https://news.ycombinator.com/item?id=49745940) |
| **4** | [Bonsai 2 27B: Near-Lossless Compression in a 9x Smaller Footprint](https://prismml.com/news/bonsai-2-27b) | ⭐ 344 | 💬 113 | [HN Thread](https://news.ycombinator.com/item?id=49746618) |
| **5** | [Bend – A language that blocks AI mistakes via proof, on CPU and GPU](https://bend-lang.com/) | ⭐ 392 | 💬 192 | [HN Thread](https://news.ycombinator.com/item?id=49746163) |
| **6** | [Jemalloc 5.4.0](https://github.com/jemalloc/jemalloc/releases/tag/5.4.0) | ⭐ 13 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49750152) |
| **7** | [Pre-Greek: The lost language hidden within Ancient Greek](https://linguisticdiscovery.com/posts/pre-greek/) | ⭐ 34 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=49749771) |
| **8** | [The Scourge of x86 Emulation](https://fex-emu.com/Scourge-of-emulation/) | ⭐ 18 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49750094) |
| **9** | [Hister: A private search engine for the pages you visit and the files you keep](https://github.com/asciimoo/hister) | ⭐ 545 | 💬 143 | [HN Thread](https://news.ycombinator.com/item?id=49743097) |
| **10** | [Qwen 3.8 Omni Flash](https://qwen.ai/blog?id=qwen3.8-omni-flash) | ⭐ 136 | 💬 29 | [HN Thread](https://news.ycombinator.com/item?id=49747925) |

---

## 🗄️ News Archive

- 📅 [2026-09-18](archive/2026-09-18.md)
- 📅 [2026-09-16](archive/2026-09-16.md)
- 📅 [2026-09-15](archive/2026-09-15.md)
- 📅 [2026-09-14](archive/2026-09-14.md)
- 📅 [2026-09-13](archive/2026-09-13.md)
- 📅 [2026-09-12](archive/2026-09-12.md)
- 📅 [2026-09-11](archive/2026-09-11.md)
- 📅 [2026-09-10](archive/2026-09-10.md)
- 📅 [2026-09-09](archive/2026-09-09.md)
- 📅 [2026-09-08](archive/2026-09-08.md)
- 📅 [2026-09-07](archive/2026-09-07.md)
- 📅 [2026-09-06](archive/2026-09-06.md)
- 📅 [2026-09-05](archive/2026-09-05.md)
- 📅 [2026-09-04](archive/2026-09-04.md)

*... and [21 older editions in the archive folder](archive/)*

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
