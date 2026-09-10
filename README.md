# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [More questions about whether researchers can trust OpenAI with unpublished math](https://mathstodon.xyz/@andreasthom/117240535270608201) | ⭐ 522 | 💬 534 | [HN Thread](https://news.ycombinator.com/item?id=49639408) |
| **2** | [NTSB Issues Investigative Update on B-767 Runway Excursion Accident in Miami](https://www.ntsb.gov:443/news/press-releases/Pages/NR20260909.aspx) | ⭐ 29 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=49650418) |
| **3** | [Cognition launches new SWE-2 model, Rivaling Fable 5.1 and GPT-Astra](https://cognition.com/blog/swe-2) | ⭐ 326 | 💬 133 | [HN Thread](https://news.ycombinator.com/item?id=49645443) |
| **4** | [NASA Color Trick Was Meant for Mars. Now It's Unveiling Rock Art on Earth](https://gizmodo.com/this-nasa-color-trick-was-meant-for-mars-now-its-unveiling-rock-art-on-earth-2000809844) | ⭐ 233 | 💬 36 | [HN Thread](https://news.ycombinator.com/item?id=49645437) |
| **5** | [Don't let anyone take away your big box of cables](https://blog.jim-nielsen.com/2026/hands-off-my-cables/) | ⭐ 227 | 💬 177 | [HN Thread](https://news.ycombinator.com/item?id=49645393) |
| **6** | [OpenAI Agents API](https://developers.openai.com/api/docs/guides/agents-api/overview) | ⭐ 49 | 💬 44 | [HN Thread](https://news.ycombinator.com/item?id=49649213) |
| **7** | [The part of Navier-Stokes no one is talking about](https://www.johndcook.com/blog/2026/09/09/formal-method-revolution/) | ⭐ 95 | 💬 75 | [HN Thread](https://news.ycombinator.com/item?id=49650326) |
| **8** | [Music Theory for the 21st-Century Classroom](https://musictheory.pugetsound.edu/mt21c/MusicTheory.html) | ⭐ 122 | 💬 60 | [HN Thread](https://news.ycombinator.com/item?id=49647134) |
| **9** | [Forgejo <=16.0.3 Critical RCE](https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md) | ⭐ 127 | 💬 48 | [HN Thread](https://news.ycombinator.com/item?id=49645907) |
| **10** | [Proof of Capture: Apple Reference Image, but open source and using steganography](https://merybenavente.me/blog/proof-of-capture) | ⭐ 33 | 💬 28 | [HN Thread](https://news.ycombinator.com/item?id=49649222) |

---

## 🗄️ News Archive

- 📅 [2026-09-10](archive/2026-09-10.md)
- 📅 [2026-09-09](archive/2026-09-09.md)
- 📅 [2026-09-08](archive/2026-09-08.md)
- 📅 [2026-09-07](archive/2026-09-07.md)
- 📅 [2026-09-06](archive/2026-09-06.md)
- 📅 [2026-09-05](archive/2026-09-05.md)
- 📅 [2026-09-04](archive/2026-09-04.md)
- 📅 [2026-09-03](archive/2026-09-03.md)
- 📅 [2026-09-02](archive/2026-09-02.md)
- 📅 [2026-09-01](archive/2026-09-01.md)
- 📅 [2026-08-31](archive/2026-08-31.md)
- 📅 [2026-08-30](archive/2026-08-30.md)
- 📅 [2026-08-29](archive/2026-08-29.md)
- 📅 [2026-08-28](archive/2026-08-28.md)

*... and [14 older editions in the archive folder](archive/)*

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
