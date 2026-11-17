# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Java4Shell: RCE in OpenJDK when processing Base64](https://calif.io/java4shell/) | ⭐ 247 | 💬 74 | [HN Thread](https://news.ycombinator.com/item?id=50538240) |
| **2** | [GPT‑6.2 Astra and Sol](https://openai.com/index/introducing-gpt-6-2-astra-sol/) | ⭐ 975 | 💬 602 | [HN Thread](https://news.ycombinator.com/item?id=50535230) |
| **3** | [Quad9's withdrawal from France: A canary in the coal mine](https://blog.cloudflare.com/quad9-withdrawal-from-france/) | ⭐ 63 | 💬 2 | [HN Thread](https://news.ycombinator.com/item?id=50538994) |
| **4** | [jQuery 4.1.0](https://github.com/jquery/jquery/releases/tag/4.1.0) | ⭐ 200 | 💬 103 | [HN Thread](https://news.ycombinator.com/item?id=50537156) |
| **5** | [Nvidia stopped disclosing Singapore sales as revenues hit $104B](https://www.ft.com/content/dbde7a30-548c-4f9d-a4be-7898a0c24dcf) | ⭐ 282 | 💬 153 | [HN Thread](https://news.ycombinator.com/item?id=50534631) |
| **6** | [MAI Code 2 and Code 2 Flash](https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/) | ⭐ 238 | 💬 111 | [HN Thread](https://news.ycombinator.com/item?id=50535885) |
| **7** | [Phrack 73 Released](https://phrack.org/issues/73/introduction_md) | ⭐ 207 | 💬 20 | [HN Thread](https://news.ycombinator.com/item?id=50535992) |
| **8** | [350 years ago, Ole Rømer discovered that light has a finite speed](https://www.sciencenorway.no/culture-history-history-of-science/350-years-ago-this-man-discovered-that-light-has-a-finite-speed/2737969) | ⭐ 189 | 💬 61 | [HN Thread](https://news.ycombinator.com/item?id=50536813) |
| **9** | [Highly classified US national security communications network goes down](https://www.cnn.com/2026/11/17/politics/highly-classified-national-security-communications-network-goes-down) | ⭐ 385 | 💬 496 | [HN Thread](https://news.ycombinator.com/item?id=50532849) |
| **10** | [Web Browser Engineering (2021)](https://browser.engineering/) | ⭐ 97 | 💬 17 | [HN Thread](https://news.ycombinator.com/item?id=50537290) |

---

## 🗄️ News Archive

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
- 📅 [2026-11-04](archive/2026-11-04.md)
- 📅 [2026-11-03](archive/2026-11-03.md)
- 📅 [2026-11-02](archive/2026-11-02.md)

*... and [73 older editions in the archive folder](archive/)*

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
