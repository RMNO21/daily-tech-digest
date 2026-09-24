# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Linux support is coming to Snapdragon X2 Series](https://www.qualcomm.com/news/onq/2026/09/snapdragon-summit-agentic-ai-pcs-linux) | ⭐ 251 | 💬 122 | [HN Thread](https://news.ycombinator.com/item?id=49823582) |
| **2** | [Claude discovers a novel enzyme system with CRISPR-like repeats](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system) | ⭐ 566 | 💬 588 | [HN Thread](https://news.ycombinator.com/item?id=49820134) |
| **3** | [Show HN: How long do I need to work at my salary before I can coast, or retire?](https://github.com/karmanyaahm/budget-tools/tree/main/fire) | ⭐ 24 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=49826059) |
| **4** | [Feds Target AI Critics as "Foreign Agents"](https://www.kenklippenstein.com/p/feds-think-ai-critics-are-foreign) | ⭐ 159 | 💬 133 | [HN Thread](https://news.ycombinator.com/item?id=49824686) |
| **5** | [ArXiv receives multiyear commitments to support it as an independent nonprofit](https://blog.arxiv.org/2026/09/23/arxiv-receives-multiyear-investment/) | ⭐ 102 | 💬 14 | [HN Thread](https://news.ycombinator.com/item?id=49823664) |
| **6** | [Making portable my unportable transputer C compiler](https://nanochess.org/transputer_c_compiler.html) | ⭐ 14 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=49795600) |
| **7** | [VSCode's SSH Agent Is Bananas (2025)](https://fly.io/blog/vscode-ssh-wtf/) | ⭐ 161 | 💬 104 | [HN Thread](https://news.ycombinator.com/item?id=49822555) |
| **8** | [Virtio-nvgpu: Near-native Nvidia GPU access inside a KVM guest](https://github.com/nestrilabs/virtio-nvgpu) | ⭐ 40 | 💬 16 | [HN Thread](https://news.ycombinator.com/item?id=49824864) |
| **9** | [The "Windows XP Box" (2003)](https://www.mini-itx.com/projects/windowsxpbox/) | ⭐ 93 | 💬 12 | [HN Thread](https://news.ycombinator.com/item?id=49796372) |
| **10** | [Meta VR Glasses](https://www.meta.com/vr-glasses/) | ⭐ 309 | 💬 272 | [HN Thread](https://news.ycombinator.com/item?id=49824268) |

---

## 🗄️ News Archive

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
- 📅 [2026-09-09](archive/2026-09-09.md)

*... and [26 older editions in the archive folder](archive/)*

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
