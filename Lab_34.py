import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

# Sample medical dataset
data = pd.DataFrame({
    'Age': [30, 40, 50, 60, 70, 45],
    'BP': [120, 140, 130, 150, 160, 135],
    'Cholesterol': [200, 220, 250, 270, 300, 210],
    'Outcome': ['Good', 'Bad', 'Good', 'Bad', 'Bad', 'Good']
})

X = data[['Age', 'BP', 'Cholesterol']]
y = data['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))
