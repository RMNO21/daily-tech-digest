# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Xiaomi: New CPU matches Apple cores single threaded, much faster multithreaded](https://twitter.com/lemire/status/2091894299289874926) | ⭐ 237 | 💬 134 | [HN Thread](https://news.ycombinator.com/item?id=49420873) |
| **2** | [MS Paint and Photos inivisibly watermark even locally generated output with GUID](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) | ⭐ 104 | 💬 46 | [HN Thread](https://news.ycombinator.com/item?id=49421158) |
| **3** | [IPFS Maintainers Winding Down](https://ipshipyard.com/blog/2026-the-end-of-ipfs-at-shipyard/) | ⭐ 65 | 💬 15 | [HN Thread](https://news.ycombinator.com/item?id=49421489) |
| **4** | [OpenAI: GPT 5.6 Sol price reduction (until at least Nov 21)](https://developers.openai.com/api/docs/pricing) | ⭐ 101 | 💬 83 | [HN Thread](https://news.ycombinator.com/item?id=49421074) |
| **5** | [How Europe is killing makers and micro-entrepreneurs](https://lectronz.com/u/lectronz/articles/how-europe-is-killing-makers-and-micro-entrepreneurs) | ⭐ 590 | 💬 407 | [HN Thread](https://news.ycombinator.com/item?id=49419237) |
| **6** | [Coding expertise is going to collapse from AI reliance](https://larsfaye.com/articles/ai-coding-will-prevent-expertise) | ⭐ 89 | 💬 92 | [HN Thread](https://news.ycombinator.com/item?id=49421554) |
| **7** | [SeL4 security proofs now complete on AArch64](https://proofcraft.systems/news-2026/#2026-08-21) | ⭐ 127 | 💬 30 | [HN Thread](https://news.ycombinator.com/item?id=49418255) |
| **8** | [Hot Chips 2026: Applying High Bandwidth Flash (HBF)](https://chipsandcheese.com/p/hot-chips-2026-applying-high-bandwidth) | ⭐ 26 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=49420592) |
| **9** | [a Blackstone real estate company exposed SSN digits, DOBs, addresses and more](https://alexschapiro.com/security/vulnerability/2026/07/16/beam-living-graphql-data-exposure) | ⭐ 8 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49422204) |
| **10** | [I were 17, I'd learn how to build LLMs from scratch](https://twitter.com/paulg/status/2091544343589060625) | ⭐ 379 | 💬 499 | [HN Thread](https://news.ycombinator.com/item?id=49412396) |

---

## 🗄️ News Archive

- 📅 [2026-08-24](archive/2026-08-24.md)
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
