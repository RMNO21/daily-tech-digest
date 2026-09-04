# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [GPT-6 Astra](https://openai.com/index/gpt-6-astra/) | ⭐ 1488 | 💬 1257 | [HN Thread](https://news.ycombinator.com/item?id=49554643) |
| **2** | [.name Termination](https://neil.fraser.name/news/2026/09/03/) | ⭐ 1514 | 💬 405 | [HN Thread](https://news.ycombinator.com/item?id=49550772) |
| **3** | [Qwen 3.8 27B available on Cerebras at 1500 tokens/s](https://inference-docs.cerebras.ai/models/overview) | ⭐ 496 | 💬 148 | [HN Thread](https://news.ycombinator.com/item?id=49554520) |
| **4** | [Project Xanadu: Even More Hindsight](https://gwern.net/xanadu) | ⭐ 33 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49559522) |
| **5** | [A Mysterious Kidney Disease Has Arrived in Texas](https://www.texasmonthly.com/news-politics/ckdu-kidney-disease-immigration/) | ⭐ 27 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=49559992) |
| **6** | [How an MIT research project became the Julia programming language](https://news.mit.edu/2026/how-mit-research-project-became-global-programming-language-0831) | ⭐ 42 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=49507072) |
| **7** | [The largest electric aircraft just flew [video]](https://www.youtube.com/watch?v=nM86DBOqgPM) | ⭐ 239 | 💬 160 | [HN Thread](https://news.ycombinator.com/item?id=49526453) |
| **8** | [Grep beats LSP? Why coding agents ignore your fancier tools](https://www.agentconnect.md/blog/grep-beat-lsp-harness/) | ⭐ 19 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49560260) |
| **9** | [From Hookswitch to Grave](https://computer.rip/2026-06-14-hookswitch-to-grave.html) | ⭐ 12 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49559901) |
| **10** | [Artificial beaver dams saw juvenile coho salmon survival rates go from 8% to 60%](https://www.discoverwildlife.com/animal-facts/artificial-beaver-dams-california) | ⭐ 195 | 💬 60 | [HN Thread](https://news.ycombinator.com/item?id=49552572) |

---

## 🗄️ News Archive

- 📅 [2026-09-04](archive/2026-09-04.md)
- 📅 [2026-09-03](archive/2026-09-03.md)
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

*... and [8 older editions in the archive folder](archive/)*

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
