import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import seaborn as sns

# Sample house data
data = pd.DataFrame({
    'Size': [1000, 1500, 1800, 2400, 3000],
    'Price': [200000, 250000, 300000, 360000, 400000]
})

X = data[['Size']]
y = data['Price']

model = LinearRegression()
model.fit(X, y)
predictions = model.predict(X)

print("R2 Score:", r2_score(y, predictions))

# Plot
sns.regplot(x='Size', y='Price', data=data)
plt.title("Linear Regression: House Size vs Price")
plt.show()
