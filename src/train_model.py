import pandas as pd
from pathlib import Path
from sklearn.linear_model import LinearRegression

data_file = Path(__file__).parent.parent / "data" / "materials.csv"
df = pd.read_csv(data_file)

# Create target variable
df["Risk"] = (100 - df["Strength"]) + df["Corrosion"]

X = df[["Strength", "Corrosion"]]
y = df["Risk"]

model = LinearRegression()
model.fit(X, y)

prediction = model.predict(
    pd.DataFrame({
        "Strength": [80],
        "Corrosion": [8]
    })
)

print("Predicted Risk:", round(prediction[0], 2))