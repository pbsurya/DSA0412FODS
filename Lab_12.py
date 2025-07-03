import matplotlib.pyplot as plt

temperature = [30, 32, 35, 36, 38, 34, 33, 31, 29, 28, 27, 26]
rainfall = [5, 6, 7, 10, 15, 20, 18, 10, 6, 3, 2, 1]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Line Plot for Temperature
plt.plot(months, temperature, marker='o', color='red')
plt.title("Line Plot - Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.show()

# Scatter Plot for Rainfall
plt.scatter(months, rainfall, color='blue')
plt.title("Scatter Plot - Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.show()
