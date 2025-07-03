import numpy as np
from scipy import stats

np.random.seed(42)
drug_group = np.random.normal(loc=8, scale=2, size=50)
placebo_group = np.random.normal(loc=5, scale=2, size=50)

# Confidence Intervals
ci_drug = stats.t.interval(0.95, len(drug_group)-1, loc=np.mean(drug_group), scale=stats.sem(drug_group))
ci_placebo = stats.t.interval(0.95, len(placebo_group)-1, loc=np.mean(placebo_group), scale=stats.sem(placebo_group))

print("95% CI for Drug Group:", ci_drug)
print("95% CI for Placebo Group:", ci_placebo)
