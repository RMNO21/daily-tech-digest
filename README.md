# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU](https://github.com/synchopate/llama-modchip) | ⭐ 111 | 💬 36 | [HN Thread](https://news.ycombinator.com/item?id=50411961) |
| **2** | [Quadrillion-parameter transformers and how to train them](https://qlabs.sh/research/parameters) | ⭐ 31 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=50352518) |
| **3** | [Porting Android 16 to my blind mother's keypad phone](https://z1x.us/blog/four-hundred-bucks-of-e-waste) | ⭐ 55 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=50366821) |
| **4** | [Goodbye Claude, Hello Pi](https://caleb.software/posts/claude-to-pi.html) | ⭐ 485 | 💬 317 | [HN Thread](https://news.ycombinator.com/item?id=50410107) |
| **5** | [JIT bitmap text rendering for microcontrollers](https://linebender.org/blog/jit-bitmap-text/) | ⭐ 50 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=50412072) |
| **6** | [Person of Interest](https://krthr.co/person-of-interest/) | ⭐ 194 | 💬 122 | [HN Thread](https://news.ycombinator.com/item?id=50412318) |
| **7** | [Writing as a Thinking Tool](http://muratbuffalo.blogspot.com/2026/11/writing-as-thinking-tool.html) | ⭐ 31 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=50412067) |
| **8** | [What I run on my $10 USD OpenStick homelab](https://blog.bosscher.ch/posts/openstick/) | ⭐ 669 | 💬 122 | [HN Thread](https://news.ycombinator.com/item?id=50406670) |
| **9** | [Clj.rs – a Clojure dialect implemented in Rust](https://clj.rs/) | ⭐ 103 | 💬 40 | [HN Thread](https://news.ycombinator.com/item?id=50366902) |
| **10** | [Claude Code's "Don't Ask Again" exposes passwords in 1,122 public GitHub files](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again) | ⭐ 476 | 💬 341 | [HN Thread](https://news.ycombinator.com/item?id=50407882) |

---

## 🗄️ News Archive

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
- 📅 [2026-10-24](archive/2026-10-24.md)

*... and [66 older editions in the archive folder](archive/)*

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
