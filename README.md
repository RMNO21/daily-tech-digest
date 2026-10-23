# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Local Wikipedia: Wikipedia, but only for things a half hour walk from you](https://edjefferson.com/localwiki/) | ⭐ 171 | 💬 35 | [HN Thread](https://news.ycombinator.com/item?id=50202285) |
| **2** | [The same AI request emits 8.5 times more CO2 in Texas than in Sweden](https://berget.ai/en/blog/per-request-co2-press-release) | ⭐ 45 | 💬 16 | [HN Thread](https://news.ycombinator.com/item?id=50205229) |
| **3** | [Docker is weird](https://codeandcake.dev/posts/2026-10-22-docker-is-weird) | ⭐ 385 | 💬 195 | [HN Thread](https://news.ycombinator.com/item?id=50202681) |
| **4** | [LLMs are making formal software verification feasible at a much larger scale](https://www.anthropic.com/research/formal-verification) | ⭐ 306 | 💬 167 | [HN Thread](https://news.ycombinator.com/item?id=50202217) |
| **5** | [How does Fable 5.1 hide messages in images?](https://www.lesswrong.com/posts/WHEQps5PK8LrrcTAb/how-does-fable-5-1-hide-messages-in-images) | ⭐ 32 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=50201445) |
| **6** | [The HTML-in-Canvas API origin trial](https://developer.chrome.com/blog/html-in-canvas-origin-trial) | ⭐ 22 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=50200164) |
| **7** | [The foolishness of "natural language programming" (1978)](https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html) | ⭐ 122 | 💬 75 | [HN Thread](https://news.ycombinator.com/item?id=50203161) |
| **8** | [This I Believe (1952)](https://www.awakin.org/v2/read/view.php?tid=468) | ⭐ 58 | 💬 19 | [HN Thread](https://news.ycombinator.com/item?id=50203759) |
| **9** | [The alien space of science: Coherent but cognitively unavailable directions](https://arxiv.org/abs/2603.01092) | ⭐ 25 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=50195002) |
| **10** | [OpenShell – A safe, private runtime for fleets of autonomous AI agents](https://github.com/NVIDIA/OpenShell) | ⭐ 373 | 💬 187 | [HN Thread](https://news.ycombinator.com/item?id=50198675) |

---

## 🗄️ News Archive

- 📅 [2026-10-23](archive/2026-10-23.md)
- 📅 [2026-10-22](archive/2026-10-22.md)
- 📅 [2026-10-21](archive/2026-10-21.md)
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

*... and [52 older editions in the archive folder](archive/)*

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
