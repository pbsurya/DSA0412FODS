import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# 🔹 Sample dataset (you can replace this with your CSV)
data = pd.DataFrame({
    'fever': [98.6, 101.1, 100.5, 99.0, 102.2, 98.7, 100.1],
    'cough': [0, 1, 1, 0, 1, 0, 1],
    'fatigue': [0, 1, 1, 0, 1, 0, 1],
    'condition': [0, 1, 1, 0, 1, 0, 1]
})

# 🔹 Split features and labels
X = data[['fever', 'cough', 'fatigue']]
y = data['condition']

# 🔹 Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 🔹 Train KNN model
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# 🔹 User input
fever_input = float(input("Enter patient fever (°F): "))
cough_input = int(input("Cough present? (0 = No, 1 = Yes): "))
fatigue_input = int(input("Fatigue present? (0 = No, 1 = Yes): "))
k = int(input("Enter the value of k (number of neighbors): "))

# 🔹 Prepare user input for prediction
new_patient = [[fever_input, cough_input, fatigue_input]]
new_patient_scaled = scaler.transform(new_patient)

# 🔹 Fit KNN model and predict
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)
prediction = knn.predict(new_patient_scaled)

# 🔹 Output
print("\nPrediction:")
print("Patient has the condition ✅" if prediction[0] == 1 else "Patient does NOT have the condition ❌")
