# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [The "$60 Gaming PC" – AMD BC-250 (2025)](https://devquasar.com/hardware/the-60-gaming-pc-amd-bc-250/) | ⭐ 161 | 💬 53 | [HN Thread](https://news.ycombinator.com/item?id=49576386) |
| **2** | [Discovery of a new OpenAI agent message board](https://collusion.wiki/) | ⭐ 1963 | 💬 1463 | [HN Thread](https://news.ycombinator.com/item?id=49563355) |
| **3** | [Actively exploited sandbox RCE in all Chromium versions](https://nvd.nist.gov/vuln/detail/cve-2026-85046) | ⭐ 690 | 💬 392 | [HN Thread](https://news.ycombinator.com/item?id=49570669) |
| **4** | [Nitter has more working instances than before the takedowns](https://codeberg.org/mv12star/shitter/wiki/Instances) | ⭐ 495 | 💬 202 | [HN Thread](https://news.ycombinator.com/item?id=49571634) |
| **5** | [Wikimedia Foundation Workers Overwhelmingly Vote to Form Union with CWA](https://wikiworkersunited.org/announcements/2026-09-04-us-wikimedia-foundation-workers-overwhelmingly-vote-to-form-union-with-cwa/) | ⭐ 124 | 💬 26 | [HN Thread](https://news.ycombinator.com/item?id=49577975) |
| **6** | [Terpstra Keyboard](http://terpstrakeyboard.com/) | ⭐ 74 | 💬 34 | [HN Thread](https://news.ycombinator.com/item?id=49575150) |
| **7** | [Formalizing Fermat's Last Theorem](https://www.anthropic.com/research/formalizing-fermats-last-theorem) | ⭐ 708 | 💬 448 | [HN Thread](https://news.ycombinator.com/item?id=49568506) |
| **8** | [Singapore subway (mrt) information display types](https://www.sgtrains.com/technology-infosys.html) | ⭐ 24 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=49535940) |
| **9** | [A Million Falcons Went Missing. Here’s How They Were Found](https://www.nationalgeographic.com/animals/article/falcons-migration-angola-falcopolis) | ⭐ 43 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=49540253) |
| **10** | [A bizarre Commodore 64 peripheral, a mime, and some pretty bad ads](https://buttondown.com/suchbadtechads/archive/spartan-and-the-mime/) | ⭐ 37 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49575859) |

---

## 🗄️ News Archive

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
- 📅 [2026-08-24](archive/2026-08-24.md)
- 📅 [2026-08-23](archive/2026-08-23.md)

*... and [9 older editions in the archive folder](archive/)*

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
