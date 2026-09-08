# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Among European Companies That Use a CDN, Nearly 9 in 10 Use Cloudflare](https://ciphercue.com/blog/european-cdn-concentration-cloudflare-nine-in-ten) | ⭐ 48 | 💬 50 | [HN Thread](https://news.ycombinator.com/item?id=49607443) |
| **2** | [I've factored the RSA keys of a Certificate Authority from the 90s](https://mcpherrin.ca/2026/09/07/rsa.html) | ⭐ 328 | 💬 56 | [HN Thread](https://news.ycombinator.com/item?id=49604637) |
| **3** | [We built our house for LAN parties](https://lanparty.house/) | ⭐ 75 | 💬 29 | [HN Thread](https://news.ycombinator.com/item?id=49579443) |
| **4** | [Mistral raises €3B](https://mistral.ai/news/mistral-makes-sovereign-open-weight-ai-to-frontier/) | ⭐ 442 | 💬 307 | [HN Thread](https://news.ycombinator.com/item?id=49605767) |
| **5** | [There's a new "Google Jail" for independent wikis](https://weirdgloop.org/blog/google-jail) | ⭐ 137 | 💬 47 | [HN Thread](https://news.ycombinator.com/item?id=49604870) |
| **6** | [Multi-Agents LLM Financial Trading Framework](https://github.com/TauricResearch/TradingAgents) | ⭐ 47 | 💬 32 | [HN Thread](https://news.ycombinator.com/item?id=49605822) |
| **7** | [TALA Is Open-Source](https://d2lang.com/blog/tala-is-open-source/) | ⭐ 222 | 💬 15 | [HN Thread](https://news.ycombinator.com/item?id=49604150) |
| **8** | [How well do agents use test/verification techniques?](https://danluu.com/agentic-testing/) | ⭐ 84 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=49605246) |
| **9** | [Arm Mali G2-Ultra NX GPU: desktop-class mobile gameplay with AI-native graphics](https://newsroom.arm.com/blog/arm-mali-g2-ultra-nx-ai-native-mobile-graphics) | ⭐ 41 | 💬 23 | [HN Thread](https://news.ycombinator.com/item?id=49605511) |
| **10** | [We have a year to fix security everywhere](https://jyn.dev/a-year-to-fix-security/) | ⭐ 225 | 💬 190 | [HN Thread](https://news.ycombinator.com/item?id=49605691) |

---

## 🗄️ News Archive

- 📅 [2026-09-08](archive/2026-09-08.md)
- 📅 [2026-09-07](archive/2026-09-07.md)
- 📅 [2026-09-06](archive/2026-09-06.md)
- 📅 [2026-09-05](archive/2026-09-05.md)
- 📅 [2026-09-04](archive/2026-09-04.md)
- 📅 [2026-09-03](archive/2026-09-03.md)
- 📅 [2026-09-02](archive/2026-09-02.md)
- 📅 [2026-09-01](archive/2026-09-01.md)
- 📅 [2026-08-31](archive/2026-08-31.md)
- 📅 [2026-08-30](archive/2026-08-30.md)
- 📅 [2026-08-29](archive/2026-08-29.md)
- 📅 [2026-08-28](archive/2026-08-28.md)
- 📅 [2026-08-27](archive/2026-08-27.md)
- 📅 [2026-08-26](archive/2026-08-26.md)

*... and [12 older editions in the archive folder](archive/)*

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
