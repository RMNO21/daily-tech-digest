# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Gemini 4 Argon](https://deepmind.google/models/gemini/) | ⭐ 767 | 💬 607 | [HN Thread](https://news.ycombinator.com/item?id=50073879) |
| **2** | [Show HN: Guitoro, a virtual guitar you strum with your keyboard](https://guitoro.com/) | ⭐ 114 | 💬 33 | [HN Thread](https://news.ycombinator.com/item?id=50077020) |
| **3** | [Ledger confirms spy chip implant behind wallet crypto thefts](https://www.bleepingcomputer.com/news/security/ledger-confirms-hardware-wallet-spy-implant-behind-crypto-thefts/) | ⭐ 237 | 💬 232 | [HN Thread](https://news.ycombinator.com/item?id=50054092) |
| **4** | [Apple HomeView](https://www.apple.com/apple-homeview/) | ⭐ 591 | 💬 725 | [HN Thread](https://news.ycombinator.com/item?id=50071017) |
| **5** | [Redesigning source control at Anthropic](https://www.anthropic.com/engineering/redesigning-source-control) | ⭐ 365 | 💬 356 | [HN Thread](https://news.ycombinator.com/item?id=50073633) |
| **6** | [Thunderbird for iOS](https://blog.thunderbird.net/2026/10/thunderbird-for-ios-a-first-look-at-the-native-iphone-email-app-in-development/) | ⭐ 260 | 💬 97 | [HN Thread](https://news.ycombinator.com/item?id=50072913) |
| **7** | [PostEra (YC W20) Is Hiring AI Researchers for Drug Discovery](https://jobs.lever.co/postera/c7d50a36-db0a-4574-bfe4-8700b74a22c0) | ⭐ 1 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50078686) |
| **8** | [11 year old unsoundness bugs found in Rust borrow checker](https://github.com/rust-lang/rust/issues/164250) | ⭐ 621 | 💬 352 | [HN Thread](https://news.ycombinator.com/item?id=50069499) |
| **9** | [I posted to HN, and then my website was flooded with AI bot traffic](https://www.sammystraus.com/#i-posted-to-hn-and-then-my-website-was-flooded-with-ai-bot-traffic) | ⭐ 193 | 💬 118 | [HN Thread](https://news.ycombinator.com/item?id=50073221) |
| **10** | [Firefox Enterprise](https://www.firefox.com/en-US/enterprise/) | ⭐ 536 | 💬 219 | [HN Thread](https://news.ycombinator.com/item?id=50070302) |

---

## 🗄️ News Archive

- 📅 [2026-10-13](archive/2026-10-13.md)
- 📅 [2026-10-10](archive/2026-10-10.md)
- 📅 [2026-10-09](archive/2026-10-09.md)
- 📅 [2026-10-08](archive/2026-10-08.md)
- 📅 [2026-10-07](archive/2026-10-07.md)
- 📅 [2026-10-05](archive/2026-10-05.md)
- 📅 [2026-10-04](archive/2026-10-04.md)
- 📅 [2026-10-03](archive/2026-10-03.md)
- 📅 [2026-10-02](archive/2026-10-02.md)
- 📅 [2026-10-01](archive/2026-10-01.md)
- 📅 [2026-09-30](archive/2026-09-30.md)
- 📅 [2026-09-29](archive/2026-09-29.md)
- 📅 [2026-09-28](archive/2026-09-28.md)
- 📅 [2026-09-27](archive/2026-09-27.md)

*... and [42 older editions in the archive folder](archive/)*

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
