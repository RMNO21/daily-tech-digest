# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Don't Paste the AI, please](https://dontpastetheai.com/) | ⭐ 622 | 💬 302 | [HN Thread](https://news.ycombinator.com/item?id=49371857) |
| **2** | [AliExpress runs silent WebAudio fingerprinting that breaks Bluetooth multipoint](https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html) | ⭐ 198 | 💬 62 | [HN Thread](https://news.ycombinator.com/item?id=49372583) |
| **3** | [Show HN: I trained a 125M model to autocomplete piano on-device](https://simedw.com/2026/08/20/midi-autocomplete/) | ⭐ 40 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=49373456) |
| **4** | [Windows brings out the Rorschach test in everyone (2003)](https://devblogs.microsoft.com/oldnewthing/20030825-00/?p=42803) | ⭐ 254 | 💬 97 | [HN Thread](https://news.ycombinator.com/item?id=49371006) |
| **5** | [OpenRouter is joining Stripe](https://openrouter.ai/blog/announcements/openrouter-is-joining-stripe/) | ⭐ 896 | 💬 458 | [HN Thread](https://news.ycombinator.com/item?id=49364559) |
| **6** | [Turns are Better than Radians (2022)](https://www.computerenhance.com/p/turns-are-better-than-radians) | ⭐ 252 | 💬 134 | [HN Thread](https://news.ycombinator.com/item?id=49369408) |
| **7** | [Google has stopped pushing Git tags for some Android source code](https://grapheneos.social/@GrapheneOS/117057099753905023) | ⭐ 682 | 💬 265 | [HN Thread](https://news.ycombinator.com/item?id=49364745) |
| **8** | [Proof of Human (YC S23) Is Hiring a Member of Technical Staff](https://www.ycombinator.com/companies/proof-of-human/jobs/ZTZHEbb-member-of-technical-staff) | ⭐ 1 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49373423) |
| **9** | [Go 1.27](https://go.dev/blog/go1.27) | ⭐ 695 | 💬 212 | [HN Thread](https://news.ycombinator.com/item?id=49365405) |
| **10** | [A faster way to calculate the day of the week](https://www.benjoffe.com/fast-day-of-week) | ⭐ 196 | 💬 46 | [HN Thread](https://news.ycombinator.com/item?id=49323795) |

---

## 🗄️ News Archive

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
