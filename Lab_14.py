from collections import Counter

customer_ages = [23, 25, 23, 30, 31, 30, 25, 27, 30, 29, 40, 31, 23, 27, 25]
age_freq = Counter(customer_ages)

print("Customer Age Frequency:", age_freq)
