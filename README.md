# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [New paper shows that 37% of workers in US saw real wages decline from 2021-2024 [pdf]](https://bfi.uchicago.edu/wp-content/uploads/2026/08/BFI_WP_2026-108-1.pdf) | ⭐ 323 | 💬 166 | [HN Thread](https://news.ycombinator.com/item?id=49355142) |
| **2** | [Meta's blockbuster trial draws parallels to big tobacco](https://www.economist.com/business/2026/08/18/metas-blockbuster-trial-draws-parallels-to-big-tobacco) | ⭐ 91 | 💬 65 | [HN Thread](https://news.ycombinator.com/item?id=49355825) |
| **3** | [OpenLogi](https://openlogi.org/en) | ⭐ 126 | 💬 30 | [HN Thread](https://news.ycombinator.com/item?id=49355606) |
| **4** | [Palomar: A registry of Lean verified mathematics](https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics/) | ⭐ 29 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49355968) |
| **5** | [A 3D fruit fly on macOS desktop powered by the real FlyWire connectome](https://github.com/DenisSergeevitch/desktop-fly) | ⭐ 204 | 💬 58 | [HN Thread](https://news.ycombinator.com/item?id=49353221) |
| **6** | [Cerebras CS-4](https://www.cerebras.ai/cs4) | ⭐ 144 | 💬 99 | [HN Thread](https://news.ycombinator.com/item?id=49354949) |
| **7** | [The Amazon tax](https://seths.blog/2026/08/the-amazon-tax/) | ⭐ 1040 | 💬 602 | [HN Thread](https://news.ycombinator.com/item?id=49345263) |
| **8** | [Scientists stunned by children's lung recovery in ultra low emission zone](https://www.bbc.com/news/articles/c1l1r1zne1ro) | ⭐ 79 | 💬 47 | [HN Thread](https://news.ycombinator.com/item?id=49355105) |
| **9** | [Solo – a .so loader for static Linux binaries](https://github.com/pg83/solo) | ⭐ 78 | 💬 77 | [HN Thread](https://news.ycombinator.com/item?id=49354613) |
| **10** | [How does IKEA come up with names for its products?](https://www.ikea.com/se/en/customer-service/knowledge/articles/6f564c4d-2ccc-46de-b643-545a3948dc79.html) | ⭐ 268 | 💬 155 | [HN Thread](https://news.ycombinator.com/item?id=49349984) |

---

## 🗄️ News Archive

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
