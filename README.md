# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Claude Code now reads AGENTS.md if there is no Claude.md](https://code.claude.com/docs/en/changelog) | ⭐ 242 | 💬 97 | [HN Thread](https://news.ycombinator.com/item?id=49760187) |
| **2** | [Android 17 is the first since 3.x to add new APIs without releasing to the AOSP](https://grapheneos.social/@GrapheneOS/117282080803799576) | ⭐ 374 | 💬 171 | [HN Thread](https://news.ycombinator.com/item?id=49758736) |
| **3** | [Saving another 100TB of RAM](https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/) | ⭐ 148 | 💬 32 | [HN Thread](https://news.ycombinator.com/item?id=49758580) |
| **4** | [Cloudflare Quick Tunnels](https://try.cloudflare.com/) | ⭐ 495 | 💬 216 | [HN Thread](https://news.ycombinator.com/item?id=49754785) |
| **5** | [Xcode 27.1 Beta Release Notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes) | ⭐ 98 | 💬 55 | [HN Thread](https://news.ycombinator.com/item?id=49758419) |
| **6** | [Cache-to-Cache: Direct Semantic Communication Between LLMs (2025)](https://arxiv.org/abs/2510.03215) | ⭐ 52 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=49758615) |
| **7** | [Photon-Emission-Guided Laser Fault Injection Enables RP2350 Secure Debug](https://donjon.ledger.com/blog/rp2350-secure-debug-laser-fault-injection/) | ⭐ 135 | 💬 41 | [HN Thread](https://news.ycombinator.com/item?id=49757050) |
| **8** | [Show HN: Cactus Needle 3: 8-29MB automation models can match DeepSeek V4 Flash](https://cactuscompute.com/needle) | ⭐ 144 | 💬 71 | [HN Thread](https://news.ycombinator.com/item?id=49748553) |
| **9** | [How to Write with an LLM](https://sockpuppet.org/blog/2026/09/17/how-to-write-with-an-llm/) | ⭐ 341 | 💬 236 | [HN Thread](https://news.ycombinator.com/item?id=49747070) |
| **10** | [OpenJev](https://openjev.com/) | ⭐ 513 | 💬 234 | [HN Thread](https://news.ycombinator.com/item?id=49752041) |

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
