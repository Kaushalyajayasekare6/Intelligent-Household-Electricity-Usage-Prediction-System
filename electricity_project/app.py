import streamlit as st
import pandas as pd
import joblib

# Page settings
st.set_page_config(
    page_title="Electricity Usage Calculator",
    layout="centered"
)

# Custom styling (white theme with black text and visible button)
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
    background-color: #f4f7f5;
    color: black;
}

/* Force all text to black */
html, body, [class*="css"] {
    color: black !important;
}

/* Titles */
.title {
    font-size: 36px;
    font-weight: 700;
    text-align: center;
    color: #1b5e20;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: black;
    margin-bottom: 25px;
}

/* Section title */
.section-title {
    color: #1b5e20;
    font-weight: 600;
    margin-bottom: 15px;
    font-size: 18px;
}

/* Button styling */
.stButton>button {
    background-color: #2e7d32;
    color: white !important;
    font-weight: 600;
    border-radius: 8px;
    height: 45px;
    border: none;
}

.stButton>button:hover {
    background-color: #1b5e20;
    color: white !important;
}

/* Result box */
.result-card {
    padding: 30px;
    border-radius: 12px;
    text-align: center;
    font-size: 32px;
    font-weight: bold;
    margin-top: 20px;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Load model
try:
    model = joblib.load("daily_electricity_model.pkl")
except:
    st.error("Model failed to load.")
    st.stop()

# Header
st.markdown('<div class="title">Household Electricity Usage</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Daily electricity consumption estimator</div>', unsafe_allow_html=True)

# Section title
st.markdown('<div class="section-title">Appliance Inputs</div>', unsafe_allow_html=True)

# Input columns
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Low-power devices**")
    st.caption("Lights, chargers")
    low_devices = st.number_input("Number of devices", 0, step=1, key="low_d")
    low_hours = st.slider("Usage hours", 0.0, 24.0, 0.0, 0.5, key="low_h")

with col2:
    st.markdown("**Medium-power devices**")
    st.caption("Fans, TVs")
    medium_devices = st.number_input("Number of devices", 0, step=1, key="med_d")
    medium_hours = st.slider("Usage hours", 0.0, 24.0, 0.0, 0.5, key="med_h")

with col3:
    st.markdown("**High-power devices**")
    st.caption("Fridge, AC")
    high_devices = st.number_input("Number of devices", 0, step=1, key="high_d")
    high_hours = st.slider("Usage hours", 0.0, 24.0, 0.0, 0.5, key="high_h")

calculate = st.button("Calculate Daily Usage", use_container_width=True)

# Prediction logic
if calculate:
    if (low_devices == 0 and low_hours == 0 and
        medium_devices == 0 and medium_hours == 0 and
        high_devices == 0 and high_hours == 0):

        st.warning("Please enter appliance usage.")
    else:
        # Convert devices × hours into usage features
        input_df = pd.DataFrame({
            "low_usage": [low_devices * low_hours],
            "medium_usage": [medium_devices * medium_hours],
            "high_usage": [high_devices * high_hours]
        })

        # Predict
        prediction = model.predict(input_df)[0]
        prediction = max(prediction, 0)

        # Color selection
        if prediction < 3:
            color = "#2e7d32"   # green
            label = "Low usage"
        elif prediction < 7:
            color = "#f9a825"   # amber
            label = "Moderate usage"
        else:
            color = "#c62828"   # red
            label = "High usage"

        st.markdown(
            f'<div class="result-card" style="background:{color};">'
            f'{prediction:.2f} kWh/day</div>',
            unsafe_allow_html=True
        )

        st.info(label)
