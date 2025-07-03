import numpy as np
from scipy import stats

np.random.seed(42)
conversion_a = np.random.rand(100) < 0.12  # Group A
conversion_b = np.random.rand(100) < 0.17  # Group B

# T-test
t_stat, p_value = stats.ttest_ind(conversion_a, conversion_b)

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Result: Statistically significant difference.")
else:
    print("Result: No significant difference.")
