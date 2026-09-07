# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Keep Our Servers Running](https://blog.archive.org/2026/09/01/keep-our-servers-running-your-recurring-donation-goes-3x-this-september/) | ⭐ 479 | 💬 100 | [HN Thread](https://news.ycombinator.com/item?id=49593563) |
| **2** | [Live map of public transport in Belgium](https://openbaarvervoerbelgie.be/) | ⭐ 25 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=49595865) |
| **3** | [Caltech Mathathon – first hackathon ever devoted to research level mathematics](https://mathathonchallenge.com/index.html) | ⭐ 7 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49596055) |
| **4** | [Programming is Art](https://orchidfiles.com/programming-is-art/) | ⭐ 58 | 💬 54 | [HN Thread](https://news.ycombinator.com/item?id=49595360) |
| **5** | [LG smart TVs caught logging audio with screen off and snooping on local devices](https://www.notebookcheck.net/LG-smart-TVs-caught-logging-audio-with-screen-off-and-snooping-on-local-devices.1391214.0.html) | ⭐ 136 | 💬 64 | [HN Thread](https://news.ycombinator.com/item?id=49594878) |
| **6** | [Making a Python interpreter in 1024 bytes](https://austinhenley.com/blog/python1024.html) | ⭐ 236 | 💬 84 | [HN Thread](https://news.ycombinator.com/item?id=49591876) |
| **7** | [Speculative Decoding in vLLM on AMD GPUs](https://vllm.ai/blog/2026-08-23-speculative-decoding-amd-gpus) | ⭐ 6 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49596054) |
| **8** | ['You Can See Everything' Review: Nathan Fielder's Doc About Elizabeth Holmes](https://variety.com/2026/film/reviews/nathan-fielder-surprise-film-telluride-elizabeth-holmes-1236853513/) | ⭐ 24 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49596119) |
| **9** | [Ask HN: How do you manage skills files?](https://news.ycombinator.com/item?id=49589914) | ⭐ 141 | 💬 118 | [HN Thread](https://news.ycombinator.com/item?id=49589914) |
| **10** | [It took a year to ship WebAssembly in Anubis](https://anubis.techaro.lol/blog/2026/anubis-wasm/) | ⭐ 277 | 💬 136 | [HN Thread](https://news.ycombinator.com/item?id=49590611) |

---

## 🗄️ News Archive

- 📅 [2026-09-07](archive/2026-09-07.md)
- 📅 [2026-09-06](archive/2026-09-06.md)
- 📅 [2026-09-05](archive/2026-09-05.md)
- 📅 [2026-09-04](archive/2026-09-04.md)
- 📅 [2026-09-03](archive/2026-09-03.md)
- 📅 [2026-09-02](archive/2026-09-02.md)
- 📅 [2026-09-01](archive/2026-09-01.md)
- 📅 [2026-08-31](archive/2026-08-31.md)
- 📅 [2026-08-30](archive/2026-08-30.md)
- 📅 [2026-08-29](archive/2026-08-29.md)
- 📅 [2026-08-28](archive/2026-08-28.md)
- 📅 [2026-08-27](archive/2026-08-27.md)
- 📅 [2026-08-26](archive/2026-08-26.md)
- 📅 [2026-08-25](archive/2026-08-25.md)

*... and [11 older editions in the archive folder](archive/)*

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
