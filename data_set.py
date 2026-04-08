import pandas as pd
import numpy as np

n = 1000

df = pd.DataFrame({
    "date": pd.date_range(start="2025-01-01", periods=n, freq="h"),
    "agent_id": np.random.randint(1, 20, n),
    "calls_handled": np.random.randint(5, 30, n),
    "avg_handle_time": np.random.randint(200, 600, n),
    "resolution_time": np.random.randint(300, 900, n),
    "satisfaction_score": np.random.uniform(3.0, 5.0, n),
    "resolved": np.random.choice([0,1], n),
    "queue": np.random.choice(["Billing","Tech","General"], n),
    "shift": np.random.choice(["Morning","Evening","Night"], n)
})

df.to_csv("call_center_data.csv", index=False)