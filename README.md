# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Nvidia is the central bank of AI](https://www.economist.com/interactive/briefing/2026/09/03/nvidia-is-the-central-bank-of-ai) | ⭐ 132 | 💬 102 | [HN Thread](https://news.ycombinator.com/item?id=49673098) |
| **2** | [Make Your First Edit to OpenStreetMap in the Next 15 Minutes](https://high5apps.github.io/josm-plugin-website-wizard/) | ⭐ 22 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49674050) |
| **3** | [A Mathematical Framework for Transformer Circuits (2021)](https://transformer-circuits.pub/2021/framework/index.html) | ⭐ 47 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49672365) |
| **4** | [IKEA made a mod for Skyrim [video]](https://www.youtube.com/watch?v=iZODN0QUgjI) | ⭐ 436 | 💬 105 | [HN Thread](https://news.ycombinator.com/item?id=49639647) |
| **5** | [Microcode in Intel's 8087 floating-point chip: the scale instruction](https://www.righto.com/2026/09/8087-microcode-reverse-engineering-fscale.html) | ⭐ 17 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49673580) |
| **6** | [Retrospectively Reverse-Engineering Apple's Neural Engine](https://eiln.github.io/posts/ane.html) | ⭐ 184 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=49670032) |
| **7** | [A misalignment of AI in mathematics](https://mathandai.org/) | ⭐ 1133 | 💬 1063 | [HN Thread](https://news.ycombinator.com/item?id=49662371) |
| **8** | [I refuse to let SPICE die](https://github.com/nefarius/vd_agent/) | ⭐ 21 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=49672641) |
| **9** | [I spent $220 on Google app ads and 60% of the installs were robots](https://dayzlegame.com/blog/google-ads-bot-farm/) | ⭐ 693 | 💬 374 | [HN Thread](https://news.ycombinator.com/item?id=49662990) |
| **10** | [Fuck it, make it anyway](https://www.joelotter.com/posts/2026/09/make-it-anyway/) | ⭐ 432 | 💬 392 | [HN Thread](https://news.ycombinator.com/item?id=49671329) |

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
