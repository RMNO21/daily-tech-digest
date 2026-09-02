# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Gemini 3.8 Flash](https://deepmind.google/models/model-cards/gemini-3-8-flash/) | ⭐ 205 | 💬 106 | [HN Thread](https://news.ycombinator.com/item?id=49537553) |
| **2** | [A Note from LWN](https://lwn.net/Articles/1090585/) | ⭐ 437 | 💬 92 | [HN Thread](https://news.ycombinator.com/item?id=49535752) |
| **3** | [GrapheneOS says Pixel 11 has MTE support after all](https://grapheneos.social/@GrapheneOS/117194007157499435) | ⭐ 89 | 💬 57 | [HN Thread](https://news.ycombinator.com/item?id=49536384) |
| **4** | [Mistral now trains on user input by default, except on enterprise tier](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training) | ⭐ 169 | 💬 77 | [HN Thread](https://news.ycombinator.com/item?id=49535284) |
| **5** | [Biggest dark matter detector spots a single weird particle](https://www.science.org/content/article/world-s-biggest-dark-matter-detector-spots-single-weird-particle) | ⭐ 106 | 💬 18 | [HN Thread](https://news.ycombinator.com/item?id=49536079) |
| **6** | [Three sites made 215,128 “best software” pages for AI. Perplexity cites them](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/) | ⭐ 139 | 💬 76 | [HN Thread](https://news.ycombinator.com/item?id=49536375) |
| **7** | [Exit the Cave](https://turtlespace.blog/p/exit-the-cave) | ⭐ 55 | 💬 13 | [HN Thread](https://news.ycombinator.com/item?id=49536606) |
| **8** | [Gemini 3.8 Flash and 3.8 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) | ⭐ 19 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49538007) |
| **9** | [Poisson Disk Sampling](https://stripeacross.com/posts/poisson-disk-sampling/) | ⭐ 54 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49536177) |
| **10** | [Aging Brains Blend Memories Together Instead of Just Forgetting Them](https://studyfinds.com/aging-brains-blend-memories-together-instead-of-forgetting-them-study-finds/) | ⭐ 69 | 💬 26 | [HN Thread](https://news.ycombinator.com/item?id=49535548) |

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
