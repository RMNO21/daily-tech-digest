# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [How the European Commission rolled out Matrix to more than 40k staff](https://element.io/blog/how-the-european-commission-rolled-out-matrix-to-more-than-40-000-staff/) | ⭐ 205 | 💬 71 | [HN Thread](https://news.ycombinator.com/item?id=50558533) |
| **2** | [The AI Superintelligence Debate Has Serious Flaws](https://spectrum.ieee.org/ai-superintelligence-debate) | ⭐ 42 | 💬 21 | [HN Thread](https://news.ycombinator.com/item?id=50559140) |
| **3** | [What's New in PHP 8.6](https://www.php.net/releases/8.6/en.php) | ⭐ 130 | 💬 61 | [HN Thread](https://news.ycombinator.com/item?id=50557870) |
| **4** | [Ruby2ßhell: Pre-authentication RCE on stock Rails](https://verialabs.com/ruby2shell/) | ⭐ 221 | 💬 87 | [HN Thread](https://news.ycombinator.com/item?id=50556287) |
| **5** | [Garage Door Spam](https://blog.harrison.page/garage-door-spam/) | ⭐ 104 | 💬 37 | [HN Thread](https://news.ycombinator.com/item?id=50519231) |
| **6** | [Distributed, high-performance blob storage on SQLite](https://zerodha.tech/blog/high-performance-distributed-blob-storage/) | ⭐ 119 | 💬 21 | [HN Thread](https://news.ycombinator.com/item?id=50557537) |
| **7** | [Nintendo takes Picofly firmware down from GitHub [video]](https://www.youtube.com/watch?v=-TLCGUpoD6c) | ⭐ 30 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=50547048) |
| **8** | [Gemini 4 Neon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/) | ⭐ 892 | 💬 702 | [HN Thread](https://news.ycombinator.com/item?id=50552424) |
| **9** | [SSD prices will start going down the second half of next year](https://www.drivevault.io/blog/when-will-hard-drive-prices-come-down.html) | ⭐ 147 | 💬 116 | [HN Thread](https://news.ycombinator.com/item?id=50557716) |
| **10** | [Mass launched to orbit each year by rocket builder](https://www.kadoa.com/companies/insights/spacex-europe-payload) | ⭐ 19 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=50546221) |

---

## 🗄️ News Archive

- 📅 [2026-11-19](archive/2026-11-19.md)
- 📅 [2026-11-18](archive/2026-11-18.md)
- 📅 [2026-11-17](archive/2026-11-17.md)
- 📅 [2026-11-16](archive/2026-11-16.md)
- 📅 [2026-11-15](archive/2026-11-15.md)
- 📅 [2026-11-14](archive/2026-11-14.md)
- 📅 [2026-11-11](archive/2026-11-11.md)
- 📅 [2026-11-10](archive/2026-11-10.md)
- 📅 [2026-11-09](archive/2026-11-09.md)
- 📅 [2026-11-08](archive/2026-11-08.md)
- 📅 [2026-11-07](archive/2026-11-07.md)
- 📅 [2026-11-06](archive/2026-11-06.md)
- 📅 [2026-11-05](archive/2026-11-05.md)
- 📅 [2026-11-04](archive/2026-11-04.md)

*... and [75 older editions in the archive folder](archive/)*

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
