# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Why is this fingerprinting script creating bioweapons?](https://nullpt.rs/fingerprinting-bioweapons) | ⭐ 473 | 💬 104 | [HN Thread](https://news.ycombinator.com/item?id=50276998) |
| **2** | [Formlabs Studio 1 $699 Resin Printer](https://formlabs.com/products/form-studio-1-basic-founders-edition/) | ⭐ 22 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=50281044) |
| **3** | [Gemini 4 Carbon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) | ⭐ 659 | 💬 536 | [HN Thread](https://news.ycombinator.com/item?id=50276792) |
| **4** | [CNC Stone Carving](https://carmelitegothic.com/cnc-stone-carving/) | ⭐ 340 | 💬 107 | [HN Thread](https://news.ycombinator.com/item?id=50274409) |
| **5** | [Dayjob: Tax – evaluating AI agents on 50 professional tax assignments](https://surgehq.ai/blog/dayjob-tax) | ⭐ 159 | 💬 87 | [HN Thread](https://news.ycombinator.com/item?id=50275626) |
| **6** | [MacBook Pro with PROLED XDR Display and Touch](https://www.apple.com/macbook-pro/proled-xdr-display/) | ⭐ 420 | 💬 715 | [HN Thread](https://news.ycombinator.com/item?id=50276940) |
| **7** | [Nango (YC W23) Is Hiring Across Eng, FDE, Marketing, DevRel](https://nango.dev/careers) | ⭐ 1 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50280824) |
| **8** | [Leak Exposes 41,000 Homeland Security Workers–Including Undercover ICE Agents](https://www.wired.com/story/massive-leak-exposes-41000-homeland-security-workers-including-undercover-ice-agents/) | ⭐ 68 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=50280864) |
| **9** | [The case of the 9 bit AES key](https://v12.sh/blog/the-case-of-the-9bit-aes-key) | ⭐ 13 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=50280722) |
| **10** | [The Grid, a factory-scale robot in Massachusetts that builds PCBs on demand](https://www.circuithub.com/post/unveiling-the-grid) | ⭐ 363 | 💬 180 | [HN Thread](https://news.ycombinator.com/item?id=50243060) |

---

## 🗄️ News Archive

- 📅 [2026-10-28](archive/2026-10-28.md)
- 📅 [2026-10-27](archive/2026-10-27.md)
- 📅 [2026-10-26](archive/2026-10-26.md)
- 📅 [2026-10-25](archive/2026-10-25.md)
- 📅 [2026-10-24](archive/2026-10-24.md)
- 📅 [2026-10-23](archive/2026-10-23.md)
- 📅 [2026-10-22](archive/2026-10-22.md)
- 📅 [2026-10-21](archive/2026-10-21.md)
- 📅 [2026-10-20](archive/2026-10-20.md)
- 📅 [2026-10-19](archive/2026-10-19.md)
- 📅 [2026-10-18](archive/2026-10-18.md)
- 📅 [2026-10-17](archive/2026-10-17.md)
- 📅 [2026-10-16](archive/2026-10-16.md)
- 📅 [2026-10-15](archive/2026-10-15.md)

*... and [57 older editions in the archive folder](archive/)*

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
