# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Hilariously Fast Volume Computation with the Divergence Theorem](https://alyssarosenzweig.ca/blog/hilariously-fast-volume-computation-with-the-divergence-theorem.html) | ⭐ 44 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49476143) |
| **2** | [Saving 100 terabytes of memory by optimizing 1.1.1.1's DNS cache](https://blog.cloudflare.com/dns-cache-memory-optimization-1111/) | ⭐ 769 | 💬 225 | [HN Thread](https://news.ycombinator.com/item?id=49468083) |
| **3** | [Small Models Have Arrived](https://calv.info/small-models-have-arrived) | ⭐ 648 | 💬 295 | [HN Thread](https://news.ycombinator.com/item?id=49466917) |
| **4** | [Sovereign Tech Agency invests €500k in Flatpak](https://modal.cx/blog/announcing-flatpak-sta/) | ⭐ 129 | 💬 73 | [HN Thread](https://news.ycombinator.com/item?id=49474786) |
| **5** | [507 Mechanical Movements](https://507movements.com/) | ⭐ 587 | 💬 74 | [HN Thread](https://news.ycombinator.com/item?id=49465169) |
| **6** | [Show HN: OpenTIE and OpenXWA, Modern Ports of Tie Fighter and X-Wing Alliance](https://github.com/elyosh/OpenTIE/) | ⭐ 164 | 💬 38 | [HN Thread](https://news.ycombinator.com/item?id=49471965) |
| **7** | [Gemini-3.5-Transcribe](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/) | ⭐ 288 | 💬 92 | [HN Thread](https://news.ycombinator.com/item?id=49468818) |
| **8** | [Microduck](https://pollen-robotics.com/microduck/) | ⭐ 664 | 💬 213 | [HN Thread](https://news.ycombinator.com/item?id=49462763) |
| **9** | [Doctors are finally learning to manage antidepressant withdrawal](https://www.newscientist.com/article/2584861-antidepressant-withdrawal-symptoms-are-prompting-a-radical-rethink-of-how-we-treat-depression/) | ⭐ 129 | 💬 119 | [HN Thread](https://news.ycombinator.com/item?id=49472090) |
| **10** | [We found a division by zero bug in FFmpeg with a vibecoded fuzzer](https://code.ffmpeg.org/FFmpeg/FFmpeg/issues/24290) | ⭐ 248 | 💬 194 | [HN Thread](https://news.ycombinator.com/item?id=49468642) |

---

## 🗄️ News Archive

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
- 📅 [2026-08-17](archive/2026-08-17.md)
- 📅 [2026-08-16](archive/2026-08-16.md)
- 📅 [2026-08-15](archive/2026-08-15.md)

*... and [1 older editions in the archive folder](archive/)*

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
