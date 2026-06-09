# Customer Churn Analysis Report
**Virtual Work Lab — Data Analytics Internship | Task 2**  
*June 2026*

---

## Executive Summary

Monthly churn has risen to **8.4%** (+1.2 percentage points month-over-month), with 1,247 users cancelling in the last 30 days and approximately **$94,000 MRR at risk**. The average customer churns after only 4.2 months — well before reaching full product value. Immediate action on onboarding, re-engagement automation, and integration adoption could reduce churn by an estimated 25–35% within 90 days.

---

## 1. Churn Trend

Churn has increased steadily over the past six months:

| Month | Churn Rate |
|---|---|
| January | 5.1% |
| February | 5.6% |
| March | 6.0% |
| April | 6.8% |
| May | 7.2% |
| June | 8.4% |

The consistent upward trajectory suggests systemic product-market fit or engagement issues rather than a one-time event.

---

## 2. Churn by Tier

| Tier | Users | Churn Rate |
|---|---|---|
| Basic | ~14,800 | 14.0% |
| Pro | ~8,200 | 8.0% |
| Enterprise | ~480 | 1.9% |

Basic-tier users are the most at-risk group. The strong retention in Enterprise accounts reflects dedicated CSM support and deeper integration into customer workflows.

---

## 3. Why Customers Leave (Exit Survey)

Exit survey responses (n = 847, 68% response rate):

| Reason | Share |
|---|---|
| Price too high | 34% |
| Missing features | 28% |
| Bugs / reliability issues | 21% |
| Other | 17% |

Price and missing features together account for 62% of exits, pointing to product-value misalignment for lower-tier customers.

---

## 4. Behavioral Signals

Analysis of user activity data reveals the following as the strongest predictors of churn:

| Signal | % of Churned Users |
|---|---|
| No login within 14 days | 88% |
| < 3 core feature uses/week | 74% |
| 2+ support contacts | 63% |
| Skipped onboarding steps | 58% |
| No team collaboration | 47% |
| No integration connected | 41% |

Inactivity is the clearest signal. A user who hasn't logged in within 14 days has a very high probability of churning without intervention.

---

## 5. Engagement vs Churn Correlation

There is a strong negative correlation between engagement score and churn rate:

- Score 0–20 → ~20% churn
- Score 40–60 → ~7% churn
- Score 80–100 → ~2% churn

The most powerful single action is connecting an integration: users with at least one integration connected churn at **3.2%** compared to **11.8%** for those without — a 3.7× difference.

---

## 6. At-Risk Segments

| Segment | Users | Churn Rate | Risk Level |
|---|---|---|---|
| Basic — month 1–2 | 3,410 | 18.2% | 🔴 Critical |
| Pro — solo users | 1,820 | 12.7% | 🔴 High |
| Basic — month 3–6 | 5,200 | 9.4% | 🟡 Moderate |
| Pro — small team (2–5) | 2,140 | 5.1% | 🟡 Watch |
| Enterprise — all | 480 | 1.9% | 🟢 Stable |

---

## 7. Recommendations

### Priority 1 — Redesign Onboarding
58% of churned users skipped onboarding. A guided, milestone-based onboarding with a 7-day activation email sequence should significantly reduce early churn. Estimated impact: **−40% churn in months 1–2**.

### Priority 2 — Automated Re-engagement
Trigger a personalized email at day 7 of inactivity, with an offer for a 1:1 check-in call at day 14. This catches users before cancellation intent solidifies. Estimated recovery: **15–20% of at-risk accounts**.

### Priority 3 — Collaboration Nudges
Solo Pro users churn 2.5× more than team accounts. Prompt team invites within 72 hrs and offer a referral discount on additional seats.

### Priority 4 — Integration Adoption
Add an integration wizard to the onboarding flow. Surface 3 recommended integrations on the new-user dashboard. Goal: increase integration adoption from 28% to 50%.

### Priority 5 — Pricing Strategy Review
34% cite price as their reason for leaving. Consider a lightweight free tier, usage-based pricing for low-volume users, and an annual plan at 15–20% discount.

### Priority 6 — Support Escalation Flow
Users with 2+ support tickets show 63% churn likelihood. Auto-route these users to a CSM and follow up within 24 hrs of every ticket resolution.

---

## 8. Methodology

- **Data sources**: subscription records, event telemetry, support tickets, exit surveys
- **Analysis window**: 6-month rolling cohort (Jan–Jun 2026)
- **Churn definition**: subscription cancelled and not renewed within 30 days
- **Predictive model**: logistic regression on behavioral features (AUC = 0.81)
- **Exit survey**: n = 847 respondents, ~68% response rate, collected at cancellation

---

*Report prepared by [Your Name] · Virtual Work Lab Data Analytics Internship · Task 2*
