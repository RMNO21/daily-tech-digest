# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Cloudflare Quick Tunnels](https://try.cloudflare.com/) | ⭐ 121 | 💬 70 | [HN Thread](https://news.ycombinator.com/item?id=49754785) |
| **2** | [An Empirical Study of Harness Design for Coding Agents](https://arxiv.org/abs/2609.20804) | ⭐ 144 | 💬 31 | [HN Thread](https://news.ycombinator.com/item?id=49753878) |
| **3** | [North Korean nuclear test sets off years of earthquakes](https://www.science.org/content/article/north-korean-nuclear-test-sets-years-earthquakes) | ⭐ 54 | 💬 41 | [HN Thread](https://news.ycombinator.com/item?id=49755160) |
| **4** | [OpenJev](https://openjev.com/) | ⭐ 354 | 💬 194 | [HN Thread](https://news.ycombinator.com/item?id=49752041) |
| **5** | [GrassLobster: AI Agentic Generation of Parametric Geometry Workflows](https://www.miro.vision/index.php/2026/09/17/grasslobbster/) | ⭐ 12 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49755431) |
| **6** | [Show HN: Microsoft Office running with Wine on Linux with no virtualization](https://github.com/Tombert/office365_flake) | ⭐ 9 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49746401) |
| **7** | [I don't like passkeys](https://hawksley.dev/blog/i-dont-like-passkeys) | ⭐ 459 | 💬 431 | [HN Thread](https://news.ycombinator.com/item?id=49753211) |
| **8** | [Mathematicians Build Long-Awaited Graph Sandwich](https://www.quantamagazine.org/mathematicians-build-long-awaited-graph-sandwich-20260918/) | ⭐ 16 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49755095) |
| **9** | [The Shadows Lurking in the Equations – Underwater Islands](https://gods.art/articles/equation_shadows) | ⭐ 42 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=49721507) |
| **10** | [US Treasuries Have Become Unappetizing for Foreign Central Banks and Governments](https://wolfstreet.com/2026/09/17/treasuries-have-become-badly-unappetizing-for-foreign-central-banks-governments/) | ⭐ 30 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49756171) |

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
