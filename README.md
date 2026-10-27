# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Three new discoveries in mathematics, computer science, and physics](https://openai.com/index/building-scientific-understanding-with-academic-communities/) | ⭐ 725 | 💬 316 | [HN Thread](https://news.ycombinator.com/item?id=50251344) |
| **2** | [There are now 5 inference providers for abliterated DeepSeek](https://allmodels.io/llm/abliterated) | ⭐ 39 | 💬 27 | [HN Thread](https://news.ycombinator.com/item?id=50254836) |
| **3** | [The Exponential Time Hypothesis Is False [pdf]](https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf) | ⭐ 507 | 💬 186 | [HN Thread](https://news.ycombinator.com/item?id=50251661) |
| **4** | [Sebastian Raschka's from-scratch video course on building reasoning models](https://magazine.sebastianraschka.com/p/building-reasoning-models) | ⭐ 648 | 💬 91 | [HN Thread](https://news.ycombinator.com/item?id=50245138) |
| **5** | [Oldest GUI application that still runs on Windows 11](https://blog.enlyth.com/posts/oldest-windows-gui-app-win-11/) | ⭐ 372 | 💬 216 | [HN Thread](https://news.ycombinator.com/item?id=50248055) |
| **6** | [16-bit Windows (Windows 1.x, 2.x, 3.0, 3.1, etc.) on 64-bit Windows](https://github.com/otya128/winevdm) | ⭐ 63 | 💬 5 | [HN Thread](https://news.ycombinator.com/item?id=50253529) |
| **7** | [Type Server Protocol](https://github.com/microsoft/pylance-release/blob/main/docs/tsp/type-server-protocol.md) | ⭐ 223 | 💬 146 | [HN Thread](https://news.ycombinator.com/item?id=50248371) |
| **8** | [Cross-request KV cache exposure in the GLM-5.3 Workers AI model (155 responses)](https://blog.cloudflare.com/kv-cache-exposure-remediation/) | ⭐ 114 | 💬 37 | [HN Thread](https://news.ycombinator.com/item?id=50252159) |
| **9** | [APC says let there be light, with standards to speed up photonics manufacturing](https://www.nextplatform.com/connect/2026/10/23/apc-says-let-there-be-light-with-raft-of-standards-to-speed-up-photonics-manufacturing/5304950) | ⭐ 30 | 💬 4 | [HN Thread](https://news.ycombinator.com/item?id=50234707) |
| **10** | [CSS-Tricks has a new owner](https://css-tricks.com/css-tricks-has-a-new-owner/) | ⭐ 424 | 💬 96 | [HN Thread](https://news.ycombinator.com/item?id=50245831) |

---

## 🗄️ News Archive

- 📅 [2026-10-27](archive/2026-10-27.md)
- 📅 [2026-10-26](archive/2026-10-26.md)
- 📅 [2026-10-25](archive/2026-10-25.md)
- 📅 [2026-10-24](archive/2026-10-24.md)
- 📅 [2026-10-23](archive/2026-10-23.md)
- 📅 [2026-10-22](archive/2026-10-22.md)
- 📅 [2026-10-21](archive/2026-10-21.md)
- 📅 [2026-10-20](archive/2026-10-20.md)
- 📅 [2026-10-19](archive/2026-10-19.md)
- 📅 [2026-10-18](archive/2026-10-18.md)
- 📅 [2026-10-17](archive/2026-10-17.md)
- 📅 [2026-10-16](archive/2026-10-16.md)
- 📅 [2026-10-15](archive/2026-10-15.md)
- 📅 [2026-10-14](archive/2026-10-14.md)

*... and [56 older editions in the archive folder](archive/)*

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
