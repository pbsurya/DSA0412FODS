import numpy as np

# Example quarterly sales data: [Q1, Q2, Q3, Q4]
sales_data = np.array([10000, 12000, 15000, 18000])

# Total sales for the year
total_sales = np.sum(sales_data)

# Percentage increase from Q1 to Q4
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print("Total Sales:", total_sales)
print("Percentage Increase from Q1 to Q4:", percentage_increase, "%")
