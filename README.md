# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [San Francisco Onion Futures Company](https://onionfutures.com/) | ⭐ 106 | 💬 32 | [HN Thread](https://news.ycombinator.com/item?id=49763296) |
| **2** | [Android 17 is the first since 3.x to add new APIs without releasing to the AOSP](https://grapheneos.social/@GrapheneOS/117282080803799576) | ⭐ 721 | 💬 353 | [HN Thread](https://news.ycombinator.com/item?id=49758736) |
| **3** | [Typesafe-computer-use drives a Mac toward a goal for 1/50th of a cent per step](https://github.com/awlevin/typesafe-computer-use) | ⭐ 36 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=49733647) |
| **4** | [SDCC – Small Device C Compiler](https://sdcc.sourceforge.net/) | ⭐ 44 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=49762744) |
| **5** | [Science Is Open Software](https://jepedersen.dk/blog/202505_research/) | ⭐ 50 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=49762687) |
| **6** | [How OpenAI Used Its Own LLMs to Design Its Jalapeño Chip](https://spectrum.ieee.org/llms-for-chip-design) | ⭐ 98 | 💬 73 | [HN Thread](https://news.ycombinator.com/item?id=49761432) |
| **7** | [Cloudflare Quick Tunnels](https://try.cloudflare.com/) | ⭐ 657 | 💬 272 | [HN Thread](https://news.ycombinator.com/item?id=49754785) |
| **8** | [Saving another 100TB of RAM](https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/) | ⭐ 304 | 💬 58 | [HN Thread](https://news.ycombinator.com/item?id=49758580) |
| **9** | [Why building a Rust LSP is hard](https://rust-glancer.github.io/blog/why-lsp-is-hard/) | ⭐ 36 | 💬 18 | [HN Thread](https://news.ycombinator.com/item?id=49734131) |
| **10** | [How to Write with an LLM](https://sockpuppet.org/blog/2026/09/17/how-to-write-with-an-llm/) | ⭐ 457 | 💬 307 | [HN Thread](https://news.ycombinator.com/item?id=49747070) |

---

## 🗄️ News Archive

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
- 📅 [2026-09-05](archive/2026-09-05.md)

*... and [22 older editions in the archive folder](archive/)*

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
