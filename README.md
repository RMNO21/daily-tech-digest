# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Creepy Crawlies](https://people.kernel.org/monsieuricon/creepy-crawlies) | ⭐ 793 | 💬 366 | [HN Thread](https://news.ycombinator.com/item?id=49491791) |
| **2** | [Cores in space: The core memory module from a 1980 Spacelab computer](https://www.righto.com/2026/08/spacelab-core-memory.html) | ⭐ 44 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=49502214) |
| **3** | [Haiku R1/beta6 has been released](https://www.haiku-os.org/news/2026-08-26_haiku_r1_beta6) | ⭐ 215 | 💬 60 | [HN Thread](https://news.ycombinator.com/item?id=49499867) |
| **4** | [NFC Energy-Harvesting PCB Business Card with an MCU](https://wilsonharper.net/projects/businesscard/) | ⭐ 58 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49478426) |
| **5** | [Continuous Diffusion Language Models (CDLM's)](https://sander.ai/2026/08/24/continuous-dlms.html) | ⭐ 30 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49502611) |
| **6** | [Sort branches by last commit date](https://ryangreenberg.com/til/git-branches-by-commit-date/) | ⭐ 53 | 💬 13 | [HN Thread](https://news.ycombinator.com/item?id=49435285) |
| **7** | [Why open source rocks – a new SM750 (Silicon Motion GPU) HDMI Driver](https://github.com/KodeMunkie/sm750hdmifb) | ⭐ 51 | 💬 26 | [HN Thread](https://news.ycombinator.com/item?id=49501611) |
| **8** | [Coordination Headwind: How Organizations Are Like Slime Molds](https://komoroske.com/slime-mold/) | ⭐ 110 | 💬 38 | [HN Thread](https://news.ycombinator.com/item?id=49499891) |
| **9** | [Hacking IKEA Furniture](https://greenlightning.eu/diy/hacking-ikea-furniture/) | ⭐ 240 | 💬 147 | [HN Thread](https://news.ycombinator.com/item?id=49497810) |
| **10** | [Zig: Pointer Stability for ArrayLists](https://ziglang.org/devlog/2026/#2026-08-27) | ⭐ 74 | 💬 33 | [HN Thread](https://news.ycombinator.com/item?id=49499095) |

---

## 🗄️ News Archive

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
- 📅 [2026-08-17](archive/2026-08-17.md)

*... and [3 older editions in the archive folder](archive/)*

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
