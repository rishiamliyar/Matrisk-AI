# 📊 MatRisk AI

## Overview

MatRisk AI is a machine learning-powered risk assessment platform that combines material science, infrastructure risk analysis, ESG evaluation, and financial risk modeling.

The system predicts material-related risks, evaluates infrastructure asset exposure, calculates ESG scores, and simulates real-world shock events to estimate portfolio risk.

---

## Key Features

### 🤖 Machine Learning Risk Prediction

* Trained using Scikit-Learn
* Predicts material risk based on:

  * Material Strength
  * Corrosion Level

### 🏗 Infrastructure Asset Risk Analysis

Supported assets:

* Bridge
* Power Plant
* Pipeline
* Factory
* Warehouse

Each asset has a unique risk multiplier that affects overall exposure.

### 🌱 ESG Risk Scoring

Environmental, Social, and Governance (ESG) scoring for materials:

* Steel
* Aluminum
* Copper
* Titanium
* Concrete

### 📈 Portfolio Risk Calculation

Combines:

* Predicted Material Risk
* Asset Exposure
* ESG Performance

to generate an overall Portfolio Risk Score.

### ⚡ Shock Event Simulation

Simulate real-world risk events:

* Steel Price Spike
* Corrosion Failure
* Supply Chain Disruption
* Natural Disaster

and analyze their impact on portfolio risk.

### 📊 Interactive Dashboard

Built with Streamlit:

* Material selection
* Asset selection
* Risk visualization
* ESG analytics
* Shock simulation
* Portfolio monitoring

---

## System Architecture

```text
Material Properties
        │
        ▼
Machine Learning Model
        │
        ▼
Predicted Risk
        │
        ├────────► ESG Analysis
        │
        ├────────► Asset Risk Analysis
        │
        ▼
Portfolio Risk Engine
        │
        ▼
Shock Event Simulation
        │
        ▼
Interactive Dashboard
```

---

## Project Structure

```text
MatRisk-AI/
│
├── dashboard/
│   └── app.py
│
├── data/
│   └── materials.csv
│
├── docs/
│
├── models/
│   └── risk_model.pkl
│
├── notebooks/
│
├── src/
│   ├── asset_risk.py
│   ├── esg_risk.py
│   ├── financial_risk.py
│   ├── material_risk.py
│   ├── risk_engine.py
│   ├── shock_simulator.py
│   └── train_model.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Technology Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Joblib
* Git & GitHub

---

## Installation

### Clone Repository

```bash
git clone https://github.com/rishiamliyar/Matrisk-AI.git
cd Matrisk-AI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Dashboard

```bash
python -m streamlit run dashboard/app.py
```

---

## Example Workflow

1. Select a Material
2. Select an Infrastructure Asset
3. Adjust Strength and Corrosion
4. View ML Predicted Risk
5. Analyze ESG Score
6. Calculate Portfolio Risk
7. Simulate Shock Events
8. Monitor Risk Changes in Real Time

---

## Future Improvements

* Commodity Trading Risk Module
* Infrastructure Portfolio Management
* Insurance Risk Analytics
* ESG Portfolio Optimization
* Real-Time Market Data Integration
* PDF Risk Report Generation
* Advanced Predictive Models

---

## Author

**Rishi Amliyar**

GitHub: https://github.com/rishiamliyar

---

## Project Status

✅ Material Risk Analysis

✅ Machine Learning Prediction

✅ ESG Risk Scoring

✅ Asset Risk Modeling

✅ Portfolio Risk Engine

✅ Shock Event Simulation

✅ Interactive Dashboard

✅ GitHub Integration

🚀 Active Development
