# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Haiku R1/beta6 has been released](https://www.haiku-os.org/news/2026-08-26_haiku_r1_beta6) | ⭐ 148 | 💬 38 | [HN Thread](https://news.ycombinator.com/item?id=49499867) |
| **2** | [Creepy Crawlies](https://people.kernel.org/monsieuricon/creepy-crawlies) | ⭐ 470 | 💬 219 | [HN Thread](https://news.ycombinator.com/item?id=49491791) |
| **3** | [Coordination Headwind: How Organizations Are Like Slime Molds](https://komoroske.com/slime-mold/) | ⭐ 57 | 💬 26 | [HN Thread](https://news.ycombinator.com/item?id=49499891) |
| **4** | [Running SQLite Apps on Docker and Kubernetes with Litestream](https://openrun.dev/blog/litestream/) | ⭐ 10 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49501147) |
| **5** | [METR and Redwood Offer Holy %^ Postmortem of the HuggingFace Hack](https://thezvi.wordpress.com/2026/08/29/metr-and-redwood-offer-holy-postmortem-of-the-huggingface-hack/) | ⭐ 88 | 💬 35 | [HN Thread](https://news.ycombinator.com/item?id=49498787) |
| **6** | [Hacking IKEA Furniture](https://greenlightning.eu/diy/hacking-ikea-furniture/) | ⭐ 201 | 💬 114 | [HN Thread](https://news.ycombinator.com/item?id=49497810) |
| **7** | [Electric rain can eat through metal](https://www.scientificamerican.com/article/electric-rain-can-eat-through-metal/) | ⭐ 52 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=49463397) |
| **8** | [Zig: Pointer Stability for ArrayLists](https://ziglang.org/devlog/2026/#2026-08-27) | ⭐ 42 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49499095) |
| **9** | [European Commission Revives Push for Encryption Backdoors in ProtectEU Strategy](https://reclaimthenet.org/eu-protecteu-strategy-encryption-backdoor-law-enforcement) | ⭐ 209 | 💬 77 | [HN Thread](https://news.ycombinator.com/item?id=49499394) |
| **10** | [Artie (YC S23) Is Hiring Technical AES](https://www.artie.com/careers?ashby_jid=e87b84d2-78b3-41a3-937a-47e83643cdf1) | ⭐ 1 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49500471) |

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
