import streamlit as st
import pandas as pd

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

risk = (100 - strength) + corrosion

col1, col2 = st.columns(2)

with col1:
    st.metric("Risk Score", risk)

with col2:
    if risk < 20:
        st.success("Low Risk")
    elif risk < 50:
        st.warning("Medium Risk")
    else:
        st.error("High Risk")

df = pd.DataFrame({
    "Metric": ["Strength", "Corrosion", "Risk"],
    "Value": [strength, corrosion, risk]
})

st.bar_chart(df.set_index("Metric"))