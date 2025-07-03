import pandas as pd
import numpy as np
from scipy import stats

# Load data from CSV
data = pd.read_csv('rare_elements.csv')
concentrations = data.iloc[:, 0].dropna().values  # assuming 1 column of measurements

# User inputs
sample_size = int(input("Enter sample size: "))
confidence_level = float(input("Enter confidence level (e.g., 0.95): "))
precision = float(input("Enter desired precision (± value): "))

# Random sampling
np.random.seed(42)  # for reproducibility
sample = np.random.choice(concentrations, size=sample_size, replace=False)

# Point estimate: sample mean
sample_mean = np.mean(sample)

# Standard error
std_error = stats.sem(sample)

# t-score for given confidence level
df = sample_size - 1
t_score = stats.t.ppf((1 + confidence_level) / 2, df)

# Margin of error
margin_error = t_score * std_error

# Confidence interval
lower_bound = sample_mean - margin_error
upper_bound = sample_mean + margin_error

# Output
print(f"\nSample Mean (Point Estimate): {sample_mean:.4f}")
print(f"Confidence Interval ({int(confidence_level*100)}%): ({lower_bound:.4f}, {upper_bound:.4f})")

# Precision check
if margin_error <= precision:
    print("✅ Desired level of precision achieved.")
else:
    print("❌ Desired precision not achieved. Consider increasing sample size.")
