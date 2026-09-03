# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [GPT-6 Astra](https://openai.com/index/gpt-6-astra/) | ⭐ 941 | 💬 670 | [HN Thread](https://news.ycombinator.com/item?id=49554643) |
| **2** | [Qwen 3.8 27B available on Cerebras at 1500 tokens/s](https://inference-docs.cerebras.ai/models/overview) | ⭐ 348 | 💬 112 | [HN Thread](https://news.ycombinator.com/item?id=49554520) |
| **3** | [.name Termination](https://neil.fraser.name/news/2026/09/03/) | ⭐ 1138 | 💬 335 | [HN Thread](https://news.ycombinator.com/item?id=49550772) |
| **4** | [The largest electric aircraft just flew [video]](https://www.youtube.com/watch?v=nM86DBOqgPM) | ⭐ 87 | 💬 59 | [HN Thread](https://news.ycombinator.com/item?id=49526453) |
| **5** | [K2 Horizon: A connected fleet of six open models](https://ifm.ai/blog/k2/) | ⭐ 225 | 💬 72 | [HN Thread](https://news.ycombinator.com/item?id=49551760) |
| **6** | [Any Human Ever – One life, drawn at random from all who have ever lived](https://anyhumanever.com/) | ⭐ 387 | 💬 185 | [HN Thread](https://news.ycombinator.com/item?id=49550698) |
| **7** | [Porting my 1993 Amiga game to Godot, with an LLM reading the 68000 assembly](https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/) | ⭐ 133 | 💬 46 | [HN Thread](https://news.ycombinator.com/item?id=49550375) |
| **8** | [Tasklet (YC P26) Is Hiring a Customer Success Engineer](https://tasklet.ai/careers/customer-success-engineer) | ⭐ 1 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49556922) |
| **9** | [Artificial beaver dams saw juvenile coho salmon survival rates go from 8% to 60%](https://www.discoverwildlife.com/animal-facts/artificial-beaver-dams-california) | ⭐ 97 | 💬 26 | [HN Thread](https://news.ycombinator.com/item?id=49552572) |
| **10** | [OpenAI's GPT-6 Astra on ARC-AGI-3](https://arcprize.org/blog/astra) | ⭐ 108 | 💬 53 | [HN Thread](https://news.ycombinator.com/item?id=49555691) |

---

## 🗄️ News Archive

- 📅 [2026-09-03](archive/2026-09-03.md)
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
python scraper.py --force
```

---

<div align="center">
  <sub>Maintained by <a href="https://github.com/RMNO21">RMNO21</a> • Powered by GitHub Actions & Hacker News API</sub>
</div>
