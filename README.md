# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Canada suspends trade negotiations with USA and match tariffs dollar for dollar](https://www.pm.gc.ca/en/news/statements/2026/08/21/statement-prime-minister-carney-canada-us-trade-negotiations) | ⭐ 354 | 💬 225 | [HN Thread](https://news.ycombinator.com/item?id=49398304) |
| **2** | [Munder Difflin – Agent harness to run an office of your clones](https://munderdiffl.in/) | ⭐ 52 | 💬 19 | [HN Thread](https://news.ycombinator.com/item?id=49398152) |
| **3** | [Z80–The 1970s Microprocessor Still Alive](https://www.computer.org/csdl/magazine/mi/2021/06/09623402/1yJTvlRLmhi) | ⭐ 36 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=49398158) |
| **4** | [Rust Glancer: Rust LSP using 100x less RAM](https://rust-glancer.github.io/blog/hello-world/) | ⭐ 301 | 💬 58 | [HN Thread](https://news.ycombinator.com/item?id=49393052) |
| **5** | [Felony Bench](https://www.felonybench.com/) | ⭐ 752 | 💬 281 | [HN Thread](https://news.ycombinator.com/item?id=49389430) |
| **6** | [Kobo can run apps now](https://bandarlabs.github.io/Cobalt/) | ⭐ 584 | 💬 191 | [HN Thread](https://news.ycombinator.com/item?id=49390427) |
| **7** | [Felony charges for citizen deleting phone data at US Border](https://www.nytimes.com/2026/08/21/us/politics/samuel-tunick-deleted-phone-felony.html) | ⭐ 859 | 💬 985 | [HN Thread](https://news.ycombinator.com/item?id=49386895) |
| **8** | [There's no reason for software to be slow anymore](https://danluu.com/perf-opt/) | ⭐ 486 | 💬 336 | [HN Thread](https://news.ycombinator.com/item?id=49395628) |
| **9** | [I accidentally logged hundreds of thousands of phone calls to military bases](https://lina.sh/blog/hijacking-e164-arpa) | ⭐ 582 | 💬 71 | [HN Thread](https://news.ycombinator.com/item?id=49387570) |
| **10** | [Zig’s io.threaded is neat](https://matklad.github.io/2026/08/06/neat-io-threaded.html) | ⭐ 95 | 💬 50 | [HN Thread](https://news.ycombinator.com/item?id=49388694) |

---

## 🗄️ News Archive

- 📅 [2026-08-22](archive/2026-08-22.md)
- 📅 [2026-08-21](archive/2026-08-21.md)
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
