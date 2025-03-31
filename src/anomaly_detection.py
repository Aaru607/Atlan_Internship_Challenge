from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(cost_data):
    model = IsolationForest(contamination=0.1)
    anomalies = model.fit_predict(cost_data[['AmortizedCost']])
    
    cost_data['Anomaly'] = anomalies
    return cost_data[cost_data['Anomaly'] == -1]

if __name__ == '__main__':
    # Assume `cost_data` is a DataFrame loaded from `get_cost_data` function
    cost_data = pd.read_csv('cost_data.csv')  # Replace with actual data source
    anomalies = detect_anomalies(cost_data)
    print(anomalies)
