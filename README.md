# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Toyota, Nissan, and Honda to standardize parts to lower costs](https://www.caranddriver.com/news/a74490092/toyota-nissan-honda-standardize-parts-lower-costs/) | ⭐ 267 | 💬 125 | [HN Thread](https://news.ycombinator.com/item?id=50596133) |
| **2** | [Pill to treat pancreatic cancer hailed as 'biggest breakthrough in decades'](https://www.theguardian.com/society/2026/nov/20/pill-pancreatic-cancer-breakthrough-daraxonrasib) | ⭐ 874 | 💬 203 | [HN Thread](https://news.ycombinator.com/item?id=50582069) |
| **3** | [Lean verification of the Riemann Hypothesis](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) | ⭐ 946 | 💬 809 | [HN Thread](https://news.ycombinator.com/item?id=50589618) |
| **4** | [Inkling-2-Mini in 5.4 GB Memory](https://github.com/ShinMegamiBoson/lookatmyquant) | ⭐ 429 | 💬 108 | [HN Thread](https://news.ycombinator.com/item?id=50591853) |
| **5** | [Sandwich Simulator](https://stulle.app/) | ⭐ 143 | 💬 55 | [HN Thread](https://news.ycombinator.com/item?id=50594911) |
| **6** | [Data Processing Incidents on Inference Providers](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/) | ⭐ 97 | 💬 34 | [HN Thread](https://news.ycombinator.com/item?id=50595554) |
| **7** | [Detonating a pile of lead azide](https://www.science.org/content/blog-post/detonating-huge-pile-lead-azide-really) | ⭐ 585 | 💬 378 | [HN Thread](https://news.ycombinator.com/item?id=50588982) |
| **8** | [Getting the mind to steer the body to steer you](https://notnottalmud.substack.com/p/getting-the-mind-to-steer-the-body) | ⭐ 231 | 💬 75 | [HN Thread](https://news.ycombinator.com/item?id=50583028) |
| **9** | [Show HN: The Riemann Proof Handbook](https://github.com/tamnd/riemann-handbook) | ⭐ 6 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50596664) |
| **10** | [PcapAnalyzer – self-hosted pcap analyzer with 27 problem detectors](https://github.com/sebaandrada-cell/PcapAnalyzer) | ⭐ 101 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=50594132) |

---

## 🗄️ News Archive

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
- 📅 [2026-11-06](archive/2026-11-06.md)

*... and [77 older editions in the archive folder](archive/)*

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
