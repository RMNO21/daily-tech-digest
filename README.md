# 📰 Daily Tech & AI Digest

[![Daily Tech Digest](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml/badge.svg)](https://github.com/RMNO21/daily-tech-digest/actions/workflows/daily-digest.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)

An automated **Tech & AI News Digest** that aggregates top trending discussions and articles from the developer community and maintains an organized history archive.

---

## 🚀 Latest News

| # | Story | Points | Comments | Discussion |
|:---:|:---|:---:|:---:|:---:|
| **1** | [Quad9 Is Leaving France: Why DNS Resolvers Are the Wrong Place to Fight Piracy](https://techstackups.com/articles/quad9-leaves-france-dns-blocking/) | ⭐ 85 | 💬 10 | [HN Thread](https://news.ycombinator.com/item?id=50545958) |
| **2** | [Can Peer Review Survive AI-Generated Text? [pdf]](https://www.sas.upenn.edu/~jesusfv/Peer_Review.pdf) | ⭐ 9 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50546312) |
| **3** | [Energy-Based Reasoners: 385x more efficient inference](https://energy-based-reasoners.github.io/) | ⭐ 172 | 💬 25 | [HN Thread](https://news.ycombinator.com/item?id=50543989) |
| **4** | [A Perfect SimCity](https://www.jeffquast.com/post/a-perfect-simcity/) | ⭐ 98 | 💬 22 | [HN Thread](https://news.ycombinator.com/item?id=50504373) |
| **5** | [Java4Shell: RCE in OpenJDK when processing Base64](https://calif.io/java4shell/) | ⭐ 1047 | 💬 277 | [HN Thread](https://news.ycombinator.com/item?id=50538240) |
| **6** | [When AI Knows More Than It Can Offer](https://medium.com/@smoking2man/when-ai-knows-more-than-it-can-offer-how-training-turns-an-intelligent-assistant-into-a-generator-7e700f05163e) | ⭐ 15 | 💬 1 | [HN Thread](https://news.ycombinator.com/item?id=50507918) |
| **7** | [Quad9's withdrawal from France: A canary in the coal mine](https://blog.cloudflare.com/quad9-withdrawal-from-france/) | ⭐ 769 | 💬 340 | [HN Thread](https://news.ycombinator.com/item?id=50538994) |
| **8** | [Google's AI answers reducing search traffic by 40%](https://revscope.co/blog/search-seo-geo-2026/) | ⭐ 553 | 💬 419 | [HN Thread](https://news.ycombinator.com/item?id=50540178) |
| **9** | [ID.me terms required for IRS sign-in](https://consumerrights.wiki/w/ID.me_terms_required_for_IRS_sign-in) | ⭐ 408 | 💬 203 | [HN Thread](https://news.ycombinator.com/item?id=50540437) |
| **10** | [Evidence (YC S21) Is Hiring](https://www.ycombinator.com/companies/evidence/jobs/1xb9PpP-founding-gtm-lead) | ⭐ 1 | 💬 0 | [HN Thread](https://news.ycombinator.com/item?id=50545238) |

---

## 🗄️ News Archive

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
- 📅 [2026-11-04](archive/2026-11-04.md)
- 📅 [2026-11-03](archive/2026-11-03.md)

*... and [74 older editions in the archive folder](archive/)*

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
