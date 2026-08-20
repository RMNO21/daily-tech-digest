# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [AliExpress runs silent WebAudio fingerprinting that breaks Bluetooth multipoint](https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html) | ⭐ 569 | 💬 193 | [HN Thread](https://news.ycombinator.com/item?id=49372583) |
| **2** | [I like 'em thick: an apology to my English teachers](https://www.experimental-history.com/p/i-like-em-thick) | ⭐ 116 | 💬 31 | [HN Thread](https://news.ycombinator.com/item?id=49347543) |
| **3** | [Show HN: I trained a 125M model to autocomplete piano on-device](https://simedw.com/2026/08/20/midi-autocomplete/) | ⭐ 297 | 💬 71 | [HN Thread](https://news.ycombinator.com/item?id=49373456) |
| **4** | [HTML Can Do That](https://chrisburnell.com/html-can-do-that/) | ⭐ 172 | 💬 35 | [HN Thread](https://news.ycombinator.com/item?id=49362689) |
| **5** | [Malicious Rust crate Arrayref runs a build-time payload](https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/) | ⭐ 235 | 💬 181 | [HN Thread](https://news.ycombinator.com/item?id=49374269) |
| **6** | [CIA funding helped keep NeXT afloat in the 80s](https://www.wsj.com/tech/steve-jobs-apple-next-cia-161b65f9?st=NWWds1&reflink=desktopwebshare_permalink) | ⭐ 112 | 💬 37 | [HN Thread](https://news.ycombinator.com/item?id=49368886) |
| **7** | [Clean up Claude 5's token vomit with a separate LLM](https://github.com/zachahn/vomit) | ⭐ 46 | 💬 31 | [HN Thread](https://news.ycombinator.com/item?id=49375996) |
| **8** | [DiffusionGemma Technical Report](https://arxiv.org/abs/2608.00146) | ⭐ 74 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=49374287) |
| **9** | [How to compromise your system with a job interview](https://www.codedge.de/posts/how-to-compromise-your-system-with-a-job-interview) | ⭐ 21 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49376332) |
| **10** | [Xorg-Server 26.0.99.901](https://lists.x.org/archives/xorg-announce/2026-August/003741.html) | ⭐ 59 | 💬 13 | [HN Thread](https://news.ycombinator.com/item?id=49373932) |

---

## 🗄️ News Archive

- 📅 [2026-08-20](archive/2026-08-20.md)
- 📅 [2026-08-19](archive/2026-08-19.md)
- 📅 [2026-08-18](archive/2026-08-18.md)
- 📅 [2026-08-17](archive/2026-08-17.md)
- 📅 [2026-08-16](archive/2026-08-16.md)
- 📅 [2026-08-15](archive/2026-08-15.md)
- 📅 [2026-08-14](archive/2026-08-14.md)

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
python scraper.py
```

---

<div align="center">
  <sub>Maintained by <a href="https://github.com/RMNO21">RMNO21</a> • Powered by GitHub Actions & Hacker News API</sub>
</div>
