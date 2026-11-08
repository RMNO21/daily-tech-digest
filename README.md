# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Goodbye Claude, Hello Pi](https://caleb.software/posts/claude-to-pi.html) | ⭐ 165 | 💬 93 | [HN Thread](https://news.ycombinator.com/item?id=50410107) |
| **2** | [What I run on my $10 USD OpenStick homelab](https://blog.bosscher.ch/posts/openstick/) | ⭐ 516 | 💬 99 | [HN Thread](https://news.ycombinator.com/item?id=50406670) |
| **3** | [Claude Code's "Don't Ask Again" exposes passwords in 1,122 public GitHub files](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again) | ⭐ 332 | 💬 226 | [HN Thread](https://news.ycombinator.com/item?id=50407882) |
| **4** | [Making any integer with four 2s (2025)](https://eli.thegreenplace.net/2025/making-any-integer-with-four-2s/) | ⭐ 111 | 💬 28 | [HN Thread](https://news.ycombinator.com/item?id=50408713) |
| **5** | [ZapFast: A fast, native WhatsApp client in Rust and egui](https://github.com/crmne/zapfast) | ⭐ 53 | 💬 34 | [HN Thread](https://news.ycombinator.com/item?id=50409855) |
| **6** | [Kirlian Photography: Building Your Own Equipment](https://imagesco.com/articles/kirlian/kirlian-photography.html) | ⭐ 22 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=50410359) |
| **7** | [Need for Speed Underground 2 online in the browser](https://nfsu2.xyz/) | ⭐ 922 | 💬 242 | [HN Thread](https://news.ycombinator.com/item?id=50403052) |
| **8** | [MaxxBench – "Nice DeepSWE score. But is it true?"](https://maxxbench.unlap.ai/research/why-maxxbench/) | ⭐ 276 | 💬 76 | [HN Thread](https://news.ycombinator.com/item?id=50406222) |
| **9** | [Consumer brain wave headsets threaten privacy](https://www.science.org/content/article/wearable-device-makers-are-harvesting-brain-data-train-ai-without-telling-users?referrer=https%3A%2F%2Fwww.google.com%2F) | ⭐ 25 | 💬 7 | [HN Thread](https://news.ycombinator.com/item?id=50409856) |
| **10** | [Every Mac comes with an (undocumented) family member classifier](https://8rank.ai/game/apple-intelligence-personal-knowledge-graph) | ⭐ 689 | 💬 372 | [HN Thread](https://news.ycombinator.com/item?id=50403097) |

---

## 🗄️ News Archive

- 📅 [2026-11-08](archive/2026-11-08.md)
- 📅 [2026-11-07](archive/2026-11-07.md)
- 📅 [2026-11-06](archive/2026-11-06.md)
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

*... and [66 older editions in the archive folder](archive/)*

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
