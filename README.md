# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Saving 100 terabytes of memory by optimizing 1.1.1.1's DNS cache](https://blog.cloudflare.com/dns-cache-memory-optimization-1111/) | ⭐ 360 | 💬 104 | [HN Thread](https://news.ycombinator.com/item?id=49468083) |
| **2** | [Small Models Have Arrived](https://calv.info/small-models-have-arrived) | ⭐ 350 | 💬 154 | [HN Thread](https://news.ycombinator.com/item?id=49466917) |
| **3** | [507 Mechanical Movements](https://507movements.com/) | ⭐ 414 | 💬 62 | [HN Thread](https://news.ycombinator.com/item?id=49465169) |
| **4** | [We found a division by zero bug in FFmpeg with a vibecoded fuzzer](https://code.ffmpeg.org/FFmpeg/FFmpeg/issues/24290) | ⭐ 122 | 💬 92 | [HN Thread](https://news.ycombinator.com/item?id=49468642) |
| **5** | [Show HN: We built open OpenRouter that distills usage into a better model](https://github.com/experientiallabs/experiential) | ⭐ 8 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49471407) |
| **6** | [Gemini-3.5-Transcribe](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/) | ⭐ 66 | 💬 19 | [HN Thread](https://news.ycombinator.com/item?id=49468818) |
| **7** | [Microduck](https://pollen-robotics.com/microduck/) | ⭐ 442 | 💬 173 | [HN Thread](https://news.ycombinator.com/item?id=49462763) |
| **8** | [Decompiling a Nintendo 64 game in 84 days](https://blog.chrislewis.au/decompiling-a-nintendo-64-game-in-84-days/) | ⭐ 151 | 💬 69 | [HN Thread](https://news.ycombinator.com/item?id=49466006) |
| **9** | [M5Stack Launches PaperMono](https://shop.m5stack.com/blogs/news/m5stack-launches-papermono-a-compact-e-ink-development-terminal-for-connected-projects) | ⭐ 73 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=49468593) |
| **10** | [Gemini Omni 1.1 Flash](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/) | ⭐ 160 | 💬 110 | [HN Thread](https://news.ycombinator.com/item?id=49467922) |

---

## 🗄️ News Archive

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
