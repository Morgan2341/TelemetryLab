"""Reproducible synthetic environmental sensor telemetry."""
import numpy as np
import pandas as pd


def generate(n: int = 1000, seed: int = 42, missing_rate: float = 0.05) -> pd.DataFrame:
    if not 1 <= n <= 100000:
        raise ValueError("n must be between 1 and 100000")
    if not 0 <= missing_rate <= 1:
        raise ValueError("missing_rate must be between 0 and 1")
    rng = np.random.default_rng(seed)
    received = rng.random(n) >= missing_rate
    return pd.DataFrame({
        "timestamp": pd.date_range("2025-01-01", periods=n, freq="s", tz="UTC"),
        "received": received,
        "temperature_c": np.where(received, rng.normal(21, 2, n), np.nan),
        "latency_ms": np.where(received, rng.lognormal(3.5, 0.35, n), np.nan),
    })


def summarize(data: pd.DataFrame) -> dict:
    if data.empty:
        raise ValueError("data must not be empty")
    latency = data.loc[data["received"], "latency_ms"]
    return {
        "samples": len(data),
        "missing_pct": 100 * float((~data["received"]).mean()),
        "median_latency_ms": float(latency.median()) if latency.notna().any() else None,
        "p95_latency_ms": float(latency.quantile(0.95)) if latency.notna().any() else None,
    }
