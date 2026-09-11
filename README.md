# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [A misalignment of AI in mathematics](https://mathandai.org/) | ⭐ 151 | 💬 236 | [HN Thread](https://news.ycombinator.com/item?id=49662371) |
| **2** | [Λ Snap – An inviting programming language for kids and adults for CS study](https://snap.berkeley.edu/) | ⭐ 51 | 💬 27 | [HN Thread](https://news.ycombinator.com/item?id=49662214) |
| **3** | [Claude is only available to people over 18 years](https://support.claude.com/en/articles/15171100-age-assurance-on-claude) | ⭐ 445 | 💬 498 | [HN Thread](https://news.ycombinator.com/item?id=49656225) |
| **4** | [The EPA Is Planning to Scrap Public Review Rules for Data Center Pollution](https://capitalbnews.org/data-centers-permit-rules-epa/) | ⭐ 131 | 💬 83 | [HN Thread](https://news.ycombinator.com/item?id=49662672) |
| **5** | [I've operated petabyte-scale ClickHouse clusters for 5 years](https://www.tinybird.co/blog/what-i-learned-operating-clickhouse) | ⭐ 123 | 💬 45 | [HN Thread](https://news.ycombinator.com/item?id=49601138) |
| **6** | [Show HN: Hacker News, Without AI](https://www.unslop.news/) | ⭐ 119 | 💬 53 | [HN Thread](https://news.ycombinator.com/item?id=49660783) |
| **7** | [118M Queries per Second on Neki](https://planetscale.com/blog/118-million-queries-per-second-on-neki) | ⭐ 64 | 💬 31 | [HN Thread](https://news.ycombinator.com/item?id=49660555) |
| **8** | [Rune is now open source](https://rune.build/blog/rune-is-now-open-source) | ⭐ 70 | 💬 19 | [HN Thread](https://news.ycombinator.com/item?id=49660149) |
| **9** | [GrapheneOS' rewritten Messages app is released](https://github.com/GrapheneOS/Messaging/releases/tag/13) | ⭐ 15 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49663373) |
| **10** | [Show HN: Godot and Rust based multiplexer (terminal panes and more)](https://github.com/godot-pty/gpty) | ⭐ 61 | 💬 34 | [HN Thread](https://news.ycombinator.com/item?id=49660676) |

---

## 🗄️ News Archive

- 📅 [2026-09-11](archive/2026-09-11.md)
- 📅 [2026-09-10](archive/2026-09-10.md)
- 📅 [2026-09-09](archive/2026-09-09.md)
- 📅 [2026-09-08](archive/2026-09-08.md)
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

*... and [15 older editions in the archive folder](archive/)*

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
