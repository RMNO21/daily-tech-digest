# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Google SWE points 48 AI agents at NASA Lidar, finds unmapped Maya pyramid in 72h](https://pietromiotti.com/latest/maya-site/?maya) | ⭐ 462 | 💬 174 | [HN Thread](https://news.ycombinator.com/item?id=50452455) |
| **2** | [Can a Linear Program Do Weight-Space Programming?](https://nathan.rs/posts/weight-space-lp/) | ⭐ 101 | 💬 15 | [HN Thread](https://news.ycombinator.com/item?id=50452655) |
| **3** | [Pharo in the Browser with WebAssembly](https://massimo-nocentini.github.io/pharo-vm/world.html) | ⭐ 29 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=50453763) |
| **4** | [Atuin Threads: All your agent sessions on every machine](https://blog.atuin.sh/threads-agent-sessions/) | ⭐ 21 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=50453637) |
| **5** | [Using voltage glitching to unleash the A100 in my mining card](https://blog.kate.land/posts/using-voltage-glitching-to-unlock-the-a100/) | ⭐ 109 | 💬 44 | [HN Thread](https://news.ycombinator.com/item?id=50451903) |
| **6** | [I asked every TV manufacturer 17 questions about how they spy on you](https://www.theverge.com/tech/1012372/tv-privacy-acr-questions) | ⭐ 78 | 💬 31 | [HN Thread](https://news.ycombinator.com/item?id=50453474) |
| **7** | [Protecting SSH Keys with macOS Secure Enclave](https://gatezh.com/posts/macos-secure-enclave-ssh-keys/) | ⭐ 310 | 💬 111 | [HN Thread](https://news.ycombinator.com/item?id=50449748) |
| **8** | [Next-Level Benchmarking Overfitting – Thomas Neumann](http://databasearchitects.blogspot.com/2026/11/next-level-benchmarking-overfitting.html) | ⭐ 36 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=50452496) |
| **9** | [Show HN: Godbolt-in-a-floating-window for Neovim (C, C++, Rust)](https://github.com/0xdeadf1sh/AssemblyForNeovim) | ⭐ 16 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=50453229) |
| **10** | [Apple is killing its Support Community forum next week](https://www.theverge.com/tech/1031507/apple-community-support-forum-shutting-down) | ⭐ 46 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=50453555) |

---

## 🗄️ News Archive

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
- 📅 [2026-10-28](archive/2026-10-28.md)
- 📅 [2026-10-27](archive/2026-10-27.md)

*... and [69 older editions in the archive folder](archive/)*

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
