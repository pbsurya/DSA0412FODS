from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Load Iris dataset
iris = load_iris()
X = iris.data  # features
y = iris.target  # labels (0, 1, 2)

# Train a Decision Tree Classifier
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# User input
print("Enter flower measurements:")
sepal_length = float(input("Sepal length (cm): "))
sepal_width = float(input("Sepal width (cm): "))
petal_length = float(input("Petal length (cm): "))
petal_width = float(input("Petal width (cm): "))

# Make prediction
sample = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(sample)

# Map prediction to species name
species = iris.target_names[prediction[0]]
print(f"\nPredicted Iris species: {species.capitalize()}")
