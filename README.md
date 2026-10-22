# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Quad9 (DNS Resolver) to Exit France](https://quad9.net/news/blog/au-revoir-france/) | ⭐ 846 | 💬 318 | [HN Thread](https://news.ycombinator.com/item?id=50195959) |
| **2** | [OpenShell – A safe, private runtime for fleets of autonomous AI agents](https://github.com/NVIDIA/OpenShell) | ⭐ 229 | 💬 124 | [HN Thread](https://news.ycombinator.com/item?id=50198675) |
| **3** | [Getting ready to operate GNU Taler in Germany](https://www.taler.net/en/news/2026-13.html) | ⭐ 183 | 💬 62 | [HN Thread](https://news.ycombinator.com/item?id=50197404) |
| **4** | [Show HN: Run full iOS 16.5 firmware on Android Devices](https://github.com/oosexgang/hackios-xnu-kernel) | ⭐ 274 | 💬 100 | [HN Thread](https://news.ycombinator.com/item?id=50196718) |
| **5** | [Woman faces six years in prison over Cash App account she never opened](https://www.techspot.com/news/114296-woman-spends-three-nights-jail-faces-six-years.html) | ⭐ 360 | 💬 344 | [HN Thread](https://news.ycombinator.com/item?id=50194833) |
| **6** | [Every AI model has the same "controversial" take on humans](https://www.modelcompare.ai/blog/ai-models-controversial-take-on-humans) | ⭐ 131 | 💬 158 | [HN Thread](https://news.ycombinator.com/item?id=50197313) |
| **7** | [AI and the Enclosure of the Scientific Commons](https://arxiv.org/abs/2610.27251) | ⭐ 81 | 💬 44 | [HN Thread](https://news.ycombinator.com/item?id=50199230) |
| **8** | [Hedra is a 3D open world game I wrote from scratch while in highschool](https://github.com/maxilevi/project-hedra/tree/pre-ai) | ⭐ 84 | 💬 18 | [HN Thread](https://news.ycombinator.com/item?id=50199389) |
| **9** | [What Is Gridifcation](https://musicalform.substack.com/p/what-is-gridifcation) | ⭐ 371 | 💬 184 | [HN Thread](https://news.ycombinator.com/item?id=50150163) |
| **10** | [Jailbreaking the Switch 2](https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/) | ⭐ 661 | 💬 231 | [HN Thread](https://news.ycombinator.com/item?id=50192536) |

---

## 🗄️ News Archive

- 📅 [2026-10-22](archive/2026-10-22.md)
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

*... and [51 older editions in the archive folder](archive/)*

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
