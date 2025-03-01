import pandas as pd
from sklearn.ensemble import IsolationForest
import json

# Load sample log data (modify the path as needed)
# Assume logs are in CSV with columns: timestamp, event_type, source, dest, value
logs = pd.read_csv("wazuh_logs.csv")

# For demonstration, use numeric feature(s)
# Let's assume 'value' is a numeric representation of some metric
X = logs[['value']]

# Train Isolation Forest for anomaly detection
model = IsolationForest(contamination=0.05, random_state=42)
logs['anomaly'] = model.fit_predict(X)

# Filter out anomalies (where anomaly == -1)
anomalies = logs[logs['anomaly'] == -1]

# Save anomalies as JSON for reporting or further processing
anomalies.to_json("anomaly_report.json", orient="records", lines=True)

print("Anomaly detection complete. Check anomaly_report.json for details.")
