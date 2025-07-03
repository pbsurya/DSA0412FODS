import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

# Sample clinical trial data
# Replace with real data if available
control_group = np.array([5.1, 5.3, 5.0, 4.9, 5.2, 5.1, 5.0])
treatment_group = np.array([6.2, 6.4, 6.5, 6.1, 6.3, 6.6, 6.2])

# Hypothesis Testing: Independent t-test
t_stat, p_value = ttest_ind(treatment_group, control_group)

# Print result
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_value:.4f}")

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("✅ Result: Statistically significant difference (reject H0)")
else:
    print("❌ Result: No significant difference (fail to reject H0)")

# Visualization
data = [control_group, treatment_group]
labels = ['Control (Placebo)', 'Treatment (Drug)']

plt.figure(figsize=(8, 5))
plt.boxplot(data, labels=labels)
plt.title('Clinical Trial Results')
plt.ylabel('Response Value')
plt.text(1.5, max(max(control_group), max(treatment_group)) + 0.1, f'p = {p_value:.4f}', 
         ha='center', fontsize=12, color='red')
plt.grid(True)
plt.tight_layout()
plt.show()
