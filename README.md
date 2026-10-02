# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Pi 1.0](https://earendil.com/posts/pi-1-0/) | ⭐ 999 | 💬 317 | [HN Thread](https://news.ycombinator.com/item?id=49926069) |
| **2** | [DeepSeek Harness](https://www.deepseek.com/en/harness/) | ⭐ 87 | 💬 26 | [HN Thread](https://news.ycombinator.com/item?id=49929489) |
| **3** | [Meta's Muse is fantastic for web scraping](https://sigh.dev/posts/metas-muse-is-fantastic-for-web-scraping/) | ⭐ 17 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=49929970) |
| **4** | [How Singapore's government-run dating service works](https://www.singapore-samizdat.com/p/how-singapores-government-run-dating-service-firstdate-works) | ⭐ 64 | 💬 30 | [HN Thread](https://news.ycombinator.com/item?id=49929113) |
| **5** | [Shimano Bicycle Museum Review](https://inrng.com/2026/10/shimano-bicycle-museum/) | ⭐ 6 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49930047) |
| **6** | [Clef: Open-weight decision models, and new RL fine-tuning platform](https://blog.cloudflare.com/clef-decision-models/) | ⭐ 473 | 💬 170 | [HN Thread](https://news.ycombinator.com/item?id=49923692) |
| **7** | [Several vulnerabilities have been discovered in the Linux kernel](https://lwn.net/Articles/1097401/) | ⭐ 213 | 💬 138 | [HN Thread](https://news.ycombinator.com/item?id=49928121) |
| **8** | [SvelteKit 3](https://svelte.dev/blog/sveltekit-3-is-here) | ⭐ 193 | 💬 63 | [HN Thread](https://news.ycombinator.com/item?id=49926536) |
| **9** | [Automatic Transmission – a data-privacy study of connected vehicles](https://automatictransmission.khoury.northeastern.edu/index.html) | ⭐ 160 | 💬 152 | [HN Thread](https://news.ycombinator.com/item?id=49926628) |
| **10** | [Pi Durable](https://earendil.com/posts/pi-durable/) | ⭐ 301 | 💬 37 | [HN Thread](https://news.ycombinator.com/item?id=49925969) |

---

## 🗄️ News Archive

- 📅 [2026-10-02](archive/2026-10-02.md)
- 📅 [2026-10-01](archive/2026-10-01.md)
- 📅 [2026-09-30](archive/2026-09-30.md)
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

*... and [34 older editions in the archive folder](archive/)*

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
