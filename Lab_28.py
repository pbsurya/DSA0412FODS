import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Sample customer dataset (you can load real data from CSV)
data = pd.DataFrame({
    'annual_spending': [5000, 15000, 7000, 20000, 3000, 10000, 18000, 4000],
    'visits_per_month': [3, 10, 5, 12, 2, 6, 11, 3]
})

# Feature Scaling
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# KMeans clustering
k = 3  # Number of customer segments
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(scaled_data)

# Get user input
print("Enter new customer details:")
spending = float(input("Annual spending (in ₹): "))
visits = int(input("Average visits per month: "))

# Prepare and scale the new data point
new_customer = np.array([[spending, visits]])
new_customer_scaled = scaler.transform(new_customer)

# Predict segment
segment = kmeans.predict(new_customer_scaled)[0]

# Output
print(f"\nThe new customer belongs to Segment: {segment}")
