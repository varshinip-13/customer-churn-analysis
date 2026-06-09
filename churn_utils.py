"""
churn_utils.py
Helper functions for Customer Churn Analysis
Virtual Work Lab Internship — Task 2
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ── Data loading & cleaning ───────────────────────────────────────────────────

def load_data(filepath: str) -> pd.DataFrame:
    """Load customer dataset and perform basic cleaning."""
    df = pd.read_csv(filepath, parse_dates=["signup_date", "last_login_date"])
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    df = df.drop_duplicates(subset="customer_id")
    return df


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create derived features for churn prediction."""
    df = df.copy()
    today = pd.Timestamp.today()

    df["days_since_login"] = (today - df["last_login_date"]).dt.days
    df["tenure_days"] = (today - df["signup_date"]).dt.days
    df["tenure_months"] = df["tenure_days"] / 30

    df["is_inactive_14d"] = (df["days_since_login"] > 14).astype(int)
    df["low_feature_usage"] = (df["weekly_feature_uses"] < 3).astype(int)
    df["repeat_support"] = (df["support_tickets"] >= 2).astype(int)
    df["skipped_onboarding"] = (df["onboarding_completion_pct"] < 50).astype(int)
    df["is_solo_user"] = (df["team_size"] == 1).astype(int)
    df["no_integration"] = (df["integrations_connected"] == 0).astype(int)

    df["churn_risk_score"] = (
        df["is_inactive_14d"] * 0.30 +
        df["low_feature_usage"] * 0.20 +
        df["repeat_support"] * 0.18 +
        df["skipped_onboarding"] * 0.16 +
        df["is_solo_user"] * 0.10 +
        df["no_integration"] * 0.06
    )

    return df


# ── Analysis helpers ──────────────────────────────────────────────────────────

def churn_rate_by_group(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """Calculate churn rate for each value in a grouping column."""
    return (
        df.groupby(group_col)["churned"]
        .agg(total="count", churned="sum")
        .assign(churn_rate=lambda x: (x["churned"] / x["total"] * 100).round(1))
        .sort_values("churn_rate", ascending=False)
    )


def top_churn_signals(df: pd.DataFrame) -> pd.DataFrame:
    """Return the percentage of churned users who showed each risk signal."""
    churned = df[df["churned"] == 1]
    signals = {
        "No login 14+ days":        churned["is_inactive_14d"].mean(),
        "Low feature usage":         churned["low_feature_usage"].mean(),
        "Repeat support contacts":   churned["repeat_support"].mean(),
        "Skipped onboarding":        churned["skipped_onboarding"].mean(),
        "Solo user (no team)":       churned["is_solo_user"].mean(),
        "No integration connected":  churned["no_integration"].mean(),
    }
    return (
        pd.DataFrame.from_dict(signals, orient="index", columns=["pct_of_churned"])
        .sort_values("pct_of_churned", ascending=False)
        .assign(pct_of_churned=lambda x: (x["pct_of_churned"] * 100).round(1))
    )


# ── Plotting ──────────────────────────────────────────────────────────────────

def plot_churn_trend(monthly_df: pd.DataFrame, save_path: str = None):
    """Plot monthly churn rate as a line chart."""
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(monthly_df["month"], monthly_df["churn_rate"],
            color="#E24B4A", linewidth=2.5, marker="o", markersize=5)
    ax.fill_between(monthly_df["month"], monthly_df["churn_rate"],
                    alpha=0.08, color="#E24B4A")
    ax.set_ylabel("Churn rate (%)")
    ax.set_title("Monthly churn rate trend", fontsize=13, fontweight="normal")
    ax.set_ylim(0, monthly_df["churn_rate"].max() * 1.3)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches="tight")
    return fig


def plot_churn_by_tier(df: pd.DataFrame, save_path: str = None):
    """Bar chart of churn rate by subscription tier."""
    rates = churn_rate_by_group(df, "subscription_tier")
    colors = {"Basic": "#378ADD", "Pro": "#D85A30", "Enterprise": "#1D9E75"}
    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(rates.index, rates["churn_rate"],
                  color=[colors.get(t, "#888780") for t in rates.index],
                  width=0.5, edgecolor="none")
    for bar, val in zip(bars, rates["churn_rate"]):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
                f"{val}%", ha="center", va="bottom", fontsize=11)
    ax.set_ylabel("Churn rate (%)")
    ax.set_title("Churn rate by subscription tier", fontsize=13, fontweight="normal")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches="tight")
    return fig


def plot_churn_drivers(df: pd.DataFrame, save_path: str = None):
    """Horizontal bar chart of top behavioral churn drivers."""
    signals = top_churn_signals(df)
    fig, ax = plt.subplots(figsize=(7, 4))
    colors = ["#E24B4A" if v >= 70 else "#EF9F27" if v >= 50 else "#378ADD"
              for v in signals["pct_of_churned"]]
    ax.barh(signals.index, signals["pct_of_churned"], color=colors, edgecolor="none")
    for i, val in enumerate(signals["pct_of_churned"]):
        ax.text(val + 0.5, i, f"{val}%", va="center", fontsize=10)
    ax.set_xlabel("% of churned users who showed this signal")
    ax.set_title("Top behavioral churn drivers", fontsize=13, fontweight="normal")
    ax.set_xlim(0, 105)
    ax.invert_yaxis()
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches="tight")
    return fig
