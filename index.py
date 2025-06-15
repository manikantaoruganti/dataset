import pandas as pd
import numpy as np

# Synthetic data generator
def generate_data(n_samples=1000):
    data = pd.DataFrame({
        'tap_pressure': np.random.normal(0.5, 0.1, n_samples),
        'swipe_speed': np.random.normal(0.6, 0.15, n_samples),
        'hold_time': np.random.normal(0.3, 0.05, n_samples),
        'typing_speed': np.random.normal(50, 10, n_samples),
        'device_tilt': np.random.normal(5, 2, n_samples),
        'location_distance': np.random.normal(3, 1, n_samples),
    })
    data.to_csv('behavior_data.csv', index=False)
    print("Synthetic behavioral data generated")

if __name__ == "__main__":
    generate_data()
    
