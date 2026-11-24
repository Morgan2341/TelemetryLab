# TelemetryLab

Interactive analysis of synthetic environmental sensor telemetry using Python, pandas, NumPy and Streamlit. No real aircraft or employer data is used.

## Quick start
Requires Python 3.11 or later.

```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell alternative: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

Choose a sample count, random seed and missing measurement probability. Explore temperature and latency charts, review summary statistics and export CSV.

## Architecture
- telemetry.py: seeded synthetic data generator and descriptive statistics
- app.py: interactive dashboard and export
- test_telemetry.py: reproducibility, missing-data edge cases and validation
- .github/workflows/ci.yml: automated pytest workflow

## Testing
```bash
python -m pytest -q
```

CI is configured; test execution has not been independently verified here. The simulated measurements are illustrative and are not a validated model of any physical communication system.

Developed with AI assistance as a learning portfolio project.
