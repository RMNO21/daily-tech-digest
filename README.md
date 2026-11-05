# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Sshole](https://sshhole.com) | ⭐ 903 | 💬 248 | [HN Thread](https://news.ycombinator.com/item?id=50378228) |
| **2** | [Alpine Linux Security advisory: OpenSSH-server password authentication bypass](https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/) | ⭐ 55 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=50379704) |
| **3** | [MCP Explained](https://mcp-explained.com/) | ⭐ 78 | 💬 29 | [HN Thread](https://news.ycombinator.com/item?id=50379249) |
| **4** | [Image of Our Satellite-Choked Night Skies](https://kottke.org/26/11/stunning-image-of-our-satellite-choked-night-skies) | ⭐ 33 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=50379773) |
| **5** | [OpenSSH 10.6p2 Critical workaround for alpine without PAM](https://www.openssh.org/releasenotes.html#10.6p2) | ⭐ 110 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=50377976) |
| **6** | [September in Servo: <progress>, rounded rectangles, and more](https://servo.org/blog/2026/11/05/september-in-servo/) | ⭐ 17 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=50379576) |
| **7** | [Download your favourite YouTube videos](https://criminallyvulgar.dev/you-should-absolutely-download-your-favourite-youtube-videos/) | ⭐ 42 | 💬 22 | [HN Thread](https://news.ycombinator.com/item?id=50378571) |
| **8** | [Baidu released ERNIE 5.5 Flash Base](https://ernie.baidu.com/release/ernie-5-5-flash-base/) | ⭐ 123 | 💬 71 | [HN Thread](https://news.ycombinator.com/item?id=50377078) |
| **9** | [Obscure audio codec is a perfect fit for the N64](https://phoboslab.org/log/2026/11/n64-ulc-codec) | ⭐ 34 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50378508) |
| **10** | [Vivaldi 8.3 for Desktop: make bad ads sad](https://vivaldi.com/blog/vivaldi-on-desktop-8-3/) | ⭐ 28 | 💬 27 | [HN Thread](https://news.ycombinator.com/item?id=50378398) |

---

## 🗄️ News Archive

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
- 📅 [2026-10-22](archive/2026-10-22.md)
- 📅 [2026-10-21](archive/2026-10-21.md)

*... and [63 older editions in the archive folder](archive/)*

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
