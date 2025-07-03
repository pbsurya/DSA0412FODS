import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Sample car data
data = pd.DataFrame({
    'Engine Size': [1.6, 2.0, 2.4, 3.0, 3.5],
    'Horsepower': [130, 165, 190, 220, 250],
    'Price': [20000, 25000, 27000, 30000, 35000]
})

X = data[['Engine Size', 'Horsepower']]
y = data['Price']

model = LinearRegression()
model.fit(X, y)
predictions = model.predict(X)

print("R2 Score:", r2_score(y, predictions))
