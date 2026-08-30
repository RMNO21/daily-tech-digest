# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Hacking IKEA Furniture](https://greenlightning.eu/diy/hacking-ikea-furniture/) | ⭐ 41 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49497810) |
| **2** | [Arbitrary code execution in QubesOS via copy-to-VM error reporting backchannel](https://www.qubes-os.org/news/2026/08/29/qsb-118/) | ⭐ 100 | 💬 41 | [HN Thread](https://news.ycombinator.com/item?id=49496918) |
| **3** | [Longest Straight Line Paths on Water or Land on the Earth (2018)](https://arxiv.org/abs/1804.07389) | ⭐ 128 | 💬 32 | [HN Thread](https://news.ycombinator.com/item?id=49496782) |
| **4** | [Casey Muratori – The Root of the Root of All Evil – BSC 2026 [video]](https://www.youtube.com/watch?v=hpj6r6CjJf8) | ⭐ 79 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=49463888) |
| **5** | [Claude Session URL appended to commit messages and PR descriptions by default](https://github.com/anthropics/claude-code/issues/66504) | ⭐ 56 | 💬 49 | [HN Thread](https://news.ycombinator.com/item?id=49498201) |
| **6** | [An implementation of Conway's Game of Life for Windows 3.1x and later](https://www.muppetlabs.com/~breadbox/software/windows.html) | ⭐ 14 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49497819) |
| **7** | [Brits would quite like their private messages to stay private](https://www.theregister.com/security/2026/08/30/turns-out-brits-would-quite-like-their-private-messages-to-stay-private/5292994) | ⭐ 196 | 💬 119 | [HN Thread](https://news.ycombinator.com/item?id=49497063) |
| **8** | [What my dad taught me about AI coding in the 90s](https://askmike.org/articles/ai-coding-lessons-in-the-90s-from-my-dad/) | ⭐ 10 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49419381) |
| **9** | [One Nix flake to rule them all](https://fzakaria.com/2026/08/28/one-flake-to-rule-them-all) | ⭐ 24 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49497712) |
| **10** | [monty-go: Pure-Go wrapper for Pydantic's Monty Python Interpreter](https://github.com/fugue-labs/monty-go) | ⭐ 14 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49497928) |

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
