# 📊 Customer Churn Analysis
### Virtual Work Lab — Data Analytics Internship

![Status](https://img.shields.io/badge/status-completed-brightgreen)
![Task](https://img.shields.io/badge/task-2-blue)
![Python](https://img.shields.io/badge/python-3.10+-yellow)

---

## 🗂️ Project Overview

This project analyzes customer subscription data to identify patterns behind cancellations, evaluate engagement levels, and surface actionable retention strategies.

**Intern:** [Your Name]  
**Track:** Data Analytics  
**Task ID:** Task 2 — Customer Churn Analysis  
**Period:** June 2026

---

## 📁 Repository Structure

```
vwl-internship-churn/
│
├── README.md                        ← You are here
├── requirements.txt                 ← Python dependencies
├── .gitignore
│
├── data/
│   ├── raw/                         ← Original dataset (not tracked by git)
│   └── processed/                   ← Cleaned, feature-engineered data
│
├── notebooks/
│   └── churn_analysis.ipynb         ← Main analysis notebook
│
├── src/
│   └── churn_utils.py               ← Helper functions
│
├── reports/
│   ├── churn_analysis_report.md     ← Written findings
│   └── customer_churn_analysis.html ← Interactive dashboard
│
└── assets/
    └── charts/                      ← Exported chart images
```

---

## 🔍 Key Findings

| Metric | Value |
|---|---|
| Monthly churn rate | **8.4%** (▲ +1.2pp MoM) |
| Churned users (30d) | **1,247** |
| Avg tenure at churn | **4.2 months** |
| MRR at risk | **$94,000** |

### Top Churn Drivers

| # | Behavioral Signal | Churn Correlation |
|---|---|---|
| 1 | No login within 14 days | 88% |
| 2 | < 3 core feature uses/week | 74% |
| 3 | 2+ support contacts | 63% |
| 4 | Skipped onboarding | 58% |
| 5 | No team collaboration | 47% |
| 6 | No integration connected | 41% |

### Churn by Tier

| Tier | Churn Rate | Risk |
|---|---|---|
| Basic | 14.0% | 🔴 High |
| Pro | 8.0% | 🟡 Moderate |
| Enterprise | 1.9% | 🟢 Stable |

---

## 💡 Retention Recommendations

| Priority | Action | Expected Impact |
|---|---|---|
| 🔴 High | Redesign onboarding with activation checklist | −40% early churn |
| 🔴 High | Auto re-engagement at day 7 / CSM call at day 14 | +15–20% recovery |
| 🟡 Medium | Incentivize team invite within 72 hrs of signup | −2.5× solo churn |
| 🟡 Medium | Integration setup wizard in onboarding flow | −8.6pp churn rate |
| 🟡 Medium | Annual plan discount + usage-based pricing tier | Address 34% price exits |
| 🟢 Quick Win | Route repeat support users to CSM proactively | −25% post-support churn |

---

## 🛠️ Tech Stack

- **Python 3.10+** — data processing & analysis
- **pandas / numpy** — data wrangling
- **matplotlib / seaborn** — visualizations
- **scikit-learn** — churn prediction model (logistic regression)
- **Chart.js** — interactive HTML dashboard

---

## 🚀 Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/vwl-internship-churn.git
cd vwl-internship-churn

# 2. Install dependencies
pip install -r requirements.txt

# 3. Open the analysis notebook
jupyter notebook notebooks/churn_analysis.ipynb

# 4. View the interactive dashboard
open reports/customer_churn_analysis.html
```

---

## 📈 Methodology

- **Behavioral telemetry**: login frequency, feature usage depth, session patterns
- **Exit survey analysis**: n = 847 responses (~68% response rate)
- **Cohort analysis**: 6-month rolling window, segmented by tier and signup date
- **Predictive modeling**: logistic regression on engagement features (AUC = 0.81)

---

## 📄 License

This project was completed as part of the [Virtual Work Lab](https://virtualworklab.com) internship program.

---

*Last updated: June 2026*
