# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [I turned my security cameras into an automatic bird identification system](https://jasontucker.blog/how-i-turned-my-security-cameras-into-an-automatic-bird-identification-system-with-birdnet-go/) | ⭐ 278 | 💬 76 | [HN Thread](https://news.ycombinator.com/item?id=49511856) |
| **2** | [A walkable ASCII cyberpunk city in one HTML file [video]](https://www.youtube.com/watch?v=3YtygAx_C6A) | ⭐ 130 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=49512975) |
| **3** | [Playa Phone](https://playaphone.com/) | ⭐ 404 | 💬 156 | [HN Thread](https://news.ycombinator.com/item?id=49510514) |
| **4** | ['Mad honey' that can stop your heart is being sold online](https://phys.org/news/2026-08-mad-honey-heart-sold-online.html) | ⭐ 30 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=49476239) |
| **5** | [Show HN: Laser Graffiti](https://laser.consti.de) | ⭐ 77 | 💬 16 | [HN Thread](https://news.ycombinator.com/item?id=49489376) |
| **6** | [Smartphone LED detects hidden cameras with AI](https://www.chosun.com/english/industry-en/2026/08/30/SBFXUIJQYZEARKP5T4FBAY25HQ/) | ⭐ 90 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=49496292) |
| **7** | [Autonomous (YC F25) Is Hiring Engineers](https://news.ycombinator.com/item?id=49514781) | ⭐ 1 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49514781) |
| **8** | [Terence Tao explains 6 essential mathematical concepts [video]](https://www.youtube.com/watch?v=OOMx2BHHWtE) | ⭐ 81 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49503521) |
| **9** | [Dwarf Fortress is getting the mother of all magic updates](https://www.rockpapershotgun.com/dwarf-fortress-is-getting-the-mother-of-all-magic-updates-extending-to-the-fundamental-cosmological-makeup-of-the-universe) | ⭐ 212 | 💬 74 | [HN Thread](https://news.ycombinator.com/item?id=49467636) |
| **10** | [Tmp.0ut, Vol. 5](https://tmpout.sh/5/) | ⭐ 91 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49433481) |

---

## 🗄️ News Archive

- 📅 [2026-08-31](archive/2026-08-31.md)
- 📅 [2026-08-30](archive/2026-08-30.md)
- 📅 [2026-08-29](archive/2026-08-29.md)
- 📅 [2026-08-28](archive/2026-08-28.md)
- 📅 [2026-08-27](archive/2026-08-27.md)
- 📅 [2026-08-26](archive/2026-08-26.md)
- 📅 [2026-08-25](archive/2026-08-25.md)
- 📅 [2026-08-24](archive/2026-08-24.md)
- 📅 [2026-08-23](archive/2026-08-23.md)
- 📅 [2026-08-22](archive/2026-08-22.md)
- 📅 [2026-08-21](archive/2026-08-21.md)
- 📅 [2026-08-20](archive/2026-08-20.md)
- 📅 [2026-08-19](archive/2026-08-19.md)
- 📅 [2026-08-18](archive/2026-08-18.md)

*... and [4 older editions in the archive folder](archive/)*

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
