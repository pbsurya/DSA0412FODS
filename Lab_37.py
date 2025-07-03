import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = pd.DataFrame({
    'StudyHours': [1, 2, 3, 4, 5, 6, 7],
    'Score': [50, 55, 65, 70, 75, 80, 85]
})

# Correlation
correlation = data.corr()
print("Correlation Matrix:\n", correlation)

# Plot
sns.regplot(x='StudyHours', y='Score', data=data)
plt.title("Study Hours vs Exam Score")
plt.show()
