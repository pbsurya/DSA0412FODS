import numpy as np

# Example fuel efficiency data (in mpg) for different car models
fuel_efficiency = np.array([25, 30, 35, 28, 32])

# Calculate average fuel efficiency
average_efficiency = np.mean(fuel_efficiency)

# Choose two car models (e.g., model A at index 0 and model B at index 2)
model_a = fuel_efficiency[0]
model_b = fuel_efficiency[2]

# Calculate percentage improvement from model A to model B
percentage_improvement = ((model_b - model_a) / model_a) * 100

print("Average Fuel Efficiency:", average_efficiency, "mpg")
print("Percentage Improvement from Model A to B:", percentage_improvement, "%")
