# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Kimi K3.1 Pro and K3.1 Pro Highspeed](https://www.kimi.ai/blog/kimi-k3-1-pro) | ⭐ 587 | 💬 356 | [HN Thread](https://news.ycombinator.com/item?id=50212065) |
| **2** | [Apple Music 404 Not Found](https://music.apple.com/this-url-doesnt-exist) | ⭐ 413 | 💬 145 | [HN Thread](https://news.ycombinator.com/item?id=50207910) |
| **3** | [Dessa: the most authentic full-duplex speech model ever built](https://block.xyz/dessa) | ⭐ 123 | 💬 37 | [HN Thread](https://news.ycombinator.com/item?id=50213925) |
| **4** | [Today, we hacked what we'd set out to hack: the iPhone](https://blog.calif.io/p/iphone) | ⭐ 647 | 💬 424 | [HN Thread](https://news.ycombinator.com/item?id=50211474) |
| **5** | [We are all living inside of an obscure sci-fi film from 1970](https://thanksforthatjim.bearblog.dev/we-are-all-living-inside-of-an-obscure-sci-fi-film-from-1970/) | ⭐ 63 | 💬 39 | [HN Thread](https://news.ycombinator.com/item?id=50214323) |
| **6** | [OpenAI: Securing our frontier model training environment](https://openai.com/index/securing-our-frontier-model-training-environment/) | ⭐ 39 | 💬 32 | [HN Thread](https://news.ycombinator.com/item?id=50214416) |
| **7** | [Local Wikipedia: Wikipedia, but only for things a half hour walk from you](https://edjefferson.com/localwiki/) | ⭐ 1153 | 💬 222 | [HN Thread](https://news.ycombinator.com/item?id=50202285) |
| **8** | [The Real Kevin Bacon](https://pudding.cool/2026/10/kevin-bacon/) | ⭐ 196 | 💬 56 | [HN Thread](https://news.ycombinator.com/item?id=50169499) |
| **9** | [CVE Tracker](https://cve.0xosprey.com/) | ⭐ 7 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50215530) |
| **10** | [Canadians are running out of time to oppose Bill C-22](https://www.eff.org/deeplinks/2026/10/canadians-are-running-out-time-oppose-dangerous-c-22-surveillance-bill) | ⭐ 251 | 💬 116 | [HN Thread](https://news.ycombinator.com/item?id=50202114) |

---

## 🗄️ News Archive

- 📅 [2026-10-23](archive/2026-10-23.md)
- 📅 [2026-10-22](archive/2026-10-22.md)
- 📅 [2026-10-21](archive/2026-10-21.md)
- 📅 [2026-10-20](archive/2026-10-20.md)
- 📅 [2026-10-19](archive/2026-10-19.md)
- 📅 [2026-10-18](archive/2026-10-18.md)
- 📅 [2026-10-17](archive/2026-10-17.md)
- 📅 [2026-10-16](archive/2026-10-16.md)
- 📅 [2026-10-15](archive/2026-10-15.md)
- 📅 [2026-10-14](archive/2026-10-14.md)
- 📅 [2026-10-13](archive/2026-10-13.md)
- 📅 [2026-10-10](archive/2026-10-10.md)
- 📅 [2026-10-09](archive/2026-10-09.md)
- 📅 [2026-10-08](archive/2026-10-08.md)

*... and [52 older editions in the archive folder](archive/)*

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
