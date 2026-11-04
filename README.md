# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Kitty 0.50](https://sw.kovidgoyal.net/kitty/changelog/#) | ⭐ 31 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=50362980) |
| **2** | [Jelly Sheet](https://mrdoob.github.io/codevember-2026/01/) | ⭐ 232 | 💬 60 | [HN Thread](https://news.ycombinator.com/item?id=50361268) |
| **3** | [Verification Is Not Knowledge: Science needs more than answers](https://blog.cosmos-institute.org/p/verification-is-not-knowledge) | ⭐ 4 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50363019) |
| **4** | [C++26 Disapproved](https://andreasfertig.com/blog/2026/11/cpp26-dis-failed-how-does-cpp-survive/) | ⭐ 287 | 💬 174 | [HN Thread](https://news.ycombinator.com/item?id=50360164) |
| **5** | [The lost malloc()](https://napcakes.nekoweb.org/posts/malloc/) | ⭐ 29 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=50362466) |
| **6** | [Jailbreaking my car's navigation system just so I can change the time](https://blog.nns.ee/2026/11/02/renault-hack/) | ⭐ 795 | 💬 313 | [HN Thread](https://news.ycombinator.com/item?id=50339288) |
| **7** | [Stringman, an $800 open-source room scale gripper robot](https://neufangled.com/) | ⭐ 586 | 💬 194 | [HN Thread](https://news.ycombinator.com/item?id=50354358) |
| **8** | [The Internals of PostgreSQL](https://www.interdb.jp/pg/index.html) | ⭐ 268 | 💬 21 | [HN Thread](https://news.ycombinator.com/item?id=50358702) |
| **9** | [Show HN: Uncracked City, detective game where you question LLM suspects that lie](https://uncracked.city) | ⭐ 57 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=50358352) |
| **10** | [Distinct cellular and genetic differences in colorectal cancer in young patients](https://www.dana-farber.org/newsroom/news-releases/2026/study-reveals-distinct-cellular-and-genetic-differences-in-colorectal-cancer-in-younger-patients) | ⭐ 66 | 💬 13 | [HN Thread](https://news.ycombinator.com/item?id=50361154) |

---

## 🗄️ News Archive

- 📅 [2026-11-04](archive/2026-11-04.md)
- 📅 [2026-11-03](archive/2026-11-03.md)
- 📅 [2026-11-02](archive/2026-11-02.md)
- 📅 [2026-10-31](archive/2026-10-31.md)
- 📅 [2026-10-30](archive/2026-10-30.md)
- 📅 [2026-10-28](archive/2026-10-28.md)
- 📅 [2026-10-27](archive/2026-10-27.md)
- 📅 [2026-10-26](archive/2026-10-26.md)
- 📅 [2026-10-25](archive/2026-10-25.md)
- 📅 [2026-10-24](archive/2026-10-24.md)
- 📅 [2026-10-23](archive/2026-10-23.md)
- 📅 [2026-10-22](archive/2026-10-22.md)
- 📅 [2026-10-21](archive/2026-10-21.md)
- 📅 [2026-10-20](archive/2026-10-20.md)

*... and [62 older editions in the archive folder](archive/)*

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
