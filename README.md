# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Global Glacier Extinction Explorer](https://glacierextinction.com) | ⭐ 21 | 💬 3 | [HN Thread](https://news.ycombinator.com/item?id=49660576) |
| **2** | [Godot and Rust based multiplexer (terminal panes and more)](https://github.com/godot-pty/gpty) | ⭐ 11 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=49660676) |
| **3** | [Logo Programming Language](https://el.media.mit.edu/logo-foundation/what_is_logo/logo_programming.html) | ⭐ 100 | 💬 51 | [HN Thread](https://news.ycombinator.com/item?id=49622406) |
| **4** | [I've operated petabyte-scale ClickHouse clusters for 5 years](https://www.tinybird.co/blog/what-i-learned-operating-clickhouse) | ⭐ 48 | 💬 15 | [HN Thread](https://news.ycombinator.com/item?id=49601138) |
| **5** | [Copying login keychains between Macs fails on Secure Enclave Macs with Tahoe](https://derflounder.wordpress.com/2026/09/08/manually-copying-login-keychain-files-from-one-mac-to-another-no-longer-works-on-secure-enclave-equipped-macs-running-macos-tahoe/) | ⭐ 22 | 💬 6 | [HN Thread](https://news.ycombinator.com/item?id=49651046) |
| **6** | [So you want to use OpenRouter?](https://mmoustafa.com/blog/so-you-want-to-use-openrouter/) | ⭐ 484 | 💬 125 | [HN Thread](https://news.ycombinator.com/item?id=49621546) |
| **7** | [Matt Mullenweg tells Automattic staff in Slack he's back in control after ouster](https://techcrunch.com/2026/09/11/matt-mullenweg-tells-automattic-staff-in-slack-hes-back-in-control-after-ceo-ouster/) | ⭐ 62 | 💬 30 | [HN Thread](https://news.ycombinator.com/item?id=49660104) |
| **8** | [HuggingFace: Security.txt](https://huggingface.co/security.txt) | ⭐ 112 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=49659245) |
| **9** | [The AI Takeover Checklist: A Devil's Advocate Audit](https://nochan.net/b/Internet-Crap/20260910-Asked-Claude-For-A-Checklist/) | ⭐ 3 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=49660923) |
| **10** | [RTK reports token savings, but our cost benchmarks disagree](https://quesma.com/blog/does-rtk-make-ai-coding-cheaper/) | ⭐ 97 | 💬 54 | [HN Thread](https://news.ycombinator.com/item?id=49656471) |

---

## 🗄️ News Archive

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
- 📅 [2026-08-31](archive/2026-08-31.md)
- 📅 [2026-08-30](archive/2026-08-30.md)
- 📅 [2026-08-29](archive/2026-08-29.md)

*... and [15 older editions in the archive folder](archive/)*

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
