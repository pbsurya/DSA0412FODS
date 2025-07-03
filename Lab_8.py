import pandas as pd

# Sample sales data
sales_data = pd.DataFrame({
    'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Mouse', 'Laptop', 'Keyboard', 'Mouse', 'Monitor'],
    'quantity_sold': [2, 5, 3, 4, 2, 3, 1, 2, 6]
})

# Group by product and sum the quantity sold
total_sales = sales_data.groupby('product_name')['quantity_sold'].sum()

# Sort in descending order and get top 5
top_5_products = total_sales.sort_values(ascending=False).head(5)

# Output
print("Top 5 Most Sold Products:\n", top_5_products)
