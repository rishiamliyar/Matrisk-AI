import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Load model
model_path = Path(__file__).parent.parent / "models" / "risk_model.pkl"
model = joblib.load(model_path)

st.set_page_config(
    page_title="MatRisk AI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 MatRisk AI Dashboard")

material = st.selectbox(
    "Select Material",
    ["Steel", "Aluminum", "Copper", "Titanium", "Concrete"]
)

strength = st.slider("Material Strength", 0, 100, 80)
corrosion = st.slider("Corrosion Level", 0, 50, 10)

# ML prediction
input_data = pd.DataFrame({
    "Strength": [strength],
    "Corrosion": [corrosion]
})

predicted_risk = model.predict(input_data)[0]

col1, col2 = st.columns(2)

with col1:
    st.metric("Predicted Risk", round(predicted_risk, 2))

with col2:
    if predicted_risk < 20:
        st.success("Low Risk")
    elif predicted_risk < 50:
        st.warning("Medium Risk")
    else:
        st.error("High Risk")

chart_df = pd.DataFrame({
    "Metric": ["Strength", "Corrosion", "Risk"],
    "Value": [strength, corrosion, predicted_risk]
})

st.bar_chart(chart_df.set_index("Metric"))