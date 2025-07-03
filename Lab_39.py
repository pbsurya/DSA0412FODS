import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample transaction data
data = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4, 5],
    'AmountSpent': [300, 700, 200, 600, 1000],
    'ItemsPurchased': [3, 7, 2, 6, 10]
})

X = data[['AmountSpent', 'ItemsPurchased']]
kmeans = KMeans(n_clusters=2)
data['Cluster'] = kmeans.fit_predict(X)

plt.scatter(data['AmountSpent'], data['ItemsPurchased'], c=data['Cluster'], cmap='Set2')
plt.xlabel("Amount Spent")
plt.ylabel("Items Purchased")
plt.title("Customer Clustering")
plt.show()
