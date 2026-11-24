import pandas as pd
import pytest
from telemetry import generate, summarize


def test_reproducibility():
    pd.testing.assert_frame_equal(generate(100, 42), generate(100, 42))


def test_complete_loss():
    data = generate(100, missing_rate=1)
    assert summarize(data)["missing_pct"] == 100
    assert summarize(data)["p95_latency_ms"] is None
    assert data["temperature_c"].isna().all()


def test_no_loss():
    data = generate(100, missing_rate=0)
    assert summarize(data)["missing_pct"] == 0
    assert summarize(data)["p95_latency_ms"] > 0


@pytest.mark.parametrize("n", [0, -1, 100001])
def test_invalid_size(n):
    with pytest.raises(ValueError):
        generate(n)
