# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Code Is CRAP [2011]](https://testing.googleblog.com/2011/02/this-code-is-crap.html) | ⭐ 40 | 💬 29 | [HN Thread](https://news.ycombinator.com/item?id=49729228) |
| **2** | [Claude Cowork and chat are now one Claude](https://claude.com/blog/cowork-is-now-claude) | ⭐ 21 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49729412) |
| **3** | [Dream-RSI: Recursive Self-Improvement through Evolving Worlds](https://arxiv.org/abs/2609.14858) | ⭐ 97 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=49726955) |
| **4** | [Small Programming Tricks](https://will-keleher.com/posts/small-programming-tricks-matter/) | ⭐ 64 | 💬 45 | [HN Thread](https://news.ycombinator.com/item?id=49729000) |
| **5** | [Mistral X Mozilla: Private, Multilingual AI Browsing](https://mistral.ai/news/mistral-x-mozilla/) | ⭐ 360 | 💬 118 | [HN Thread](https://news.ycombinator.com/item?id=49723408) |
| **6** | [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) | ⭐ 1701 | 💬 459 | [HN Thread](https://news.ycombinator.com/item?id=49717558) |
| **7** | [Measuring Gauss-Seidel loop-carried dependency and fixing it via loop unrolling](https://loiseaujc.github.io/posts/blog-title/make_gauss_seidel_great_again.html) | ⭐ 12 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49710201) |
| **8** | [Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations](https://github.com/arnegiacomo/fugleramme) | ⭐ 1869 | 💬 222 | [HN Thread](https://news.ycombinator.com/item?id=49711544) |
| **9** | [Tell the speakers that you liked their talks](https://ohhelloana.blog/tell-the-speakers/) | ⭐ 90 | 💬 26 | [HN Thread](https://news.ycombinator.com/item?id=49710903) |
| **10** | [How Big Are Factorials?](https://eli.thegreenplace.net/2026/how-big-are-factorials/) | ⭐ 30 | 💬 13 | [HN Thread](https://news.ycombinator.com/item?id=49712185) |

---

## 🗄️ News Archive

- 📅 [2026-09-16](archive/2026-09-16.md)
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

*... and [20 older editions in the archive folder](archive/)*

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
