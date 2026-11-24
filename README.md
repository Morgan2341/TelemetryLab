# TelemetryLab

Interactive data quality dashboard for synthetic environmental sensor measurements, built with Python, NumPy, pandas and Streamlit.

## Features
- Seeded, reproducible synthetic measurements
- Missing-data percentage and latency quantiles
- Interactive sample count and missing-measurement controls
- Temperature and latency time-series charts
- CSV download
- Data-generation tests and dashboard interaction tests

## Run locally
Python 3.11+:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

On Windows PowerShell, activate using .venv/Scripts/Activate.ps1 instead.

## Run using Docker
```bash
docker build -t telemetrylab .
docker run --rm -p 127.0.0.1:8501:8501 telemetrylab
```

Open http://localhost:8501.

## Tests
```bash
python -m pytest -q
```

## Architecture
- telemetry.py: synthetic generation and descriptive statistics
- app.py: interactive dashboard and CSV export
- test_telemetry.py: data generation and statistical edge cases
- test_dashboard.py: dashboard startup and interaction
- .github/workflows/ci.yml: continuous testing

## Limitations
All data is simulated, not sourced from an employer or actual aircraft. The simulator illustrates generic sensor data quality, not validated physical communications behavior. Execution and CI results have not yet been independently verified.

Developed with AI assistance as a learning portfolio project.
