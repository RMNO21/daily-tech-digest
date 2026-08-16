# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Claude: System Prompts](https://platform.claude.com/docs/en/release-notes/system-prompts) | ⭐ 238 | 💬 122 | [HN Thread](https://news.ycombinator.com/item?id=49319556) |
| **2** | [The AI Credit Resale Economy](https://vectoral.com/blog/who-are-the-token-brokers) | ⭐ 78 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=49320611) |
| **3** | [St Lucie Nuclear Reactor Unit 1 manually shutdown, 3 control rods drop into core](https://www.wptv.com/news/treasure-coast/region-st-lucie-county/saint-lucie-nuclear-power-plant-unit-1-manually-shut-down-after-3-control-rods-drop-into-reactor-core) | ⭐ 30 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=49320856) |
| **4** | [Firefox for iOS now has a native adblocker](https://support.mozilla.org/en-US/kb/block-ads-firefox-ios) | ⭐ 214 | 💬 82 | [HN Thread](https://news.ycombinator.com/item?id=49319633) |
| **5** | [A True Telnet BBS on a Casio Calculator](https://ei3lh.eu/2026/08/16/a-true-telnet-bbs-on-a-casio-calculator/) | ⭐ 37 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49319349) |
| **6** | [Show HN: A public AI whose memory is shared across all users](https://wildstatic.com/) | ⭐ 25 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=49319814) |
| **7** | [The weekend is 100 years old](https://www.theguardian.com/money/2026/aug/16/the-weekend-is-100-years-old-skiveday-fridays-and-hybrid-working-ruined-it) | ⭐ 31 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49320984) |
| **8** | [GPS and the Lost Art of Getting Lost](https://www.newyorker.com/news/annals-of-inquiry/gps-and-the-lost-art-of-getting-lost) | ⭐ 10 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=49320673) |
| **9** | [Clamiga: Common Lisp for the Amiga](https://nnamgreb.de/blog/Clamiga+-+Common+Lisp+for+the+Amiga) | ⭐ 10 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49281352) |
| **10** | [A SAT Attack on Tarski's High School Algebra Problem](https://arxiv.org/abs/2608.08421) | ⭐ 46 | 💬 16 | [HN Thread](https://news.ycombinator.com/item?id=49268565) |

---

## 🗄️ News Archive

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
python scraper.py
```

---

<div align="center">
  <sub>Maintained by <a href="https://github.com/RMNO21">RMNO21</a> • Powered by GitHub Actions & Hacker News API</sub>
</div>
