# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [KetchUp – Open-source SketchUp alternative built with Rust and WebGPU](https://ketchup3d.github.io/app/) | ⭐ 427 | 💬 117 | [HN Thread](https://news.ycombinator.com/item?id=50418176) |
| **2** | [Unlocking any car from X brand in most of the world](https://shubs.io/unlocking-any-car-from-x-brand-in-most-of-the-world/) | ⭐ 278 | 💬 93 | [HN Thread](https://news.ycombinator.com/item?id=50419215) |
| **3** | [Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation](https://arxiv.org/abs/2610.14162) | ⭐ 8 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50422168) |
| **4** | [I'm not convinced the AI bubble exists](https://matteoraso.github.io/im-not-convinced-the-ai-bubble-exists.html#im-not-convinced-the-ai-bubble-exists) | ⭐ 217 | 💬 304 | [HN Thread](https://news.ycombinator.com/item?id=50418975) |
| **5** | [Chimera Vocal Synth](https://chimera-vocal-synth.vercel.app/) | ⭐ 183 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=50418182) |
| **6** | [Declarative Dragging](https://declarative-dragging.github.io/) | ⭐ 497 | 💬 63 | [HN Thread](https://news.ycombinator.com/item?id=50368481) |
| **7** | [A Critique of GPUI](https://blog.zortax.de/posts/a-critique-of-gpui) | ⭐ 78 | 💬 43 | [HN Thread](https://news.ycombinator.com/item?id=50420857) |
| **8** | [Outlook.com is rejecting email from domains without DMARC](https://mailroute.net/blog/outlook-rejecting-email-without-dmarc) | ⭐ 372 | 💬 264 | [HN Thread](https://news.ycombinator.com/item?id=50416158) |
| **9** | [Dux: Free, open-source Wayland desktop shell with file manager and theming](https://duxlabs.dev/) | ⭐ 265 | 💬 86 | [HN Thread](https://news.ycombinator.com/item?id=50416053) |
| **10** | [Ask HN: What are you working on? (November 2026)](https://news.ycombinator.com/item?id=50417407) | ⭐ 198 | 💬 665 | [HN Thread](https://news.ycombinator.com/item?id=50417407) |

---

## 🗄️ News Archive

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
- 📅 [2026-10-26](archive/2026-10-26.md)
- 📅 [2026-10-25](archive/2026-10-25.md)

*... and [67 older editions in the archive folder](archive/)*

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
