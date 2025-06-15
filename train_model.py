import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle

# Load data
data = pd.read_csv('behavior_data.csv')

# Train model
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(data)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Isolation Forest Model Trained & Saved")
