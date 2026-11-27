# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [GPT 6.2 Astra Solves a Historical Mystery](https://generativehistory.substack.com/p/gpt-62-astra-solves-a-historical) | ⭐ 122 | 💬 110 | [HN Thread](https://news.ycombinator.com/item?id=50643158) |
| **2** | [Credit card skimming scripts using WebRTC found on popular shopping sites](https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer) | ⭐ 330 | 💬 176 | [HN Thread](https://news.ycombinator.com/item?id=50668145) |
| **3** | [Convex skills send the user's app idea to a remote server without telling them](https://github.com/convex/convex-backend-skill/issues/64) | ⭐ 161 | 💬 51 | [HN Thread](https://news.ycombinator.com/item?id=50669765) |
| **4** | [Citroën Hydraulic System](https://www.citroenet.org.uk/miscellaneous/hydraulics/hydraulics-1.html) | ⭐ 70 | 💬 28 | [HN Thread](https://news.ycombinator.com/item?id=50662313) |
| **5** | [Michael Nielsen took down his book on neural nets](https://twitter.com/michael_nielsen/status/2126359767362748777) | ⭐ 226 | 💬 136 | [HN Thread](https://news.ycombinator.com/item?id=50670757) |
| **6** | [The AT&T Unix PC (3B1) VM](https://virtuallyfun.com/2026/11/22/the-ultimate-att-unix-pc-3b1-vm-w-tcp-ip-and-apps/) | ⭐ 30 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=50670841) |
| **7** | [Show HN: bouncemarket – a live prediction market game for a bouncing ball](https://bouncemarket.minhanhday.com/) | ⭐ 299 | 💬 92 | [HN Thread](https://news.ycombinator.com/item?id=50667726) |
| **8** | [False computer-checked proofs](https://cr.yp.to/proofs/falseccp.html) | ⭐ 143 | 💬 66 | [HN Thread](https://news.ycombinator.com/item?id=50667989) |
| **9** | [First images of the impact of DART asteroid deflection experiment](https://arstechnica.com/space/2026/11/europes-hera-mission-returns-to-the-chaotic-scene-of-a-cosmic-smashup/) | ⭐ 165 | 💬 52 | [HN Thread](https://news.ycombinator.com/item?id=50657392) |
| **10** | [Show HN: DragDropMath – Learn math by feel](https://dragdropmath.com/) | ⭐ 60 | 💬 15 | [HN Thread](https://news.ycombinator.com/item?id=50669673) |

---

## 🗄️ News Archive

- 📅 [2026-11-27](archive/2026-11-27.md)
- 📅 [2026-11-26](archive/2026-11-26.md)
- 📅 [2026-11-23](archive/2026-11-23.md)
- 📅 [2026-11-22](archive/2026-11-22.md)
- 📅 [2026-11-21](archive/2026-11-21.md)
- 📅 [2026-11-19](archive/2026-11-19.md)
- 📅 [2026-11-18](archive/2026-11-18.md)
- 📅 [2026-11-17](archive/2026-11-17.md)
- 📅 [2026-11-16](archive/2026-11-16.md)
- 📅 [2026-11-15](archive/2026-11-15.md)
- 📅 [2026-11-14](archive/2026-11-14.md)
- 📅 [2026-11-11](archive/2026-11-11.md)
- 📅 [2026-11-10](archive/2026-11-10.md)
- 📅 [2026-11-09](archive/2026-11-09.md)

*... and [80 older editions in the archive folder](archive/)*

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
