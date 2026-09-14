# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [EuroBirdPortal – Live bird movements across Europe](https://www.eurobirdportal.org/ebp/en/) | ⭐ 155 | 💬 52 | [HN Thread](https://news.ycombinator.com/item?id=49693610) |
| **2** | [A 386 PC for Your RP2350](https://github.com/rh1tech/frank-386) | ⭐ 122 | 💬 29 | [HN Thread](https://news.ycombinator.com/item?id=49693613) |
| **3** | [An atlas of periodic solutions to the three-body problem](https://www.threebodyorbits.com/) | ⭐ 138 | 💬 32 | [HN Thread](https://news.ycombinator.com/item?id=49670852) |
| **4** | [Apple's Siri AI Can Be Swapped Out for Claude, ChatGPT, Code Shows](https://www.macrumors.com/2026/09/14/siri-can-be-swapped-out-for-chatgpt-claude/) | ⭐ 103 | 💬 39 | [HN Thread](https://news.ycombinator.com/item?id=49695409) |
| **5** | [Show HN: Kinesis – Control your Mac with the Meta Neural Band](https://github.com/callbacked/kinesis) | ⭐ 69 | 💬 22 | [HN Thread](https://news.ycombinator.com/item?id=49695408) |
| **6** | [Devil's Arrows: Ancient builders hauled 55k-lb stones 11 miles for UK stone row](https://www.sciencedaily.com/releases/2026/09/260909005152.htm) | ⭐ 11 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=49659557) |
| **7** | [Texas judge rules TikTok misled users on child safety feature](https://www.reuters.com/legal/litigation/texas-judge-rules-tiktok-misled-users-child-safety-feature-2026-09-11/) | ⭐ 54 | 💬 9 | [HN Thread](https://news.ycombinator.com/item?id=49695829) |
| **8** | [Drawably: Hand-Drawn UI Controls](https://github.com/Danilaa1/drawably) | ⭐ 29 | 💬 16 | [HN Thread](https://news.ycombinator.com/item?id=49630353) |
| **9** | [OpenArch – PyTorch implementations of modern LLM architectures](https://github.com/anuj0456/OpenArch) | ⭐ 92 | 💬 18 | [HN Thread](https://news.ycombinator.com/item?id=49693384) |
| **10** | [Registration without a phone number on Signal will use zero-knowledge proofs](https://community.signalusers.org/t/registration-without-a-phone-number/2222?page=10) | ⭐ 337 | 💬 169 | [HN Thread](https://news.ycombinator.com/item?id=49689048) |

---

## 🗄️ News Archive

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
- 📅 [2026-09-01](archive/2026-09-01.md)

*... and [18 older editions in the archive folder](archive/)*

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
