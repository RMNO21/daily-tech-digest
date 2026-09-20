# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Samsung is expected to more than double output of its HBM4 and HBM4E DRAM](https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say) | ⭐ 256 | 💬 179 | [HN Thread](https://news.ycombinator.com/item?id=49778029) |
| **2** | [ChatGPT now knows what you do on other websites via ad collector](https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/) | ⭐ 487 | 💬 280 | [HN Thread](https://news.ycombinator.com/item?id=49776729) |
| **3** | [Qwen Image 2.1](https://qwen.ai/blog?id=qwen-image-2.1) | ⭐ 427 | 💬 145 | [HN Thread](https://news.ycombinator.com/item?id=49775499) |
| **4** | [Nobody pays for FOSS, we can force them to](https://seldo.com/posts/nobody-pays-for-open-source-we-can-force-them-to/) | ⭐ 50 | 💬 23 | [HN Thread](https://news.ycombinator.com/item?id=49780064) |
| **5** | [Pirate Face Rescues LLM Models from Deletion](https://pirateface.co/) | ⭐ 378 | 💬 121 | [HN Thread](https://news.ycombinator.com/item?id=49776699) |
| **6** | [The Effect of CRTs on Pixel Art](https://datagubbe.se/crt/) | ⭐ 35 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49768336) |
| **7** | [Apple iPhone 18 Pro Camera test](https://www.dxomark.com/apple-iphone-18-pro-camera-test/) | ⭐ 79 | 💬 92 | [HN Thread](https://news.ycombinator.com/item?id=49771218) |
| **8** | [Singapore’s National Library Board offers micropayments to build reading habits](https://www.gadgetreview.com/singapore-is-paying-people-to-put-down-their-phones-and-read-books) | ⭐ 154 | 💬 65 | [HN Thread](https://news.ycombinator.com/item?id=49776717) |
| **9** | [A Necessary History of the Oddest Letter: W](https://lithub.com/a-necessary-history-of-the-oddest-letter-w/) | ⭐ 74 | 💬 43 | [HN Thread](https://news.ycombinator.com/item?id=49778195) |
| **10** | [Nipple tattooist 'frustrated' by online censorship](https://www.bbc.com/news/articles/cx2z7ejn891o) | ⭐ 13 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=49780466) |

---

## 🗄️ News Archive

- 📅 [2026-09-20](archive/2026-09-20.md)
- 📅 [2026-09-19](archive/2026-09-19.md)
- 📅 [2026-09-18](archive/2026-09-18.md)
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

*... and [23 older editions in the archive folder](archive/)*

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
