# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [VGHF Digital Archive passes 5000 magazines. Here's what's next](https://gamehistory.org/5k-magazines/) | ⭐ 48 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49952029) |
| **2** | [Tell HN: Bob Cringely has died](https://news.ycombinator.com/item?id=49949438) | ⭐ 561 | 💬 110 | [HN Thread](https://news.ycombinator.com/item?id=49949438) |
| **3** | [Why don't more developers “use the platform”?](https://nolanlawson.com/2026/10/03/why-dont-more-developers-use-the-platform/) | ⭐ 181 | 💬 157 | [HN Thread](https://news.ycombinator.com/item?id=49950554) |
| **4** | [Run Qwen 3.8 Flash Next (125B) on consumer hardware (RTX 4090) at 100T/s](https://github.com/Niko1221/Strata) | ⭐ 4 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49953495) |
| **5** | [Glashütte Trash Clock – A 30-minute pendulum clock made from trash](https://niklasroy.com/gtc/) | ⭐ 5 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49930439) |
| **6** | [The work by Valve's Timur Kristóf on improving old AMD GPUs on Linux](https://www.phoronix.com/news/XDC-2026-Valve-Timur-AMDGPU) | ⭐ 336 | 💬 57 | [HN Thread](https://news.ycombinator.com/item?id=49946895) |
| **7** | [gpuvis: GPU Trace Visualizer](https://github.com/mikesart/gpuvis) | ⭐ 33 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49935097) |
| **8** | [Rejection Sensitivity in Gifted and Twice-Exceptional Children](https://teachyourkids.substack.com/p/rejection-sensitivity-in-gifted-and) | ⭐ 24 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49953116) |
| **9** | [Show HN: AI search for every photo and every frame of video on macOS](https://github.com/allenv0/SCM) | ⭐ 16 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=49952111) |
| **10** | [Treachery in the Rodin Museum 3D scan verdict](https://cosmowenman.substack.com/p/rodin-museum-3d-scan-verdict) | ⭐ 235 | 💬 108 | [HN Thread](https://news.ycombinator.com/item?id=49946355) |

---

## 🗄️ News Archive

- 📅 [2026-10-04](archive/2026-10-04.md)
- 📅 [2026-10-03](archive/2026-10-03.md)
- 📅 [2026-10-02](archive/2026-10-02.md)
- 📅 [2026-10-01](archive/2026-10-01.md)
- 📅 [2026-09-30](archive/2026-09-30.md)
- 📅 [2026-09-29](archive/2026-09-29.md)
- 📅 [2026-09-28](archive/2026-09-28.md)
- 📅 [2026-09-27](archive/2026-09-27.md)
- 📅 [2026-09-26](archive/2026-09-26.md)
- 📅 [2026-09-25](archive/2026-09-25.md)
- 📅 [2026-09-24](archive/2026-09-24.md)
- 📅 [2026-09-22](archive/2026-09-22.md)
- 📅 [2026-09-21](archive/2026-09-21.md)
- 📅 [2026-09-20](archive/2026-09-20.md)

*... and [36 older editions in the archive folder](archive/)*

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
