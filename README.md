# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [SpaceX catches the Starship to end Flight 15](https://www.spacex.com/launches/starship-flight-15) | ⭐ 1254 | 💬 851 | [HN Thread](https://news.ycombinator.com/item?id=50500963) |
| **2** | [Why did some Apollo missions carry a grenade launcher?](https://space.stackexchange.com/questions/37775) | ⭐ 33 | 💬 15 | [HN Thread](https://news.ycombinator.com/item?id=50505271) |
| **3** | [Lovable apps expose passport details and more than 200K private messages](https://www.crissyfield.de/research/lovable-en/) | ⭐ 843 | 💬 319 | [HN Thread](https://news.ycombinator.com/item?id=50499017) |
| **4** | [Court denies motion to dismiss DRAM price fixing case](https://litnews.ai/articles/garciaguirre-samsung-sk-hynix-micron-dram-conspiracy-suit-survives-dismissal) | ⭐ 179 | 💬 49 | [HN Thread](https://news.ycombinator.com/item?id=50502988) |
| **5** | [A rare glimpse inside the high-risk, high-reward Hormuz trade](https://www.lloydslist.com/LL1158922/A-rare-glimpse-inside-the-highrisk-highreward-Hormuz-trade) | ⭐ 76 | 💬 53 | [HN Thread](https://news.ycombinator.com/item?id=50443331) |
| **6** | [Handwritten 200-year-old dismissal notice found on roof tile](https://www.bbc.co.uk/news/articles/c6jdmdzv25r9o) | ⭐ 19 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=50474529) |
| **7** | [How did Woz write the Apple 1 BASIC before building the computer?](https://retrocomputing.stackexchange.com/questions/17957) | ⭐ 226 | 💬 111 | [HN Thread](https://news.ycombinator.com/item?id=50501594) |
| **8** | [Semicircle Packing](https://rorz.io/writing/semicircle-packing) | ⭐ 29 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=50484234) |
| **9** | [Disk encryption on NetBSD – achieving secrecy](https://netbsd.org/~nia/disk-encrypt/) | ⭐ 34 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=50504277) |
| **10** | [My favourite modern NES games](https://jordi.inversethought.com/blog/25-of-my-favourite-modern-nes-games/) | ⭐ 93 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=50503465) |

---

## 🗄️ News Archive

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
- 📅 [2026-11-03](archive/2026-11-03.md)
- 📅 [2026-11-02](archive/2026-11-02.md)
- 📅 [2026-10-31](archive/2026-10-31.md)
- 📅 [2026-10-30](archive/2026-10-30.md)

*... and [71 older editions in the archive folder](archive/)*

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
