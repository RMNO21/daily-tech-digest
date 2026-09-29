# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [U.S. postal inspectors shut down website selling counterfeit postage labels](https://postalemployeenetwork.com/news/2026/09/26/u-s-postal-inspectors-shut-down-website-selling-millions-of-counterfeit-postage-labels/) | ⭐ 37 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=49899090) |
| **2** | [Tcl/Tk 9.1 Released](https://www.tcl-lang.org/software/tcltk/9.1.html) | ⭐ 173 | 💬 49 | [HN Thread](https://news.ycombinator.com/item?id=49896712) |
| **3** | [GPT 6.1 Sol: Near-Astra intelligence for a fifth of the price](https://openai.com/index/introducing-gpt-6-1-sol/) | ⭐ 618 | 💬 541 | [HN Thread](https://news.ycombinator.com/item?id=49896586) |
| **4** | [How Delhi cut electricity loss from 50 to 5 percent](https://spectrum.ieee.org/delhi-electricity-loss) | ⭐ 383 | 💬 213 | [HN Thread](https://news.ycombinator.com/item?id=49892245) |
| **5** | [PS5 Relapse Exploit](https://github.com/ntfargo/Relapse-Exploit) | ⭐ 156 | 💬 79 | [HN Thread](https://news.ycombinator.com/item?id=49895304) |
| **6** | [Nicholas Polson has authored 258 academic papers in 2026 (so far)](https://statmodeling.stat.columbia.edu/2026/08/27/258/) | ⭐ 82 | 💬 53 | [HN Thread](https://news.ycombinator.com/item?id=49898877) |
| **7** | [DraftKings Is Using AI to Behaviorally Target Chronic Gamblers](https://www.eff.org/deeplinks/2026/09/draftkings-using-ai-supercharge-harms-online-behavioral-advertising) | ⭐ 442 | 💬 304 | [HN Thread](https://news.ycombinator.com/item?id=49896050) |
| **8** | [AI needs $6T in annual revenue to justify data centre boom](https://www.thenationalnews.com/future/technology/2026/09/29/ai-industry-needs-to-earn-6-trillion-by-2031-to-justify-data-centres/) | ⭐ 129 | 💬 106 | [HN Thread](https://news.ycombinator.com/item?id=49898952) |
| **9** | [NAND-16: a computer built from 277,248 NAND gates](https://somethingbig.ai/computer) | ⭐ 60 | 💬 29 | [HN Thread](https://news.ycombinator.com/item?id=49871018) |
| **10** | [Dots: Always-on agents](https://openai.com/index/introducing-dots/) | ⭐ 375 | 💬 280 | [HN Thread](https://news.ycombinator.com/item?id=49896604) |

---

## 🗄️ News Archive

- 📅 [2026-09-29](archive/2026-09-29.md)
- 📅 [2026-09-28](archive/2026-09-28.md)
- 📅 [2026-09-27](archive/2026-09-27.md)
- 📅 [2026-09-26](archive/2026-09-26.md)
- 📅 [2026-09-25](archive/2026-09-25.md)
- 📅 [2026-09-24](archive/2026-09-24.md)
- 📅 [2026-09-22](archive/2026-09-22.md)
- 📅 [2026-09-21](archive/2026-09-21.md)
- 📅 [2026-09-20](archive/2026-09-20.md)
- 📅 [2026-09-19](archive/2026-09-19.md)
- 📅 [2026-09-18](archive/2026-09-18.md)
- 📅 [2026-09-16](archive/2026-09-16.md)
- 📅 [2026-09-15](archive/2026-09-15.md)
- 📅 [2026-09-14](archive/2026-09-14.md)

*... and [31 older editions in the archive folder](archive/)*

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
