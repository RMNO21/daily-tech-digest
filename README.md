# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Libghostty 1.0](https://mitchellh.com/writing/libghostty-1-0) | ⭐ 647 | 💬 100 | [HN Thread](https://news.ycombinator.com/item?id=50399933) |
| **2** | [A barbarian tribe's mythic origin story is true, ancient DNA reveals](https://www.science.org/content/article/barbarian-tribe-s-mythic-origin-story-true-ancient-dna-reveals) | ⭐ 101 | 💬 62 | [HN Thread](https://news.ycombinator.com/item?id=50401740) |
| **3** | [A Jev that can ask Opus for help gives Opus accuracy at 4x lower cost](https://hightouch.com/blog/llm-judges-identity-resolution) | ⭐ 480 | 💬 110 | [HN Thread](https://news.ycombinator.com/item?id=50397429) |
| **4** | [The Components of Agent Memory](https://www.anthropic.com/research/components-of-agent-memory) | ⭐ 44 | 💬 23 | [HN Thread](https://news.ycombinator.com/item?id=50402212) |
| **5** | [Tesla to wind down Cybertruck production](https://www.nbcnews.com/tech/tech-news/tesla-wind-cybertruck-production-years-poor-sales-markets-rcna607817) | ⭐ 1011 | 💬 1866 | [HN Thread](https://news.ycombinator.com/item?id=50391456) |
| **6** | [PostgreSQL Internals [pdf]](https://edu.postgrespro.com/postgresql_internals-14_en.pdf) | ⭐ 23 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=50361765) |
| **7** | [RealPage rent-pricing case wraps with nearly $360M to renters](https://www.multifamilydive.com/news/realpage-rent-pricing-case-360m-renters/873553/) | ⭐ 127 | 💬 62 | [HN Thread](https://news.ycombinator.com/item?id=50399991) |
| **8** | [Bong: DuckDuckGo bang alternative, open-source and self-hosted](https://bong.glendalab.com) | ⭐ 17 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=50402535) |
| **9** | [US FAA says it will phase out floppy disks from air traffic control by 2028](https://www.reuters.com/world/us/us-faa-says-it-will-phase-out-floppy-disks-air-traffic-control-by-2028-2026-11-05/) | ⭐ 339 | 💬 274 | [HN Thread](https://news.ycombinator.com/item?id=50388001) |
| **10** | [Greece has its own Pompeii: Thera buried Akrotiri in ash 17th-16th century BCE](https://www.smithsonianmag.com/history/greece-has-its-own-pompeii-and-the-ruins-tell-a-captivating-story-of-a-sophisticated-seafaring-bronze-age-society-180989747/) | ⭐ 105 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=50360810) |

---

## 🗄️ News Archive

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
- 📅 [2026-10-23](archive/2026-10-23.md)

*... and [65 older editions in the archive folder](archive/)*

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
