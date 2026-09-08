# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [DaVinci Resolve 21.1](https://www.blackmagicdesign.com/media/release/20260908-03) | ⭐ 69 | 💬 18 | [HN Thread](https://news.ycombinator.com/item?id=49610181) |
| **2** | [Show HN: Copperhead – Hardware as Fast as Software](https://copperhead.sh/) | ⭐ 53 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=49610059) |
| **3** | [LibreOffice breaks download records after declaring it has no AI features](https://manualdousuario.net/en/libreoffice-download-record-no-ai/) | ⭐ 90 | 💬 18 | [HN Thread](https://news.ycombinator.com/item?id=49610538) |
| **4** | [Among European Companies That Use a CDN, Nearly 9 in 10 Use Cloudflare](https://ciphercue.com/blog/european-cdn-concentration-cloudflare-nine-in-ten) | ⭐ 305 | 💬 250 | [HN Thread](https://news.ycombinator.com/item?id=49607443) |
| **5** | [Antiquated HTML Snippets and Artefacts](https://vale.rocks/posts/html-relics) | ⭐ 139 | 💬 47 | [HN Thread](https://news.ycombinator.com/item?id=49607991) |
| **6** | [Extracting Steering Vectors from J space](https://darshanmakwana412.github.io/2026/09/extracting-steering-vectors-from-j-space/) | ⭐ 16 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=49586667) |
| **7** | [I've factored the RSA keys of a Certificate Authority from the 90s](https://mcpherrin.ca/2026/09/07/rsa.html) | ⭐ 423 | 💬 88 | [HN Thread](https://news.ycombinator.com/item?id=49604637) |
| **8** | [There's a new "Google Jail" for independent wikis](https://weirdgloop.org/blog/google-jail) | ⭐ 344 | 💬 124 | [HN Thread](https://news.ycombinator.com/item?id=49604870) |
| **9** | [Why getting your hands dirty is good for you](https://www.bbc.com/future/article/20260904-how-getting-your-hands-dirty-boosts-your-health-within-weeks) | ⭐ 128 | 💬 100 | [HN Thread](https://news.ycombinator.com/item?id=49608023) |
| **10** | [Picolibrary: A Small Press](https://novalis.org/blog/2026-08-31-picolibrary-a-very-small-press.html) | ⭐ 25 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49574941) |

---

## 🗄️ News Archive

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
- 📅 [2026-08-28](archive/2026-08-28.md)
- 📅 [2026-08-27](archive/2026-08-27.md)
- 📅 [2026-08-26](archive/2026-08-26.md)

*... and [12 older editions in the archive folder](archive/)*

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
