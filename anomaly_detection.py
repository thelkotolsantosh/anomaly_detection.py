"""Flag unusually high login counts using a mean-plus-deviation threshold."""

import numpy as np
import pandas as pd


def generate_login_data(n_records=500, n_users=20, seed=7):
    if n_records < 0 or n_users < 1:
        raise ValueError("Use a nonnegative record count and at least one user.")
    rng = np.random.default_rng(seed)
    return pd.DataFrame({
        "user": [f"user_{i}" for i in rng.integers(1, n_users + 1, n_records)],
        "logins": rng.poisson(3, n_records),
    })


def detect_anomalies(df, std_multiplier=2):
    if "logins" not in df:
        raise ValueError("Missing logins column.")
    if not np.isfinite(std_multiplier) or std_multiplier < 0:
        raise ValueError("std_multiplier must be finite and nonnegative.")
    values = pd.to_numeric(df["logins"], errors="raise")
    if values.isna().any() or (~np.isfinite(values)).any() or (values < 0).any():
        raise ValueError("Login counts must be finite and nonnegative.")
    mean = float(values.mean()) if len(values) else 0.0
    std = float(values.std()) if len(values) > 1 else 0.0
    threshold = mean + std_multiplier * std
    anomalies = df.loc[values > threshold].copy()
    return anomalies, {
        "mean": mean, "std": std, "threshold": threshold,
        "std_multiplier": std_multiplier, "total_records": len(df),
        "anomaly_count": len(anomalies),
        "anomaly_percentage": len(anomalies) / len(df) * 100 if len(df) else 0.0,
    }


def main():
    anomalies, stats = detect_anomalies(generate_login_data())
    print(pd.Series(stats).to_string())
    print(anomalies.to_string(index=False))


if __name__ == "__main__":
    main()
