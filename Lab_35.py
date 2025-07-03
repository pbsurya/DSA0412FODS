import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Sample transaction data
data = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4, 5],
    'TotalSpent': [200, 500, 700, 300, 600],
    'Frequency': [5, 8, 6, 4, 9]
})

X = data[['TotalSpent', 'Frequency']]
kmeans = KMeans(n_clusters=2)
data['Cluster'] = kmeans.fit_predict(X)

# Visualization
sns.scatterplot(x='TotalSpent', y='Frequency', hue='Cluster', data=data)
plt.title("Customer Segmentation Based on Spending")
plt.show()
