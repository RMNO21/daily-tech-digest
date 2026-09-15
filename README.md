# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations](https://github.com/arnegiacomo/fugleramme) | ⭐ 79 | 💬 22 | [HN Thread](https://news.ycombinator.com/item?id=49711544) |
| **2** | [Java 27 Released](https://mail.openjdk.org/archives/list/announce@openjdk.org/thread/ORGGLMN75HFEWP7YL3ZLGHLYHVIBJDYT/) | ⭐ 34 | 💬 8 | [HN Thread](https://news.ycombinator.com/item?id=49712041) |
| **3** | [I can't stop thinking about Papua New Guinea](https://notnottalmud.substack.com/p/why-i-cant-stop-thinking-about-papua) | ⭐ 502 | 💬 204 | [HN Thread](https://news.ycombinator.com/item?id=49708431) |
| **4** | [25 Years of Mass Surveillance Is Enough](https://www.schneier.com/blog/archives/2026/09/25-years-of-mass-surveillance-is-enough.html) | ⭐ 139 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=49710883) |
| **5** | [Alternatives to MinIO for single-node local S3](https://rmoff.net/2026/01/14/alternatives-to-minio-for-single-node-local-s3/) | ⭐ 103 | 💬 54 | [HN Thread](https://news.ycombinator.com/item?id=49709381) |
| **6** | [CSS-Tricks in Limbo](https://vale.rocks/micros/20260915-0135) | ⭐ 118 | 💬 37 | [HN Thread](https://news.ycombinator.com/item?id=49708993) |
| **7** | [A rough guide for going back to the Moon](https://research.ibm.com/blog/nasa-ibm-lunar-foundation-model) | ⭐ 27 | 💬 13 | [HN Thread](https://news.ycombinator.com/item?id=49697549) |
| **8** | [iOS 27, iPadOS 27, and macOS 27](https://www.apple.com/newsroom/2026/09/major-updates-for-apples-software-platforms-are-now-available/) | ⭐ 661 | 💬 763 | [HN Thread](https://news.ycombinator.com/item?id=49701004) |
| **9** | [The k-server conjecture is true](https://arxiv.org/abs/2609.15979) | ⭐ 56 | 💬 19 | [HN Thread](https://news.ycombinator.com/item?id=49709129) |
| **10** | [OpenArm: An open-source 7DOF humanoid arm](https://github.com/enactic/OpenArm) | ⭐ 145 | 💬 29 | [HN Thread](https://news.ycombinator.com/item?id=49684289) |

---

## 🗄️ News Archive

- 📅 [2026-09-15](archive/2026-09-15.md)
- 📅 [2026-09-14](archive/2026-09-14.md)
- 📅 [2026-09-13](archive/2026-09-13.md)
- 📅 [2026-09-12](archive/2026-09-12.md)
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

*... and [19 older editions in the archive folder](archive/)*

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
