import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [150, 200, 250, 300, 280, 320]

# Line Plot
plt.plot(months, sales, marker='o')
plt.title("Line Plot - Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Scatter Plot
plt.scatter(months, sales, color='orange')
plt.title("Scatter Plot - Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Bar Plot
plt.bar(months, sales, color='skyblue')
plt.title("Bar Plot - Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
