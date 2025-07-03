import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Data for 18 individuals
age = [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 56, 57, 58, 58, 60, 61, 61]
fat = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]

# Create DataFrame
df = pd.DataFrame({'Age': age, 'Fat': fat})

# Calculate statistics
print("Statistics for Age:")
print("Mean:", df['Age'].mean())
print("Median:", df['Age'].median())
print("Standard Deviation:", df['Age'].std())

print("\nStatistics for %Fat:")
print("Mean:", df['Fat'].mean())
print("Median:", df['Fat'].median())
print("Standard Deviation:", df['Fat'].std())

# Plot boxplots
plt.figure(figsize=(14, 10))

plt.subplot(2, 2, 1)
sns.boxplot(data=df[['Age', 'Fat']])
plt.title("Boxplots for Age and %Fat")

# Scatter plot
plt.subplot(2, 2, 2)
sns.scatterplot(x='Age', y='Fat', data=df)
plt.title("Scatter Plot: Age vs %Fat")

# Q-Q Plot for Age
plt.subplot(2, 2, 3)
stats.probplot(df['Age'], dist="norm", plot=plt)
plt.title("Q-Q Plot for Age")

# Q-Q Plot for %Fat
plt.subplot(2, 2, 4)
stats.probplot(df['Fat'], dist="norm", plot=plt)
plt.title("Q-Q Plot for %Fat")

plt.tight_layout()
plt.show()
