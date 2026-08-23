# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [How I Find Problems to Solve as a Staff Engineer](https://lalitm.com/post/find-problems-staff-engineer/) | ⭐ 43 | 💬 21 | [HN Thread](https://news.ycombinator.com/item?id=49411643) |
| **2** | [A website for debloated open source alternatives](https://debloat.dev/) | ⭐ 149 | 💬 62 | [HN Thread](https://news.ycombinator.com/item?id=49410362) |
| **3** | [Fable and the End of the Free Lunch](https://www.dbreunig.com/2026/08/23/fable-the-end-of-moore-s-law.html) | ⭐ 30 | 💬 15 | [HN Thread](https://news.ycombinator.com/item?id=49411468) |
| **4** | [How Complex Systems Fail (1998)](https://how.complexsystems.fail/) | ⭐ 163 | 💬 45 | [HN Thread](https://news.ycombinator.com/item?id=49409473) |
| **5** | [Why Sal Khan't: On Learning by Making but Teaching by Telling](https://punyamishra.com/2026/04/16/why-sal-khant-on-learning-by-making-but-teaching-by-telling/) | ⭐ 82 | 💬 51 | [HN Thread](https://news.ycombinator.com/item?id=49409862) |
| **6** | [The Vibe Tax](https://insufferable.dev/posts/vibe-tax/) | ⭐ 18 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49411199) |
| **7** | [Malware infects Android-based automotive head unit firmware](https://securelist.com/android-head-unit-malware/121106/) | ⭐ 179 | 💬 85 | [HN Thread](https://news.ycombinator.com/item?id=49408550) |
| **8** | [My favorite nonfiction books about cults, scams, and schemes](https://bookdna.com/best-books/nonfiction-about-cults-scams-and-schemes) | ⭐ 152 | 💬 58 | [HN Thread](https://news.ycombinator.com/item?id=49408858) |
| **9** | [What Is a Harness?](https://earendil.com/posts/what-is-a-harness/) | ⭐ 192 | 💬 102 | [HN Thread](https://news.ycombinator.com/item?id=49409092) |
| **10** | [Coconut Oil Jet Fuel Matches Kerosene's Efficiency in Engine Tests](https://studyfinds.com/coconut-oil-jet-fuel-matches-kerosenes-efficiency-in-engine-tests/) | ⭐ 102 | 💬 90 | [HN Thread](https://news.ycombinator.com/item?id=49409780) |

---

## 🗄️ News Archive

- 📅 [2026-08-23](archive/2026-08-23.md)
- 📅 [2026-08-22](archive/2026-08-22.md)
- 📅 [2026-08-21](archive/2026-08-21.md)
- 📅 [2026-08-20](archive/2026-08-20.md)
- 📅 [2026-08-19](archive/2026-08-19.md)
- 📅 [2026-08-18](archive/2026-08-18.md)
- 📅 [2026-08-17](archive/2026-08-17.md)
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
