import numpy as np

# Example 3x3 matrix: each row = product, each column = price in a sale
sales_data = np.array([
    [100, 150, 200],
    [80, 120, 160],
    [90, 110, 130]
])

# Calculate average price
average_price = np.mean(sales_data)

print("Average Price:", average_price)
