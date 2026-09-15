# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) | ⭐ 361 | 💬 141 | [HN Thread](https://news.ycombinator.com/item?id=49717558) |
| **2** | [Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations](https://github.com/arnegiacomo/fugleramme) | ⭐ 1113 | 💬 153 | [HN Thread](https://news.ycombinator.com/item?id=49711544) |
| **3** | [An Update on Wayback Machine Access](https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/) | ⭐ 254 | 💬 126 | [HN Thread](https://news.ycombinator.com/item?id=49716176) |
| **4** | [Gemini 3.8 Live and 3.8 Live Extended Thinking](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/) | ⭐ 182 | 💬 117 | [HN Thread](https://news.ycombinator.com/item?id=49715947) |
| **5** | [Jean-Pierre Serre is 100 years old today](https://mathshistory.st-andrews.ac.uk/Biographies/Serre/) | ⭐ 20 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49718822) |
| **6** | [We got admin access to Baseten's production GitHub in 25 minutes](https://www.strix.ai/blog/baseten-harbor-github-pat-takeover) | ⭐ 152 | 💬 61 | [HN Thread](https://news.ycombinator.com/item?id=49716476) |
| **7** | [German Rheinmetall open-sources its Battlesuite connected weapon system protcol](https://rheinmetall.github.io/onboardapi-documentation/9.10.0/index.html) | ⭐ 15 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=49718928) |
| **8** | [WangNet – 1.8 MB, zero-dependency Numberwang adjudication in 11 languages](https://github.com/GraafHenk/numberwang) | ⭐ 53 | 💬 19 | [HN Thread](https://news.ycombinator.com/item?id=49717605) |
| **9** | [Chopping up books when they're physically too big](https://attainablefelicity.mattkirkland.com/20260915/cut-up-your-books.html) | ⭐ 63 | 💬 53 | [HN Thread](https://news.ycombinator.com/item?id=49716953) |
| **10** | [Building a Linux GPU Driver for the M4 Mac Mini in One Month](https://codyho.dev/blog/gpu-driver/) | ⭐ 35 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49717638) |

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
