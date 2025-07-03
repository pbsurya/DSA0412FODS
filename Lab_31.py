import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Sample customer data
data = pd.DataFrame({
    'Age': [25, 45, 35, 33, 50, 23, 52, 40],
    'Annual Income': [50000, 100000, 75000, 62000, 115000, 43000, 105000, 70000],
    'Spending Score': [60, 40, 70, 50, 30, 80, 20, 55]
})

# Standardize data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Apply KMeans
kmeans = KMeans(n_clusters=3, random_state=0)
data['Cluster'] = kmeans.fit_predict(scaled_data)

# Plotting clusters
plt.scatter(data['Annual Income'], data['Spending Score'], c=data['Cluster'], cmap='viridis')
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()
