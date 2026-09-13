# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Astra and Fable still hack on simple variants of alignment evals from 2025](https://www.lesswrong.com/posts/munJKF7iWMsWJLAH2/astra-and-fable-still-hack-on-simple-variants-of-alignment) | ⭐ 105 | 💬 29 | [HN Thread](https://news.ycombinator.com/item?id=49684393) |
| **2** | [JetKVM Mini](https://jetkvm.com/blog/introducing-jetkvm-mini) | ⭐ 359 | 💬 138 | [HN Thread](https://news.ycombinator.com/item?id=49681152) |
| **3** | [Libraries Run Rust Inside Python (With PyO3)](https://belderbos.dev/blog/how-libraries-run-rust-inside-python/) | ⭐ 13 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=49685037) |
| **4** | ['Fingerprints' inside the Sun could reveal if it once swallowed a planet](https://ras.ac.uk/news-and-press/research-highlights/fingerprints-inside-sun-could-reveal-if-it-once-swallowed-planet) | ⭐ 70 | 💬 19 | [HN Thread](https://news.ycombinator.com/item?id=49683033) |
| **5** | [Why is the x86 undefined instruction called ud2? Why 2?](https://devblogs.microsoft.com/oldnewthing/20260910-00/?p=112689) | ⭐ 43 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=49683262) |
| **6** | [CUDA for AMD on Windows](https://github.com/Speedstu/CUDA-for-AMD-Windows) | ⭐ 25 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49684356) |
| **7** | [Reverse engineering my e-scooter and rewriting the firmware in Rust](https://bensimms.moe/reverse-engineering-scooter/) | ⭐ 131 | 💬 41 | [HN Thread](https://news.ycombinator.com/item?id=49638071) |
| **8** | [Why are AI agents lying, cheating and coordinating?](https://yoshuabengio.org/en/publication/why-are-ai-agents-lying-cheating-and-coordinating) | ⭐ 455 | 💬 528 | [HN Thread](https://news.ycombinator.com/item?id=49678969) |
| **9** | [TailTalk: A modern async user space AppleTalk stack with Rust and Tokio](https://github.com/FeralFirmware/TailTalk/) | ⭐ 44 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49678423) |
| **10** | [Cpak – OCI application package format for Linux desktops, servers and devices](https://cpak.it/) | ⭐ 5 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49684778) |

---

## 🗄️ News Archive

- 📅 [2026-09-13](archive/2026-09-13.md)
- 📅 [2026-09-12](archive/2026-09-12.md)
- 📅 [2026-09-11](archive/2026-09-11.md)
- 📅 [2026-09-10](archive/2026-09-10.md)
- 📅 [2026-09-09](archive/2026-09-09.md)
- 📅 [2026-09-08](archive/2026-09-08.md)
- 📅 [2026-09-07](archive/2026-09-07.md)
- 📅 [2026-09-06](archive/2026-09-06.md)
- 📅 [2026-09-05](archive/2026-09-05.md)
- 📅 [2026-09-04](archive/2026-09-04.md)
- 📅 [2026-09-03](archive/2026-09-03.md)
- 📅 [2026-09-02](archive/2026-09-02.md)
- 📅 [2026-09-01](archive/2026-09-01.md)
- 📅 [2026-08-31](archive/2026-08-31.md)

*... and [17 older editions in the archive folder](archive/)*

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
