# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Malware infects Android-based automotive head unit firmware](https://securelist.com/android-head-unit-malware/121106/) | ⭐ 141 | 💬 53 | [HN Thread](https://news.ycombinator.com/item?id=49408550) |
| **2** | [How Complex Systems Fail](https://how.complexsystems.fail/) | ⭐ 44 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49409473) |
| **3** | [My favorite nonfiction books about cults, scams, and schemes](https://bookdna.com/best-books/nonfiction-about-cults-scams-and-schemes) | ⭐ 85 | 💬 21 | [HN Thread](https://news.ycombinator.com/item?id=49408858) |
| **4** | [I spent $266 and four AI models to own my tablet. GLM-5.3 finished it in a day](https://ericpardee.github.io/fire-hd-ownership/) | ⭐ 87 | 💬 29 | [HN Thread](https://news.ycombinator.com/item?id=49409073) |
| **5** | [Coconut Oil Jet Fuel Matches Kerosene's Efficiency in Engine Tests](https://studyfinds.com/coconut-oil-jet-fuel-matches-kerosenes-efficiency-in-engine-tests/) | ⭐ 7 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49409780) |
| **6** | [Things I want in a modern relational query language](https://sporks.space/2026/08/19/things-i-want-in-a-modern-relational-query-language/) | ⭐ 42 | 💬 27 | [HN Thread](https://news.ycombinator.com/item?id=49402491) |
| **7** | [Slovakia finds Russian backdoor in traffic speed cameras](https://risky.biz/risky-bulletin-slovakia-finds-russian-backdoor-in-traffic-speed-cameras/) | ⭐ 102 | 💬 39 | [HN Thread](https://news.ycombinator.com/item?id=49409200) |
| **8** | [To become a better writer, read as much as you can](https://nappertime.com/the-golden-rule-of-becoming-a-better-writer/) | ⭐ 353 | 💬 226 | [HN Thread](https://news.ycombinator.com/item?id=49405870) |
| **9** | [What Is a Harness?](https://earendil.com/posts/what-is-a-harness/) | ⭐ 90 | 💬 60 | [HN Thread](https://news.ycombinator.com/item?id=49409092) |
| **10** | [The End of an Athlon](http://www.os2museum.com/wp/the-end-of-an-athlon/) | ⭐ 154 | 💬 62 | [HN Thread](https://news.ycombinator.com/item?id=49406333) |

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
