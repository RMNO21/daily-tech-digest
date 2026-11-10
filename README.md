# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Toyota brand Scion is back and it's going to sell a kei truck in America](https://www.theautopian.com/scion-is-back-and-its-going-to-sell-a-freaking-kei-truck-in-america/) | ⭐ 226 | 💬 146 | [HN Thread](https://news.ycombinator.com/item?id=50445401) |
| **2** | [After 7 Months, Glasswing Overwelms Maintainers with Underwhelming Findings](https://www.vulncheck.com/blog/anthropic-glasswing-november-update) | ⭐ 61 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=50447074) |
| **3** | [.name Grandfathered](https://neil.fraser.name/news/2026/11/10/) | ⭐ 623 | 💬 139 | [HN Thread](https://news.ycombinator.com/item?id=50442736) |
| **4** | [Smart home devices should work without the internet](https://docodethatmatters.com/home-automation-overnight-success/) | ⭐ 630 | 💬 225 | [HN Thread](https://news.ycombinator.com/item?id=50441707) |
| **5** | [Six Math Essentials by Terence Tao](https://teorth.github.io/tao-web/six-math-essentials.html) | ⭐ 83 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=50446246) |
| **6** | [Synaptics patent claims stop work on DisplayLink drivers](https://lwn.net/SubscriberLink/1102549/acbc92e00cee3a3f/) | ⭐ 255 | 💬 114 | [HN Thread](https://news.ycombinator.com/item?id=50443824) |
| **7** | [Val Town is winding down](https://blog.val.town/winding-down) | ⭐ 270 | 💬 69 | [HN Thread](https://news.ycombinator.com/item?id=50443427) |
| **8** | [Show HN: Get your coding agent off ~2019 JavaScript, onto modern web primitives](https://github.com/GoogleChrome/modern-web-guidance) | ⭐ 220 | 💬 60 | [HN Thread](https://news.ycombinator.com/item?id=50443812) |
| **9** | [AlphaProof Code](https://deepmind.google/blog/introducing-alphaproof-code/) | ⭐ 552 | 💬 173 | [HN Thread](https://news.ycombinator.com/item?id=50439193) |
| **10** | [rVPN – stealth VPN with end-to-end encryption](https://rvpn.org/) | ⭐ 35 | 💬 33 | [HN Thread](https://news.ycombinator.com/item?id=50446714) |

---

## 🗄️ News Archive

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
- 📅 [2026-10-28](archive/2026-10-28.md)
- 📅 [2026-10-27](archive/2026-10-27.md)
- 📅 [2026-10-26](archive/2026-10-26.md)

*... and [68 older editions in the archive folder](archive/)*

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
