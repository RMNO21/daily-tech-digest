# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [A 3rd World Embedded Engineer Responds to "RISC-V They Should Have Known Better"](https://rvembedded.com/blog_post/12/) | ⭐ 179 | 💬 99 | [HN Thread](https://news.ycombinator.com/item?id=49321717) |
| **2** | [Claude: System Prompts](https://platform.claude.com/docs/en/release-notes/system-prompts) | ⭐ 417 | 💬 182 | [HN Thread](https://news.ycombinator.com/item?id=49319556) |
| **3** | [Models Are Getting Dumber on Purpose](https://w4g1.dev/blog/models-are-getting-dumber-on-purpose) | ⭐ 103 | 💬 56 | [HN Thread](https://news.ycombinator.com/item?id=49322695) |
| **4** | [Protobuf has LSP support. You're welcome](https://buf.build/blog/protobuf-lsp) | ⭐ 30 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49322573) |
| **5** | [The AI Credit Resale Economy](https://vectoral.com/blog/who-are-the-token-brokers) | ⭐ 174 | 💬 65 | [HN Thread](https://news.ycombinator.com/item?id=49320611) |
| **6** | [MathCode, Mathematical Coding Agent](https://math-ai-org.github.io/mathcode/) | ⭐ 25 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=49322330) |
| **7** | [St Lucie Nuclear Reactor Unit 1 manually shutdown, 3 control rods drop into core](https://www.wptv.com/news/treasure-coast/region-st-lucie-county/saint-lucie-nuclear-power-plant-unit-1-manually-shut-down-after-3-control-rods-drop-into-reactor-core) | ⭐ 116 | 💬 82 | [HN Thread](https://news.ycombinator.com/item?id=49320856) |
| **8** | [Anton Chekhov played at love most of his life](https://commonreader.wustl.edu/winning-and-losing-at-the-great-game-of-intimacy/) | ⭐ 42 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49306021) |
| **9** | [Clamiga: Common Lisp for the Amiga](https://nnamgreb.de/blog/Clamiga+-+Common+Lisp+for+the+Amiga) | ⭐ 57 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49281352) |
| **10** | [NIH is ending a key grant for budding clinical researchers](https://www.science.org/content/article/nih-ending-key-grant-budding-clinical-researchers) | ⭐ 96 | 💬 40 | [HN Thread](https://news.ycombinator.com/item?id=49321353) |

---

## 🗄️ News Archive

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
