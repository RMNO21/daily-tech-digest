# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [GLM-5.4: Toward Generalized Coding with Our First Loop Transformer](https://z.ai/blog/glm-5.4) | ⭐ 271 | 💬 115 | [HN Thread](https://news.ycombinator.com/item?id=50609685) |
| **2** | [Free alternative TV network built from the Internet Archive's forgotten videos](https://spelunkr.tv) | ⭐ 627 | 💬 111 | [HN Thread](https://news.ycombinator.com/item?id=50606192) |
| **3** | [XNU Linux: Full OS X GUI Userspace on Linux](https://github.com/AFK-surf/xnulinux) | ⭐ 407 | 💬 187 | [HN Thread](https://news.ycombinator.com/item?id=50607261) |
| **4** | [The next circle of security hell](https://blogs.gentoo.org/mgorny/2026/10/27/the-next-circle-of-security-hell/) | ⭐ 21 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=50610334) |
| **5** | [MRAM Basics: How Magnetic Memory Is Replacing Embedded Flash](https://www.allaboutcircuits.com/technical-articles/mram-basics-how-magnetic-memory-is-replacing-embedded-flash/) | ⭐ 14 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50587750) |
| **6** | [Yes, 17M lines of Lean is a lot](https://micjm.com/blog/yes-17m-lines-of-lean-is-a-lot/) | ⭐ 143 | 💬 165 | [HN Thread](https://news.ycombinator.com/item?id=50607668) |
| **7** | [A Beginner's Guide to Local AI with Inkling, Qwen, and Unsloth](https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth) | ⭐ 576 | 💬 239 | [HN Thread](https://news.ycombinator.com/item?id=50603845) |
| **8** | [Elixir HLS makes FPGA circuits from functions written in Elixir](https://github.com/elixir-hls/elixir-hls) | ⭐ 47 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50584526) |
| **9** | [The Birds of GTA 6: A Field Guide to Vice City and Leonida's Wildlife](https://www.audubon.org/magazine/birds-of-gta-6-field-guide-vice-city-wildlife) | ⭐ 542 | 💬 290 | [HN Thread](https://news.ycombinator.com/item?id=50602843) |
| **10** | [Perplexity and Intelligence](https://openai.com/index/perplexity-and-intelligence/) | ⭐ 618 | 💬 407 | [HN Thread](https://news.ycombinator.com/item?id=50601525) |

---

## 🗄️ News Archive

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
- 📅 [2026-11-08](archive/2026-11-08.md)
- 📅 [2026-11-07](archive/2026-11-07.md)

*... and [78 older editions in the archive folder](archive/)*

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
