# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [GPT-6 Sol and Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna/) | ⭐ 931 | 💬 497 | [HN Thread](https://news.ycombinator.com/item?id=49805509) |
| **2** | [Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5) | ⭐ 983 | 💬 718 | [HN Thread](https://news.ycombinator.com/item?id=49803892) |
| **3** | [Microsoft killed FoxPro in 2007. Anyway, here's FoxPro revived](https://foxscript.org/) | ⭐ 70 | 💬 42 | [HN Thread](https://news.ycombinator.com/item?id=49808023) |
| **4** | [LLM Ass Bench](https://www.assbench.com/) | ⭐ 108 | 💬 32 | [HN Thread](https://news.ycombinator.com/item?id=49807688) |
| **5** | [OpenAI GPT–6 Astra breaks Enigma message that has resisted solution since 2005](https://www.cryptocellar.org/bgac/the-mvueh-break.html) | ⭐ 510 | 💬 346 | [HN Thread](https://news.ycombinator.com/item?id=49801324) |
| **6** | ['We hacked the FBI:' Hackers say they have data on all FBI employees](https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/) | ⭐ 205 | 💬 149 | [HN Thread](https://news.ycombinator.com/item?id=49805278) |
| **7** | [The UV index is not the warm sensation of sunlight on bare skin](https://blog.asciitweezers.com/the-uv-index-is-not-the-warm-sensation-of-sunlight-on-bare-skin/) | ⭐ 30 | 💬 15 | [HN Thread](https://news.ycombinator.com/item?id=49808109) |
| **8** | [SAML: A Fractal of Bad Design](https://blog.trailofbits.com/2026/09/21/saml-a-fractal-of-bad-design/) | ⭐ 99 | 💬 49 | [HN Thread](https://news.ycombinator.com/item?id=49806335) |
| **9** | [Claude Opus 5.5 Intelligence, Performance and Price Analysis (Max)](https://artificialanalysis.ai/models/claude-opus-5-5) | ⭐ 193 | 💬 53 | [HN Thread](https://news.ycombinator.com/item?id=49804316) |
| **10** | [WordPress: Unauthenticated path traversal leading to conditional RCE](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp) | ⭐ 130 | 💬 66 | [HN Thread](https://news.ycombinator.com/item?id=49803959) |

---

## 🗄️ News Archive

- 📅 [2026-09-22](archive/2026-09-22.md)
- 📅 [2026-09-21](archive/2026-09-21.md)
- 📅 [2026-09-20](archive/2026-09-20.md)
- 📅 [2026-09-19](archive/2026-09-19.md)
- 📅 [2026-09-18](archive/2026-09-18.md)
- 📅 [2026-09-16](archive/2026-09-16.md)
- 📅 [2026-09-15](archive/2026-09-15.md)
- 📅 [2026-09-14](archive/2026-09-14.md)
- 📅 [2026-09-13](archive/2026-09-13.md)
- 📅 [2026-09-12](archive/2026-09-12.md)
- 📅 [2026-09-11](archive/2026-09-11.md)
- 📅 [2026-09-10](archive/2026-09-10.md)
- 📅 [2026-09-09](archive/2026-09-09.md)
- 📅 [2026-09-08](archive/2026-09-08.md)

*... and [25 older editions in the archive folder](archive/)*

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
