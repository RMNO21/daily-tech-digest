# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Railway Security Disclosure](https://blog.railway.com/p/security-disclosure-wednesday-october-21st) | ⭐ 51 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=50188228) |
| **2** | [Today's PHP security release, and how we're strengthening security](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/) | ⭐ 573 | 💬 289 | [HN Thread](https://news.ycombinator.com/item?id=50182987) |
| **3** | [GitLab Critical Patch Release](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/) | ⭐ 166 | 💬 38 | [HN Thread](https://news.ycombinator.com/item?id=50185869) |
| **4** | [AWS rates PHP RCE as Important so Amazon Linux 2023 patch may take 20 days](https://github.com/amazonlinux/amazon-linux-2023/issues/1148) | ⭐ 71 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=50187708) |
| **5** | [No More Icons in Every Menu by Default](https://blog.jim-nielsen.com/2026/icons-in-every-menu/) | ⭐ 57 | 💬 36 | [HN Thread](https://news.ycombinator.com/item?id=50161346) |
| **6** | [Compromised LiteLLM 1.107.0 on PyPI Installs a Credential Stealer and Backdoor](https://safedep.io/litellm-pypi-compromise-credential-stealer-backdoor/) | ⭐ 370 | 💬 121 | [HN Thread](https://news.ycombinator.com/item?id=50181114) |
| **7** | [Why Windows 11 still ships with Windows 95's memory manager hidden inside it](https://www.windowslatest.com/2026/10/19/why-windows-11-still-ships-with-windows-95s-memory-manager-hidden-inside-it/) | ⭐ 99 | 💬 66 | [HN Thread](https://news.ycombinator.com/item?id=50159726) |
| **8** | [Eight Bits of Trust: eMudhra's CA keys cracked in milliseconds](https://scotthelme.co.uk/eight-bits-of-trust-emudhras-ca-keys-cracked-in-milliseconds/) | ⭐ 785 | 💬 385 | [HN Thread](https://news.ycombinator.com/item?id=50177916) |
| **9** | [Claude Duet](https://claude.com/product/claude-duet) | ⭐ 236 | 💬 204 | [HN Thread](https://news.ycombinator.com/item?id=50186037) |
| **10** | [Meta ordered to pay $25B penalty in New Mexico Cambridge Analytica case](https://www.cnbc.com/2026/10/21/meta-new-mexico-cambridge-analytica-penalty.html) | ⭐ 247 | 💬 147 | [HN Thread](https://news.ycombinator.com/item?id=50184820) |

---

## 🗄️ News Archive

- 📅 [2026-10-21](archive/2026-10-21.md)
- 📅 [2026-10-20](archive/2026-10-20.md)
- 📅 [2026-10-19](archive/2026-10-19.md)
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

*... and [50 older editions in the archive folder](archive/)*

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
