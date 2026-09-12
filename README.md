# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [LG denies TV spying claims, says tracking and snooping concerns 'not true'](https://www.tomshardware.com/tech-industry/big-tech/lg-strongly-denies-tv-security-claims-says-tracking-and-snooping-concerns-not-true-online-investigation-claims-216-000-000-spy-tvs-record-audio) | ⭐ 170 | 💬 182 | [HN Thread](https://news.ycombinator.com/item?id=49645480) |
| **2** | [Make your first edit to OpenStreetMap](https://high5apps.github.io/josm-plugin-website-wizard/) | ⭐ 116 | 💬 39 | [HN Thread](https://news.ycombinator.com/item?id=49674050) |
| **3** | [Nvidia is the central bank of AI](https://www.economist.com/interactive/briefing/2026/09/03/nvidia-is-the-central-bank-of-ai) | ⭐ 219 | 💬 166 | [HN Thread](https://news.ycombinator.com/item?id=49673098) |
| **4** | [Will There Be a 7G?](https://arxiv.org/abs/2609.01877) | ⭐ 38 | 💬 61 | [HN Thread](https://news.ycombinator.com/item?id=49674498) |
| **5** | [We must pace the frontier](https://darioamodei.com/post/we-must-pace-the-frontier) | ⭐ 314 | 💬 410 | [HN Thread](https://news.ycombinator.com/item?id=49672510) |
| **6** | [IKEA made a mod for Skyrim [video]](https://www.youtube.com/watch?v=iZODN0QUgjI) | ⭐ 479 | 💬 122 | [HN Thread](https://news.ycombinator.com/item?id=49639647) |
| **7** | [Microcode in Intel's 8087 floating-point chip: the scale instruction](https://www.righto.com/2026/09/8087-microcode-reverse-engineering-fscale.html) | ⭐ 50 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=49673580) |
| **8** | [I made a build visualizer to understand Bun's compile times](https://lalitm.com/post/buildprof/) | ⭐ 23 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=49672842) |
| **9** | [google.com/goto: Google's anti-scraping update](https://www.autom.dev/blog/google-search-goto-links) | ⭐ 576 | 💬 455 | [HN Thread](https://news.ycombinator.com/item?id=49668386) |
| **10** | [A Mathematical Framework for Transformer Circuits (2021)](https://transformer-circuits.pub/2021/framework/index.html) | ⭐ 58 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=49672365) |

---

## 🗄️ News Archive

- 📅 [2026-09-12](archive/2026-09-12.md)
- 📅 [2026-09-11](archive/2026-09-11.md)
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

*... and [16 older editions in the archive folder](archive/)*

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
