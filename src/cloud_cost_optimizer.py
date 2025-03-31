import boto3
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.linear_model import LinearRegression

# Placeholder for AWS cost analysis function
def analyze_costs():
    client = boto3.client('ce', region_name='us-east-1')
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': '2024-01-01',
            'End': '2024-01-31'
        },
        Granularity='DAILY',
        Metrics=['BlendedCost']
    )
    data = response['ResultsByTime']
    costs = []
    for item in data:
        costs.append({
            'date': item['TimePeriod']['Start'],
            'cost': float(item['Total']['BlendedCost']['Amount'])
        })
    df = pd.DataFrame(costs)
    return df

def forecast_costs(df):
    df['date'] = pd.to_datetime(df['date'])
    df['day_of_year'] = df['date'].dt.dayofyear

    model = LinearRegression()
    model.fit(df[['day_of_year']], df['cost'])
    
    future_days = np.array([df['day_of_year'].max() + i for i in range(1, 31)]).reshape(-1, 1)
    predictions = model.predict(future_days)
    
    return predictions

if __name__ == "__main__":
    df = analyze_costs()
    print("Historical costs:\n", df)
    
    forecast = forecast_costs(df)
    print("Cost Forecast for next 30 days:\n", forecast)
