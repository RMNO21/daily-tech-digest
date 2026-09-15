# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations](https://github.com/arnegiacomo/fugleramme) | ⭐ 800 | 💬 114 | [HN Thread](https://news.ycombinator.com/item?id=49711544) |
| **2** | [Show HN: Capsule – Single-file web apps that save their data into SQLite](https://withcapsule.app/) | ⭐ 189 | 💬 93 | [HN Thread](https://news.ycombinator.com/item?id=49712278) |
| **3** | [GEFS on OpenBSD: A Early Preview](https://marc.info/?l=openbsd-tech&m=178948744271633&w=2) | ⭐ 29 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=49715590) |
| **4** | [I can't stop thinking about Papua New Guinea](https://notnottalmud.substack.com/p/why-i-cant-stop-thinking-about-papua) | ⭐ 791 | 💬 337 | [HN Thread](https://news.ycombinator.com/item?id=49708431) |
| **5** | [Show HN: Hacking a $20 4G wireless hotspot into a texting device](https://bkovac.github.io/modem-thing/) | ⭐ 127 | 💬 18 | [HN Thread](https://news.ycombinator.com/item?id=49712102) |
| **6** | [The CSS Zen Garden dream, finally shipped](https://josprague.com/blog/the-css-zen-garden-dream-finally-shipped/) | ⭐ 56 | 💬 22 | [HN Thread](https://news.ycombinator.com/item?id=49713262) |
| **7** | [Cartesian – AI 3D Modeling for Design](https://www.formas.ai/cartesian) | ⭐ 51 | 💬 47 | [HN Thread](https://news.ycombinator.com/item?id=49713999) |
| **8** | [Jiga (YC W21) Is Hiring Product Engineer (Remote/US)](https://jiga.io/about-us/?ashby_jid=0b75d72d-c92b-4dca-8062-09d298ada0bd) | ⭐ 1 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49715446) |
| **9** | [Giving up on smart rings](https://notesbylex.com/giving-up-on-smart-rings) | ⭐ 33 | 💬 48 | [HN Thread](https://news.ycombinator.com/item?id=49677648) |
| **10** | [Let's make quality the norm again](https://www.forbrukerradet.no/short-life/) | ⭐ 171 | 💬 159 | [HN Thread](https://news.ycombinator.com/item?id=49710109) |

---

## 🗄️ News Archive

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
- 📅 [2026-09-03](archive/2026-09-03.md)
- 📅 [2026-09-02](archive/2026-09-02.md)

*... and [19 older editions in the archive folder](archive/)*

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
