import boto3

def monitor_budget(budget_name, budget_threshold):
    client = boto3.client('budgets', region_name='us-east-1')
    
    response = client.describe_budgets(AccountId='your_account_id')
    
    for budget in response['Budgets']:
        if budget['BudgetName'] == budget_name:
            cost_spent = budget['CalculatedSpend']['ActualSpend']['Amount']
            if float(cost_spent) > budget_threshold:
                print(f"Budget exceeded: {cost_spent} > {budget_threshold}")
                # Trigger alert (e.g., email or message)
            else:
                print("Within Budget")

if __name__ == '__main__':
    monitor_budget('monthly-cost-budget', 1000)
