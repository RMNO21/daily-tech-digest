# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Formalizing Fermat's Last Theorem](https://www.anthropic.com/research/formalizing-fermats-last-theorem) | ⭐ 295 | 💬 178 | [HN Thread](https://news.ycombinator.com/item?id=49568506) |
| **2** | [Discovery of a new OpenAI agent message board](https://collusion.wiki/) | ⭐ 1326 | 💬 1076 | [HN Thread](https://news.ycombinator.com/item?id=49563355) |
| **3** | [Shutting down our public encrypted DNS](https://mullvad.net/en/blog/shutting-down-our-public-encrypted-dns-servers-and-sponsoring-quad9-instead) | ⭐ 154 | 💬 53 | [HN Thread](https://news.ycombinator.com/item?id=49568579) |
| **4** | [Statichost.eu – 100% European static site hosting](https://www.statichost.eu/) | ⭐ 33 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49569896) |
| **5** | [Can AI design circuit boards yet?](https://eebench.org/blog/can-ai-design-circuit-boards-yet/) | ⭐ 64 | 💬 49 | [HN Thread](https://news.ycombinator.com/item?id=49569366) |
| **6** | [Show HN: Open-Source eInk Bike Computer](https://opentrailpaper.com) | ⭐ 175 | 💬 57 | [HN Thread](https://news.ycombinator.com/item?id=49567437) |
| **7** | [Government Rails Site Hit Hours After CVE Patch](https://rietta.com/blog/ruby-on-rails-cve-exploited-hours-after-patch/) | ⭐ 43 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=49568828) |
| **8** | [An open DNS recursive service for free security and high privacy](https://quad9.net/) | ⭐ 17 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49569663) |
| **9** | [The Rust React Compiler is now native in Vite](https://blog.master.dev/react-now-rusted-all-the-way-out/) | ⭐ 75 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=49567873) |
| **10** | [IBM Bob](https://bob.ibm.com/) | ⭐ 193 | 💬 231 | [HN Thread](https://news.ycombinator.com/item?id=49563851) |

---

## 🗄️ News Archive

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
- 📅 [2026-08-25](archive/2026-08-25.md)
- 📅 [2026-08-24](archive/2026-08-24.md)
- 📅 [2026-08-23](archive/2026-08-23.md)
- 📅 [2026-08-22](archive/2026-08-22.md)

*... and [8 older editions in the archive folder](archive/)*

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
