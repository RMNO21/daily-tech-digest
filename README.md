# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Pill to treat pancreatic cancer hailed as 'biggest breakthrough in decades'](https://www.theguardian.com/society/2026/nov/20/pill-pancreatic-cancer-breakthrough-daraxonrasib) | ⭐ 412 | 💬 116 | [HN Thread](https://news.ycombinator.com/item?id=50582069) |
| **2** | [Inkling-2-Mini in 5.4 GB Memory](https://github.com/ShinMegamiBoson/lookatmyquant) | ⭐ 309 | 💬 78 | [HN Thread](https://news.ycombinator.com/item?id=50591853) |
| **3** | [Lean verification of the Riemann Hypothesis](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) | ⭐ 741 | 💬 592 | [HN Thread](https://news.ycombinator.com/item?id=50589618) |
| **4** | [Detonating a pile of lead azide](https://www.science.org/content/blog-post/detonating-huge-pile-lead-azide-really) | ⭐ 482 | 💬 314 | [HN Thread](https://news.ycombinator.com/item?id=50588982) |
| **5** | [Brazil's tax authority open-sources its tax calculator on GitHub under MIT](https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2026/novembro/receita-federal-publica-primeiro-codigo-fonte-aberto-no-github-e-amplia-transparencia-da-reforma-tributaria) | ⭐ 683 | 💬 222 | [HN Thread](https://news.ycombinator.com/item?id=50532613) |
| **6** | [Getting the mind to steer the body to steer you](https://notnottalmud.substack.com/p/getting-the-mind-to-steer-the-body) | ⭐ 102 | 💬 40 | [HN Thread](https://news.ycombinator.com/item?id=50583028) |
| **7** | [PcapAnalyzer – self-hosted pcap analyzer with 27 problem detectors](https://github.com/sebaandrada-cell/PcapAnalyzer) | ⭐ 21 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=50594132) |
| **8** | [Advice for the next 100 Rust GUIs](https://linebender.org/blog/next-100-guis/) | ⭐ 24 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=50593737) |
| **9** | [Windows has two settings that bring work back after restart, both off by default](https://www.makeuseof.com/windows-can-bring-your-work-back-after-restart/) | ⭐ 20 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=50560203) |
| **10** | [Tasklet (YC P26) Is Hiring Product and Agent Infra Engineers](https://tasklet.ai/careers) | ⭐ 1 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50593679) |

---

## 🗄️ News Archive

- 📅 [2026-11-21](archive/2026-11-21.md)
- 📅 [2026-11-19](archive/2026-11-19.md)
- 📅 [2026-11-18](archive/2026-11-18.md)
- 📅 [2026-11-17](archive/2026-11-17.md)
- 📅 [2026-11-16](archive/2026-11-16.md)
- 📅 [2026-11-15](archive/2026-11-15.md)
- 📅 [2026-11-14](archive/2026-11-14.md)
- 📅 [2026-11-11](archive/2026-11-11.md)
- 📅 [2026-11-10](archive/2026-11-10.md)
- 📅 [2026-11-09](archive/2026-11-09.md)
- 📅 [2026-11-08](archive/2026-11-08.md)
- 📅 [2026-11-07](archive/2026-11-07.md)
- 📅 [2026-11-06](archive/2026-11-06.md)
- 📅 [2026-11-05](archive/2026-11-05.md)

*... and [76 older editions in the archive folder](archive/)*

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
