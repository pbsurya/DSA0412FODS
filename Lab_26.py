import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Sample dataset (area in sqft, bedrooms, location_encoded, price in lakhs)
# Location encoded: 0 = Rural, 1 = Suburban, 2 = Urban
data = pd.DataFrame({
    'area': [1000, 1500, 1200, 1300, 2000, 1800, 1100],
    'bedrooms': [2, 3, 2, 3, 4, 3, 2],
    'location': [0, 1, 1, 2, 2, 2, 0],
    'price': [30, 45, 36, 50, 70, 65, 32]
})

# Features and label
X = data[['area', 'bedrooms', 'location']]
y = data['price']

# Train linear regression model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Get user input
print("Enter the features of the new house:")
area = float(input("Area (in square feet): "))
bedrooms = int(input("Number of bedrooms: "))
print("Location Types:\n0 = Rural\n1 = Suburban\n2 = Urban")
location = int(input("Enter location code (0/1/2): "))

# Predict
new_house = [[area, bedrooms, location]]
predicted_price = model.predict(new_house)

print(f"\nPredicted House Price: ₹{predicted_price[0]:.2f} lakhs")
