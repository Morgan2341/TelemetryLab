import streamlit as st
from telemetry import generate, summarize

st.set_page_config(page_title="TelemetryLab", layout="wide")
st.title("TelemetryLab | Sensor data quality")
st.caption("Synthetic environmental sensor measurements — no real flight or employer data.")
n = st.sidebar.slider("Samples", 100, 10000, 1000, 100)
seed = st.sidebar.number_input("Random seed", 0, 1000000, 42)
missing = st.sidebar.slider("Missing measurement probability", 0.0, 0.5, 0.05, 0.01)
data = generate(n, int(seed), missing)
stats = summarize(data)
a, b, c = st.columns(3)
a.metric("Samples", stats["samples"])
b.metric("Missing measurements", f'{stats["missing_pct"]:.1f}%')
p95 = stats["p95_latency_ms"]
c.metric("95th percentile latency", f"{p95:.1f} ms" if p95 is not None else "N/A")
st.subheader("Temperature measurements")
st.line_chart(data.set_index("timestamp")["temperature_c"])
st.subheader("Measurement latency")
st.line_chart(data.set_index("timestamp")["latency_ms"])
st.subheader("Dataset preview")
st.dataframe(data.head(100))
st.download_button("Export CSV", data.to_csv(index=False), "telemetry.csv", "text/csv")
