# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Scientific study reveals TikTok videos deactivate key cognitive brain regions](https://www.rathbiotaclan.com/tiktok-videos-deactivate-key-cognitive-brain-regions/) | ⭐ 215 | 💬 85 | [HN Thread](https://news.ycombinator.com/item?id=49378630) |
| **2** | [Stop Eating Lady Gaga's Oreos](https://www.experimental-history.com/p/stop-eating-lady-gagas-oreos) | ⭐ 56 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=49379253) |
| **3** | [I should have loved biology](https://jsomers.net/i-should-have-loved-biology/) | ⭐ 121 | 💬 49 | [HN Thread](https://news.ycombinator.com/item?id=49377853) |
| **4** | [I like 'em thick: an apology to my English teachers](https://www.experimental-history.com/p/i-like-em-thick) | ⭐ 417 | 💬 202 | [HN Thread](https://news.ycombinator.com/item?id=49347543) |
| **5** | [Show HN: Huzzah – a novel approach to coding with AI](https://www.danielvaughn.dev/posts/huzzah/) | ⭐ 45 | 💬 21 | [HN Thread](https://news.ycombinator.com/item?id=49378768) |
| **6** | [AliExpress runs silent WebAudio fingerprinting that breaks Bluetooth multipoint](https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html) | ⭐ 764 | 💬 258 | [HN Thread](https://news.ycombinator.com/item?id=49372583) |
| **7** | [Consumer Rights Wiki](https://consumerrights.wiki/w/Main_Page) | ⭐ 50 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49378243) |
| **8** | [HTML Can Do That](https://chrisburnell.com/html-can-do-that/) | ⭐ 436 | 💬 120 | [HN Thread](https://news.ycombinator.com/item?id=49362689) |
| **9** | [Linux 7.2](https://www.igalia.com/2026/08/19/Linux-72-Released.html) | ⭐ 133 | 💬 49 | [HN Thread](https://news.ycombinator.com/item?id=49376265) |
| **10** | [CIA funding helped keep NeXT afloat in the 80s](https://www.wsj.com/tech/steve-jobs-apple-next-cia-161b65f9?st=NWWds1&reflink=desktopwebshare_permalink) | ⭐ 264 | 💬 161 | [HN Thread](https://news.ycombinator.com/item?id=49368886) |

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
