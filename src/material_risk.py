import pandas as pd
from pathlib import Path
from risk_engine import calculate_risk

data_file = Path(__file__).parent.parent / "data" / "materials.csv"
df = pd.read_csv(data_file)

df["Risk Score"] = df.apply(
    lambda row: calculate_risk(
        row["Strength"],
        row["Corrosion"]
    ),
    axis=1
)

print(df)