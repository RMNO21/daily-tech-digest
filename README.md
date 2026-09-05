# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [The "$60 Gaming PC" – AMD BC-250 (2025)](https://devquasar.com/hardware/the-60-gaming-pc-amd-bc-250/) | ⭐ 106 | 💬 31 | [HN Thread](https://news.ycombinator.com/item?id=49576386) |
| **2** | [Actively exploited sandbox RCE in all Chromium versions](https://nvd.nist.gov/vuln/detail/cve-2026-85046) | ⭐ 645 | 💬 363 | [HN Thread](https://news.ycombinator.com/item?id=49570669) |
| **3** | [Discovery of a new OpenAI agent message board](https://collusion.wiki/) | ⭐ 1883 | 💬 1435 | [HN Thread](https://news.ycombinator.com/item?id=49563355) |
| **4** | [How the Planet-Altering Disaster of "Forever Chemicals" Was Kept Secret](https://www.propublica.org/podcast/forever-chemicals-pfas-pfos-3m-secret-kris-hansen) | ⭐ 71 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=49576986) |
| **5** | [Nitter has more working instances than before the takedowns](https://codeberg.org/mv12star/shitter/wiki/Instances) | ⭐ 425 | 💬 173 | [HN Thread](https://news.ycombinator.com/item?id=49571634) |
| **6** | [Terpstra Keyboard](http://terpstrakeyboard.com/) | ⭐ 53 | 💬 22 | [HN Thread](https://news.ycombinator.com/item?id=49575150) |
| **7** | [Formalizing Fermat's Last Theorem](https://www.anthropic.com/research/formalizing-fermats-last-theorem) | ⭐ 685 | 💬 431 | [HN Thread](https://news.ycombinator.com/item?id=49568506) |
| **8** | [Git hosting that never leaves Europe](https://pushin.eu) | ⭐ 191 | 💬 99 | [HN Thread](https://news.ycombinator.com/item?id=49573680) |
| **9** | [Global warming will exceed 1.5-degree limit, UN says](https://www.pbs.org/newshour/science/global-warming-will-exceed-1-5-degree-limit-un-says-in-report-that-maps-path-back-below-danger-zone) | ⭐ 208 | 💬 181 | [HN Thread](https://news.ycombinator.com/item?id=49576124) |
| **10** | [Claude's new system prompt doesn't want to reproduce song lyrics](https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/) | ⭐ 47 | 💬 29 | [HN Thread](https://news.ycombinator.com/item?id=49575143) |

---

## 🗄️ News Archive

- 📅 [2026-09-05](archive/2026-09-05.md)
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

*... and [9 older editions in the archive folder](archive/)*

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
