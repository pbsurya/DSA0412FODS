import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.preprocessing import LabelEncoder

# 🔹 Sample car dataset
data = pd.DataFrame({
    'mileage': [12000, 30000, 15000, 40000, 18000, 22000, 35000],
    'age': [2, 5, 3, 6, 4, 3, 5],
    'brand': ['Toyota', 'BMW', 'Honda', 'BMW', 'Honda', 'Toyota', 'BMW'],
    'engine': ['Petrol', 'Diesel', 'Petrol', 'Diesel', 'Petrol', 'Diesel', 'Petrol'],
    'price': [600000, 850000, 650000, 800000, 670000, 620000, 790000]
})

# 🔹 Encode categorical columns
le_brand = LabelEncoder()
le_engine = LabelEncoder()
data['brand_encoded'] = le_brand.fit_transform(data['brand'])
data['engine_encoded'] = le_engine.fit_transform(data['engine'])

# 🔹 Features and target
X = data[['mileage', 'age', 'brand_encoded', 'engine_encoded']]
y = data['price']

# 🔹 Train CART model
model = DecisionTreeRegressor(random_state=42)
model.fit(X, y)

# 🔹 Get user input
print("Enter new car details:")
mileage = float(input("Mileage (in km): "))
age = int(input("Age (in years): "))
brand = input(f"Brand {list(le_brand.classes_)}: ")
engine = input(f"Engine type {list(le_engine.classes_)}: ")

# 🔹 Encode input
brand_enc = le_brand.transform([brand])[0]
engine_enc = le_engine.transform([engine])[0]

# 🔹 Predict
new_car = np.array([[mileage, age, brand_enc, engine_enc]])
predicted_price = model.predict(new_car)[0]

# 🔹 Display result
print(f"\nPredicted Price: ₹{predicted_price:.2f}")

# 🔹 Display decision path
print("\nDecision Path (Tree Logic):")
tree_rules = export_text(model, feature_names=['mileage', 'age', 'brand_encoded', 'engine_encoded'])
print(tree_rules)

