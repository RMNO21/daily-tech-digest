# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Wine Ported to OpenBSD](https://marc.info/?l=openbsd-ports&m=179236125692175) | ⭐ 290 | 💬 76 | [HN Thread](https://news.ycombinator.com/item?id=50152307) |
| **2** | [CERN and Mistral join forces to accelerate AI for science](https://home.cern/cern-and-mistral-join-forces-to-accelerate-ai-for-science/) | ⭐ 125 | 💬 18 | [HN Thread](https://news.ycombinator.com/item?id=50153630) |
| **3** | [Ontology-Driven Observability: Building an End-to-End Knowledge Graph at Netflix](https://netflixtechblog.com/ontology-driven-observability-building-an-end-to-end-knowledge-graph-at-netflix-scale-421392cf5adf) | ⭐ 69 | 💬 16 | [HN Thread](https://news.ycombinator.com/item?id=50153431) |
| **4** | [Timestral: Mistral release time-series foundation models](https://mistral.ai/news/timestral/) | ⭐ 379 | 💬 68 | [HN Thread](https://news.ycombinator.com/item?id=50150434) |
| **5** | [Linux 7.3](https://lwn.net/Articles/1101143/) | ⭐ 538 | 💬 241 | [HN Thread](https://news.ycombinator.com/item?id=50149392) |
| **6** | [Evidence (YC S21) Is Hiring Software Engineers](https://evidence.dev/jobs) | ⭐ 1 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50155172) |
| **7** | [It's still OK to enjoy programming](https://chriskiehl.com/article/it-is-still-ok-to-enjoy-programming) | ⭐ 113 | 💬 121 | [HN Thread](https://news.ycombinator.com/item?id=50134472) |
| **8** | [Alternatives to Animal Testing Are Finally Taking Off](https://spectrum.ieee.org/alternatives-to-animal-testing) | ⭐ 193 | 💬 49 | [HN Thread](https://news.ycombinator.com/item?id=50150927) |
| **9** | [Launch HN: Laminar (YC S24) – We trained a model to catch silent agent failures](https://news.ycombinator.com/item?id=50154029) | ⭐ 18 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=50154029) |
| **10** | [Let's Encrypt is adding two additional remote perspectives for domain validation](https://community.letsencrypt.org/t/lets-encrypt-is-adding-two-additional-remote-perspectives-for-domain-validation/252166) | ⭐ 173 | 💬 57 | [HN Thread](https://news.ycombinator.com/item?id=50150809) |

---

## 🗄️ News Archive

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
- 📅 [2026-10-03](archive/2026-10-03.md)

*... and [48 older editions in the archive folder](archive/)*

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
