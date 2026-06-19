import pandas as pd

# Read customer data
df = pd.read_csv("customer_data.csv")

# Calculate churn rate
churn_rate = (df["Churn"] == "Yes").mean() * 100

print("Customer Retention & Churn Analysis")
print("-----------------------------------")
print(df)

print("\nTotal Customers:", len(df))
print("Churn Rate: {:.2f}%".format(churn_rate))
