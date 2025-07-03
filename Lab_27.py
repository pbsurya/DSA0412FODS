import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Sample dataset: usage_minutes, contract_months, support_calls, churn (0 = No, 1 = Yes)
data = pd.DataFrame({
    'usage_minutes': [300, 450, 200, 150, 500, 380, 120, 600],
    'contract_months': [12, 24, 6, 3, 18, 12, 2, 36],
    'support_calls': [1, 0, 3, 4, 0, 1, 5, 0],
    'churn': [0, 0, 1, 1, 0, 0, 1, 0]
})

# Split features and target
X = data[['usage_minutes', 'contract_months', 'support_calls']]
y = data['churn']

# Train-test split and model training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

# Get user input
print("Enter new customer details:")
usage = float(input("Usage minutes per month: "))
contract = int(input("Contract duration (in months): "))
calls = int(input("Number of customer support calls: "))

# Predict
new_customer = [[usage, contract, calls]]
prediction = model.predict(new_customer)

# Output
print("\nPrediction:")
if prediction[0] == 1:
    print("⚠️  Customer is likely to churn (leave the company)")
else:
    print("✅ Customer is likely to stay")
