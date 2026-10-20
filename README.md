# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [DeepSeek just open-sourced its inference engine](https://github.com/deepseek-ai/DeepInfer) | ⭐ 987 | 💬 338 | [HN Thread](https://news.ycombinator.com/item?id=50163277) |
| **2** | [Demographic "Doomsday" Misses the Mark](https://www.science.org/doi/10.1126/science.ael8752) | ⭐ 35 | 💬 34 | [HN Thread](https://news.ycombinator.com/item?id=50165276) |
| **3** | [MicroG: Free-libre re-implementation of Google's proprietary Android user space](https://github.com/microg/GmsCore/wiki) | ⭐ 194 | 💬 18 | [HN Thread](https://news.ycombinator.com/item?id=50162177) |
| **4** | [Nordwand Mono – A monospace font for coders and adventurers](https://github.com/tywr/Nordwand-Mono) | ⭐ 392 | 💬 119 | [HN Thread](https://news.ycombinator.com/item?id=50141581) |
| **5** | [Apple broke an essential presentation feature of iPads](https://teddysvoronos.com/2026-10-19-apple-broke-an-essential-presentation-feature-of-ipads/) | ⭐ 12 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=50165208) |
| **6** | [OpenBSD 8.0](https://www.openbsd.org/80.html) | ⭐ 378 | 💬 119 | [HN Thread](https://news.ycombinator.com/item?id=50160494) |
| **7** | [WhatsApp's help pages hid LLM instructions: dont recommend a regulator](https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions) | ⭐ 587 | 💬 165 | [HN Thread](https://news.ycombinator.com/item?id=50159341) |
| **8** | [DeepSeek banned from U.S. federal civilian agencies under new DHS order](https://www.reuters.com/technology/us-banning-chinese-ai-deepseek-government-agency-it-systems-2026-10-19/) | ⭐ 389 | 💬 330 | [HN Thread](https://news.ycombinator.com/item?id=50154244) |
| **9** | [Hazel (YC W24) Is Hiring](https://www.ycombinator.com/companies/hazel-2/jobs/PpNKYBS-full-stack-engineer-ts-sci) | ⭐ 1 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50164991) |
| **10** | [Making a 88x31 button book using ImageMagick](https://k.sosnierz.me/08-11-24/) | ⭐ 87 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=50132198) |

---

## 🗄️ News Archive

- 📅 [2026-10-20](archive/2026-10-20.md)
- 📅 [2026-10-19](archive/2026-10-19.md)
- 📅 [2026-10-18](archive/2026-10-18.md)
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

*... and [49 older editions in the archive folder](archive/)*

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
