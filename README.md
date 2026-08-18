# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Linux 7.3 improves performance when running out of vRAM](https://pixelcluster.dev/VRAM-Overcommit/) | ⭐ 273 | 💬 85 | [HN Thread](https://news.ycombinator.com/item?id=49342719) |
| **2** | [Google buys crashed airline Spirit's data at auction, because AI](https://www.theregister.com/ai-and-ml/2026/08/18/google-buys-crashed-airline-spirits-data-at-auction-because-ai/5288962) | ⭐ 192 | 💬 113 | [HN Thread](https://news.ycombinator.com/item?id=49343559) |
| **3** | [How Bluesky draws its logo on screenshots](https://timmarinin.net/2026/bluesky-screenshots/) | ⭐ 594 | 💬 375 | [HN Thread](https://news.ycombinator.com/item?id=49338459) |
| **4** | [Teaching my kid to code with a modern MUD](https://tau.dev/2026/08/07/canon) | ⭐ 22 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49272631) |
| **5** | [Rethinking Database Programming](https://acadia.engineering/blog/rethinking-database-programming) | ⭐ 111 | 💬 52 | [HN Thread](https://news.ycombinator.com/item?id=49342530) |
| **6** | [GPT-5.6 Sol Pricing Cut by 50%](https://openrouter.ai/openai/gpt-5.6-sol) | ⭐ 516 | 💬 331 | [HN Thread](https://news.ycombinator.com/item?id=49337602) |
| **7** | [Quake Shareware, a CD-ROM just a little too full](https://fabiensanglard.net/quake_shareware_cd/index.html) | ⭐ 402 | 💬 171 | [HN Thread](https://news.ycombinator.com/item?id=49338328) |
| **8** | [As Wisconsin cities flee Flock, its shared camera network loses value](https://arstechnica.com/tech-policy/2026/08/as-wisconsin-cities-flee-flock-its-shared-camera-network-loses-value/) | ⭐ 44 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=49344114) |
| **9** | [Israel creates fake think tank in likely attempt to dupe AI chatbots](https://responsiblestatecraft.org/israel-influence-chatgpt/) | ⭐ 706 | 💬 410 | [HN Thread](https://news.ycombinator.com/item?id=49337392) |
| **10** | [Finger: Social network that never died](https://en.andros.dev/blog/54572bc7/finger-the-1971-social-network-that-never-died/) | ⭐ 46 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=49342472) |

---

## 🗄️ News Archive

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
