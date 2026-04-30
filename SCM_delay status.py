import pandas as pd

# 1. SQL Load
df = pd.read_csv('scm_mart.csv')

# 2. Categorizing delay
def check_status(delay):
    if delay > 0: return 'Late'
    elif delay == 0: return 'On-time'
    else: return 'Early'

df['Delivery_Status'] = df['Delay_Days'].apply(check_status)

# 3. Delays over 2 days 
df['High_Priority'] = (df['Profit'] > df['Profit'].median()) & (df['Delay_Days'] >= 2)

# 4. Result
df.to_csv('final_delivery_data.csv', index=False)
print("✅: 'final_delivery_data.csv' created")
