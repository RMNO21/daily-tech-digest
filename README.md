# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Dutch governments builds alternative for Microsoft based on NixOS](https://www.dawo.community/en/) | ⭐ 554 | 💬 289 | [HN Thread](https://news.ycombinator.com/item?id=49841563) |
| **2** | [Platform-Independent SIMD in Go](https://go.dev/blog/simd-experiment) | ⭐ 73 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=49843269) |
| **3** | [Git-bug: Distributed, offline-first bug tracker embedded in Git](https://github.com/git-bug/git-bug) | ⭐ 70 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=49843174) |
| **4** | [Ink and Switch Interactive Homepage](https://www.inkandswitch.com/) | ⭐ 85 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=49842270) |
| **5** | [Pentium II at 600Mhz with Voodoo 3 Emulated on 86Box with M6 Mac Mini](https://nyaa.sh/reviews/mac-mini-m6-emulation) | ⭐ 137 | 💬 53 | [HN Thread](https://news.ycombinator.com/item?id=49841285) |
| **6** | [Nobody Asked for a Crab Chair](https://newmobility.com/nobody-asked-for-a-crab-chair/) | ⭐ 15 | 💬 13 | [HN Thread](https://news.ycombinator.com/item?id=49843899) |
| **7** | [Topcoat is pushing the boundary of server applications with Rust](https://tokio.rs/blog/2026-09-24-topcoat-server-applications) | ⭐ 48 | 💬 33 | [HN Thread](https://news.ycombinator.com/item?id=49842332) |
| **8** | [F-Droid 2.0](https://f-droid.org/2026/09/24/f-droid-2.0-a-new-chapter-for-android-freedom.html) | ⭐ 1325 | 💬 380 | [HN Thread](https://news.ycombinator.com/item?id=49831968) |
| **9** | [I'm Tired of Being on the Network](https://matduggan.com/im-tired-of-being-on-the-network/) | ⭐ 67 | 💬 55 | [HN Thread](https://news.ycombinator.com/item?id=49843547) |
| **10** | [CVE-2025-13032: Entering and Breaking the Avast Antivirus Sandbox Part 2](https://www.safateam.com/intelligence-hub/research/technical-articles/cve-2025-13032-entering-and-breaking-the-avast-antivirus-sandbox-part-2) | ⭐ 77 | 💬 18 | [HN Thread](https://news.ycombinator.com/item?id=49841115) |

---

## 🗄️ News Archive

- 📅 [2026-09-25](archive/2026-09-25.md)
- 📅 [2026-09-24](archive/2026-09-24.md)
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

*... and [27 older editions in the archive folder](archive/)*

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
