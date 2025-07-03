import pandas as pd
import numpy as np
from scipy import stats

# Load the CSV file
data = pd.read_csv("customer_reviews.csv")

# Assume the ratings column is named 'rating'
ratings = data['rating'].dropna().values  # Ensure no NaN values

# Point Estimate: Mean rating
mean_rating = np.mean(ratings)

# Sample size and degrees of freedom
n = len(ratings)
df = n - 1

# Standard error
std_error = stats.sem(ratings)

# Confidence level input
confidence_level = float(input("Enter confidence level (e.g., 0.95): "))
t_score = stats.t.ppf((1 + confidence_level) / 2, df)

# Margin of error and confidence interval
margin_error = t_score * std_error
lower_bound = mean_rating - margin_error
upper_bound = mean_rating + margin_error

# Output
print(f"\nAverage Customer Rating: {mean_rating:.2f}")
print(f"{int(confidence_level*100)}% Confidence Interval: ({lower_bound:.2f}, {upper_bound:.2f})")

# Optional: Basic satisfaction level interpretation
if mean_rating >= 4.0:
    print("Customer Satisfaction: High ✅")
elif mean_rating >= 3.0:
    print("Customer Satisfaction: Moderate ⚠️")
else:
    print("Customer Satisfaction: Low ❌")
