# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Hybrid Reasoning Agents: LLM agents that think in latent space, act through text](https://arxiv.org/abs/2610.18861) | ⭐ 130 | 💬 72 | [HN Thread](https://news.ycombinator.com/item?id=50145337) |
| **2** | [Someone behind the software](https://karrisaarinen.com/posts/someone-behind-the-software/) | ⭐ 266 | 💬 112 | [HN Thread](https://news.ycombinator.com/item?id=50142573) |
| **3** | [Free Pascal compiler now supports dynamic packages](https://www.getlazarus.org/dynamic/) | ⭐ 94 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=50144066) |
| **4** | [There's never been a better time to go into math (by: 3blue1brown) [video]](https://www.youtube.com/watch?v=LKrwhjOI8Nc) | ⭐ 95 | 💬 32 | [HN Thread](https://news.ycombinator.com/item?id=50136150) |
| **5** | [RepRapMicron](https://github.com/VikOlliver/RepRapMicron/wiki) | ⭐ 316 | 💬 50 | [HN Thread](https://news.ycombinator.com/item?id=50141076) |
| **6** | [Dogs seem to agree with humans that 'bouba' is round and 'kiki' is spiky](https://www.sciencealert.com/dogs-seem-to-agree-with-humans-that-bouba-is-round-and-kiki-is-spiky) | ⭐ 85 | 💬 62 | [HN Thread](https://news.ycombinator.com/item?id=50136979) |
| **7** | [PalmOS Lemmings](https://github.com/ardiri/palmos-lemmings) | ⭐ 77 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=50143536) |
| **8** | [Show HN: WhatsApp MCP running free on Cloudflare](https://github.com/finereli/whatsapp-mcp) | ⭐ 14 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=50145715) |
| **9** | [One parser, two bugs, many routers: Exploiting Broadcom WiFi across eCos, Linux](https://quentinkaiser.be/security/2026/10/16/one-parser-two-bugs/) | ⭐ 33 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=50122058) |
| **10** | [DeepSeek search and fetch – $0.75 per 1000 successful requests](https://api-docs.deepseek.com/guides/search/) | ⭐ 521 | 💬 251 | [HN Thread](https://news.ycombinator.com/item?id=50138531) |

---

## 🗄️ News Archive

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
- 📅 [2026-10-05](archive/2026-10-05.md)
- 📅 [2026-10-04](archive/2026-10-04.md)
- 📅 [2026-10-03](archive/2026-10-03.md)
- 📅 [2026-10-02](archive/2026-10-02.md)

*... and [47 older editions in the archive folder](archive/)*

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
