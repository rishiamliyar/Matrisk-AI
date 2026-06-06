import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
import sys
from pathlib import Path
# pyrefly: ignore [missing-import]
from src.asset_risk import asset_multiplier

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))

from src.esg_risk import esg_score

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
asset = st.selectbox(
    "Infrastructure Asset",
    [
        "Bridge",
        "Power Plant",
        "Pipeline",
        "Factory",
        "Warehouse"
    ]
)
strength = st.slider("Material Strength", 0, 100, 80)
corrosion = st.slider("Corrosion Level", 0, 50, 10)

# ML prediction
input_data = pd.DataFrame({
    "Strength": [strength],
    "Corrosion": [corrosion]
})

predicted_risk = model.predict(input_data)[0]
asset_risk = predicted_risk * asset_multiplier(asset)

esg = esg_score(material)

portfolio_risk = (
    asset_risk +
    (100 - esg)
) / 2

portfolio_risk = (
    predicted_risk + (100 - esg)
) / 2

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Predicted Risk",
        round(predicted_risk, 2)
    )

    st.metric(
        "Asset Risk",
        round(asset_risk, 2)
    )

    st.metric(
        "ESG Score",
        esg
    )

    st.metric(
        "Portfolio Risk",
        round(portfolio_risk, 2)
    )
with col2:
    if predicted_risk < 20:
        st.success("Low Risk")
    elif predicted_risk < 50:
        st.warning("Medium Risk")
    else:
        st.error("High Risk")

chart_df = pd.DataFrame({
    "Metric": [
        "Strength",
        "Corrosion",
        "Predicted Risk",
        "Asset Risk",
        "Portfolio Risk"
    ],
    "Value": [
        strength,
        corrosion,
        predicted_risk,
        asset_risk,
        portfolio_risk
    ]
})

st.bar_chart(chart_df.set_index("Metric"))