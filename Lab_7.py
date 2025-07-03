import pandas as pd

# Sample DataFrame
order_data = pd.DataFrame({
    'customer_id': [101, 102, 101, 103, 102, 101],
    'order_date': ['2025-06-01', '2025-06-02', '2025-06-05', '2025-06-03', '2025-06-07', '2025-06-09'],
    'product_name': ['Laptop', 'Mouse', 'Laptop', 'Keyboard', 'Mouse', 'Keyboard'],
    'order_quantity': [1, 2, 1, 1, 3, 2]
})

# Ensure order_date is datetime
order_data['order_date'] = pd.to_datetime(order_data['order_date'])

# 1. Total number of orders made by each customer
orders_per_customer = order_data['customer_id'].value_counts()

# 2. Average order quantity for each product
avg_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()

# 3. Earliest and latest order dates
earliest_date = order_data['order_date'].min()
latest_date = order_data['order_date'].max()

# Output
print("Total Orders by Each Customer:\n", orders_per_customer)
print("\nAverage Order Quantity per Product:\n", avg_quantity_per_product)
print("\nEarliest Order Date:", earliest_date)
print("Latest Order Date:", latest_date)
