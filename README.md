# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [OpenAI CLI](https://github.com/openai/openai-cli) | ⭐ 54 | 💬 29 | [HN Thread](https://news.ycombinator.com/item?id=50191507) |
| **2** | [The recently proposed o(n log n) integer multiplication algorithm [pdf]](https://web.maths.unsw.edu.au/~davidharvey/research/subnlogn.pdf) | ⭐ 170 | 💬 95 | [HN Thread](https://news.ycombinator.com/item?id=50190455) |
| **3** | [WorldTUI: I trained a 360M model to pretend to be a terminal](https://simedw.com/2026/10/21/world-model-terminal/) | ⭐ 104 | 💬 42 | [HN Thread](https://news.ycombinator.com/item?id=50190363) |
| **4** | [There isn't an easy exploit for this PHP vulnerability](https://eliastaylor.com/noexploit/) | ⭐ 467 | 💬 248 | [HN Thread](https://news.ycombinator.com/item?id=50188948) |
| **5** | [GitLab critical patch release](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/) | ⭐ 326 | 💬 75 | [HN Thread](https://news.ycombinator.com/item?id=50185869) |
| **6** | [Compromised LiteLLM 1.107.0 on PyPI Installs a Credential Stealer and Backdoor](https://safedep.io/litellm-pypi-compromise-credential-stealer-backdoor/) | ⭐ 488 | 💬 167 | [HN Thread](https://news.ycombinator.com/item?id=50181114) |
| **7** | [Using LLM for confidence scoring is a bad idea](https://rumple.github.io/blog/2026/10/20/asking-llm-for-confidence.html) | ⭐ 64 | 💬 39 | [HN Thread](https://news.ycombinator.com/item?id=50176082) |
| **8** | [Security Disclosure](https://blog.railway.com/p/security-disclosure-wednesday-october-21st) | ⭐ 424 | 💬 249 | [HN Thread](https://news.ycombinator.com/item?id=50188228) |
| **9** | [Rust Style Guide](https://google.github.io/styleguide/rustguide.html) | ⭐ 281 | 💬 166 | [HN Thread](https://news.ycombinator.com/item?id=50186010) |
| **10** | [No more icons in every menu by default](https://blog.jim-nielsen.com/2026/icons-in-every-menu/) | ⭐ 278 | 💬 171 | [HN Thread](https://news.ycombinator.com/item?id=50161346) |

---

## 🗄️ News Archive

- 📅 [2026-10-22](archive/2026-10-22.md)
- 📅 [2026-10-21](archive/2026-10-21.md)
- 📅 [2026-10-20](archive/2026-10-20.md)
- 📅 [2026-10-19](archive/2026-10-19.md)
- 📅 [2026-10-18](archive/2026-10-18.md)
- 📅 [2026-10-17](archive/2026-10-17.md)
- 📅 [2026-10-16](archive/2026-10-16.md)
- 📅 [2026-10-15](archive/2026-10-15.md)
- 📅 [2026-10-14](archive/2026-10-14.md)
- 📅 [2026-10-13](archive/2026-10-13.md)
- 📅 [2026-10-10](archive/2026-10-10.md)
- 📅 [2026-10-09](archive/2026-10-09.md)
- 📅 [2026-10-08](archive/2026-10-08.md)
- 📅 [2026-10-07](archive/2026-10-07.md)

*... and [51 older editions in the archive folder](archive/)*

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
