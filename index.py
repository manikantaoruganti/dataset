# dataset_generator.py
import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

def generate_behavioral_data(num_users=1000, num_sessions=50):
    data = []
    for user_id in range(1, num_users+1):
        base_typing_speed = np.random.normal(180, 15)
        base_swipe_speed = np.random.normal(500, 50)
        base_touch_pressure = np.random.normal(0.5, 0.1)
        base_accel_variance = np.random.normal(1.5, 0.3)

        for session in range(num_sessions):
            typing_speed = np.random.normal(base_typing_speed, 5)
            swipe_speed = np.random.normal(base_swipe_speed, 10)
            touch_pressure = np.random.normal(base_touch_pressure, 0.02)
            accel_variance = np.random.normal(base_accel_variance, 0.1)
            nav_pattern = np.random.randint(3, 12)
            geo_cluster = np.random.choice(["Home", "Office", "Travel", "Other"], p=[0.5, 0.3, 0.1, 0.1])

            label = 0  # Normal
            # Inject anomalies (5% chance)
            if np.random.rand() < 0.05:
                typing_speed *= np.random.uniform(0.5, 1.5)
                swipe_speed *= np.random.uniform(0.5, 1.5)
                touch_pressure *= np.random.uniform(0.3, 1.7)
                accel_variance *= np.random.uniform(0.5, 2)
                label = 1  # Anomaly

            data.append([
                user_id, typing_speed, swipe_speed, touch_pressure,
                accel_variance, nav_pattern, geo_cluster, label
            ])

    columns = [
        'user_id', 'typing_speed', 'swipe_speed', 'touch_pressure',
        'accel_variance', 'nav_pattern', 'geo_cluster', 'label'
    ]

    df = pd.DataFrame(data, columns=columns)
    return df

if __name__ == "__main__":
    df = generate_behavioral_data()
    df.to_csv("behavior_data.csv", index=False)
    print("Synthetic dataset saved as behavior_data.csv")
