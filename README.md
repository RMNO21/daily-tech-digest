# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Kagi Search for Everyone](https://kagi.com/changelog) | ⭐ 176 | 💬 90 | [HN Thread](https://news.ycombinator.com/item?id=50383740) |
| **2** | [MS Paint Remote Code Execution Vulnerability](https://www.cve.org/CVERecord?id=CVE-2026-83844) | ⭐ 87 | 💬 24 | [HN Thread](https://news.ycombinator.com/item?id=50384233) |
| **3** | [sshole](https://sshhole.com) | ⭐ 2119 | 💬 530 | [HN Thread](https://news.ycombinator.com/item?id=50378228) |
| **4** | [Alpine Linux Security Advisory: OpenSSH-server password authentication bypass](https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/) | ⭐ 509 | 💬 102 | [HN Thread](https://news.ycombinator.com/item?id=50379704) |
| **5** | [The Hackintosh Reborn](https://www.naut.ca/blog/2026/11/05/the-hackintosh-reborn-with-ai/) | ⭐ 117 | 💬 38 | [HN Thread](https://news.ycombinator.com/item?id=50383057) |
| **6** | [Tencent Launches Hy4, One of the Leading Open-Source AI Models](https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/) | ⭐ 40 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=50383963) |
| **7** | [Window Sweaters](https://github.com/saragordic/window-sweaters) | ⭐ 173 | 💬 67 | [HN Thread](https://news.ycombinator.com/item?id=50381383) |
| **8** | [Goodbye from Salon](https://www.salon.com/2026/11/05/goodbye-from-salon/) | ⭐ 238 | 💬 77 | [HN Thread](https://news.ycombinator.com/item?id=50383739) |
| **9** | [The Cost of Blogging](https://onlinegoddess.net/2026/11/the-cost-of-blogging/) | ⭐ 24 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=50383877) |
| **10** | [Motorola Signature 27 with GrapheneOS support](https://motorolanews.com/motorola-signature-27-2/) | ⭐ 332 | 💬 226 | [HN Thread](https://news.ycombinator.com/item?id=50380810) |

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
