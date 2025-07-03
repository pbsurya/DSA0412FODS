import pandas as pd

# Sample temperature data
data = pd.DataFrame({
    'City': ['CityA']*5 + ['CityB']*5,
    'Temperature': [30, 32, 29, 31, 30, 20, 21, 19, 22, 20]
})

stats = data.groupby('City')['Temperature'].agg(['mean', 'std', 'min', 'max'])
stats['Range'] = stats['max'] - stats['min']

print("Temperature Stats:\n", stats)
print("City with Highest Range:", stats['Range'].idxmax())
print("Most Consistent City:", stats['std'].idxmin())
