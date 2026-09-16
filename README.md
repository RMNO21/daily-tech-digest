# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Training a 4B model to produce 81% faster query plans than Postgres](https://rohanbansal.com/qorl) | ⭐ 308 | 💬 58 | [HN Thread](https://news.ycombinator.com/item?id=49731285) |
| **2** | [Breaking the 1.58-bit Barrier for Ternary LLMs](https://arxiv.org/abs/2609.16338) | ⭐ 82 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49732931) |
| **3** | [Xiaomi Mimo 2.6 live post-training dashboard](https://mimo.xiaomi.com/rl/) | ⭐ 168 | 💬 45 | [HN Thread](https://news.ycombinator.com/item?id=49732270) |
| **4** | [Nvidia announces native GPU programming in Rust](https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/) | ⭐ 61 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=49724881) |
| **5** | [Small programming tricks](https://will-keleher.com/posts/small-programming-tricks-matter/) | ⭐ 336 | 💬 166 | [HN Thread](https://news.ycombinator.com/item?id=49729000) |
| **6** | [Reversing Factorio's RNG](https://gegell.github.io/posts/factorio-rng/) | ⭐ 91 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49674451) |
| **7** | [Performance Improvements in .NET 11](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-11/) | ⭐ 105 | 💬 11 | [HN Thread](https://news.ycombinator.com/item?id=49711424) |
| **8** | [AWS says it can't restore some data from mideast facilities struck by Iran](https://www.wsj.com/world/middle-east/aws-says-it-cant-restore-some-data-from-mideast-facilities-struck-by-iran-ddcb7e5d) | ⭐ 142 | 💬 107 | [HN Thread](https://news.ycombinator.com/item?id=49719249) |
| **9** | [Backups Aren't Simple](https://filipovski.net/2026/09/16/backups-arent-simple.html) | ⭐ 11 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49732513) |
| **10** | [The engineering behind the US Strategic Petroleum Reserve](https://johnjwang.com/post/2026/09/15/engineering-behind-us-strategic-petroleum-reserve) | ⭐ 16 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49719596) |

---

## 🗄️ News Archive

- 📅 [2026-09-16](archive/2026-09-16.md)
- 📅 [2026-09-15](archive/2026-09-15.md)
- 📅 [2026-09-14](archive/2026-09-14.md)
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

*... and [20 older editions in the archive folder](archive/)*

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
