# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Cloudflare Quick Tunnels](https://try.cloudflare.com/) | ⭐ 374 | 💬 178 | [HN Thread](https://news.ycombinator.com/item?id=49754785) |
| **2** | [Saving another 100TB of RAM with math (and Rust)](https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/) | ⭐ 18 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49758580) |
| **3** | [Photon-Emission-Guided Laser Fault Injection Enables RP2350 Secure Debug](https://donjon.ledger.com/blog/rp2350-secure-debug-laser-fault-injection/) | ⭐ 95 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=49757050) |
| **4** | [Show HN: Cactus Needle 3: 8-29MB automation models can match DeepSeek V4 Flash](https://cactuscompute.com/needle) | ⭐ 99 | 💬 50 | [HN Thread](https://news.ycombinator.com/item?id=49748553) |
| **5** | [Android 17 is the first since 3.x to add new APIs without releasing to the AOSP](https://grapheneos.social/@GrapheneOS/117282080803799576) | ⭐ 9 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49758736) |
| **6** | [US Military had close call after using AI for hallucinated intelligence report](https://www.cnn.com/2026/09/18/politics/us-military-ai-false-intelligence-china-ship) | ⭐ 206 | 💬 125 | [HN Thread](https://news.ycombinator.com/item?id=49757520) |
| **7** | [North Korean nuclear test sets off years of earthquakes](https://www.science.org/content/article/north-korean-nuclear-test-sets-years-earthquakes) | ⭐ 139 | 💬 110 | [HN Thread](https://news.ycombinator.com/item?id=49755160) |
| **8** | [OpenJev](https://openjev.com/) | ⭐ 457 | 💬 227 | [HN Thread](https://news.ycombinator.com/item?id=49752041) |
| **9** | [Cache-to-Cache: Direct Semantic Communication Between Large Language Models](https://arxiv.org/abs/2510.03215) | ⭐ 7 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49758615) |
| **10** | [Systemd is a suite of basic building blocks](https://brand.systemd.io/) | ⭐ 26 | 💬 33 | [HN Thread](https://news.ycombinator.com/item?id=49756762) |

---

## 🗄️ News Archive

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
- 📅 [2026-09-04](archive/2026-09-04.md)

*... and [21 older editions in the archive folder](archive/)*

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
