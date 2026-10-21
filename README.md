# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Updated PHP version released to GitHub](https://github.com/php/php-src/releases/tag/php-8.2.35) | ⭐ 33 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=50180873) |
| **2** | [Eight Bits of Trust; eMudhra's CA keys cracked in milliseconds](https://scotthelme.co.uk/eight-bits-of-trust-emudhras-ca-keys-cracked-in-milliseconds/) | ⭐ 420 | 💬 182 | [HN Thread](https://news.ycombinator.com/item?id=50177916) |
| **3** | [Qwen3-Coder writes less secure code when told it's for a US persona](https://www.hirundo.io/blog/qwen3-coder-vulnerabilities) | ⭐ 103 | 💬 44 | [HN Thread](https://news.ycombinator.com/item?id=50179706) |
| **4** | [Most advice is right for the person giving it](https://coached.com/essays/most-advice-is-right-for-the-person-giving-it/) | ⭐ 26 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=50180444) |
| **5** | [LayerFS: The filesystem for AI coding agents](https://layerfs.ai/) | ⭐ 24 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=50179857) |
| **6** | [Whatever Happened to Fire Escapes](https://practical.engineering/blog/2026/10/20/whatever-happened-to-fire-escapes) | ⭐ 91 | 💬 49 | [HN Thread](https://news.ycombinator.com/item?id=50178455) |
| **7** | [The Future of CSS](https://www.joshwcomeau.com/css/interop-2027/) | ⭐ 482 | 💬 200 | [HN Thread](https://news.ycombinator.com/item?id=50175070) |
| **8** | [Upcoming critical PHP security release (CVE-2026-109618 / -109619)](https://news-web.php.net/php.announce/509) | ⭐ 1330 | 💬 549 | [HN Thread](https://news.ycombinator.com/item?id=50172041) |
| **9** | [Dutch National Cyber Security Center is Offline because it uses PHP](https://www.ncsc.nl/actueel) | ⭐ 173 | 💬 60 | [HN Thread](https://news.ycombinator.com/item?id=50179828) |
| **10** | [9 Mothers (YC P26) Is Hiring in Austin, TX](https://9mothers.com/careers) | ⭐ 1 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50179455) |

---

## 🗄️ News Archive

- 📅 [2026-10-21](archive/2026-10-21.md)
- 📅 [2026-10-20](archive/2026-10-20.md)
- 📅 [2026-10-19](archive/2026-10-19.md)
- 📅 [2026-10-18](archive/2026-10-18.md)
- 📅 [2026-10-17](archive/2026-10-17.md)
- 📅 [2026-10-16](archive/2026-10-16.md)
- 📅 [2026-10-15](archive/2026-10-15.md)
- 📅 [2026-10-14](archive/2026-10-14.md)
- 📅 [2026-10-13](archive/2026-10-13.md)
- 📅 [2026-10-10](archive/2026-10-10.md)
- 📅 [2026-10-09](archive/2026-10-09.md)
- 📅 [2026-10-08](archive/2026-10-08.md)
- 📅 [2026-10-07](archive/2026-10-07.md)
- 📅 [2026-10-05](archive/2026-10-05.md)

*... and [50 older editions in the archive folder](archive/)*

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
