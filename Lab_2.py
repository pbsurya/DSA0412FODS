import numpy as np

# Example dummy data: [Bedrooms, Square Footage, Sale Price]
house_data = np.array([
    [3, 1500, 250000],
    [5, 2200, 450000],
    [4, 1800, 300000],
    [6, 3000, 600000],
    [2, 1200, 200000]
])

# Filter rows where number of bedrooms > 4
filtered_data = house_data[house_data[:, 0] > 4]

# Extract sale prices from filtered rows (column index 2)
sale_prices = filtered_data[:, 2]

# Calculate the average sale price
average_price = np.mean(sale_prices)

# Print result
print("Average sale price of houses with more than 4 bedrooms:", average_price)
