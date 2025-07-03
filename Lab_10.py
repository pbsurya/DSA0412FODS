import matplotlib.pyplot as plt

# Sample monthly sales data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [15000, 18000, 17000, 21000, 19000, 22000]

# 1. Line Plot of Monthly Sales
plt.figure(figsize=(8, 4))
plt.plot(months, sales, marker='o', linestyle='-', color='blue')
plt.title('Monthly Sales (Line Plot)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Bar Plot of Monthly Sales
plt.figure(figsize=(8, 4))
plt.bar(months, sales, color='green')
plt.title('Monthly Sales (Bar Plot)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()
