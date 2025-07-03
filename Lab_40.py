import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
data = pd.DataFrame({
    'Name': ['Player1', 'Player2', 'Player3', 'Player4', 'Player5'],
    'Age': [24, 30, 28, 33, 25],
    'Position': ['Midfielder', 'Forward', 'Defender', 'Goalkeeper', 'Forward'],
    'Goals': [10, 20, 5, 1, 17],
    'Salary': [50000, 70000, 45000, 40000, 65000]
})

# Save to CSV and read
data.to_csv('soccer_data.csv', index=False)
df = pd.read_csv('soccer_data.csv')

# Analysis
print("Top 5 Goal Scorers:\n", df.sort_values('Goals', ascending=False).head(5))
print("Top 5 Salaries:\n", df.sort_values('Salary', ascending=False).head(5))

avg_age = df['Age'].mean()
print("Average Age:", avg_age)
print("Players above average age:\n", df[df['Age'] > avg_age][['Name', 'Age']])

# Bar plot for position distribution
df['Position'].value_counts().plot(kind='bar', title='Player Positions')
plt.xlabel("Position")
plt.ylabel("Count")
plt.show()
