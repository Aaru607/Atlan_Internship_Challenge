import boto3
import pandas as pd

def get_cost_data(start_date, end_date):
    client = boto3.client('ce', region_name='us-east-1')
    
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': start_date,
            'End': end_date
        },
        Granularity='MONTHLY',
        Metrics=['AmortizedCost'],
    )
    
    cost_data = response['ResultsByTime']
    cost_df = pd.DataFrame(cost_data)
    
    return cost_df

if __name__ == '__main__':
    start_date = '2023-01-01'
    end_date = '2023-02-01'
    
    data = get_cost_data(start_date, end_date)
    print(data)
