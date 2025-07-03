import pandas as pd

# Sample property data
property_data = pd.DataFrame({
    'property_id': [1, 2, 3, 4, 5],
    'location': ['Chennai', 'Delhi', 'Chennai', 'Mumbai', 'Delhi'],
    'bedrooms': [3, 5, 2, 4, 6],
    'area_sqft': [1200, 2000, 950, 1800, 2200],
    'listing_price': [5000000, 8000000, 4500000, 7500000, 9000000]
})

# 1. Average listing price by location
avg_price_by_location = property_data.groupby('location')['listing_price'].mean()

# 2. Number of properties with more than four bedrooms
properties_over_4_bedrooms = property_data[property_data['bedrooms'] > 4].shape[0]

# 3. Property with the largest area
largest_area_property = property_data.loc[property_data['area_sqft'].idxmax()]

# Output
print("1. Average Listing Price by Location:\n", avg_price_by_location)
print("\n2. Number of Properties with More Than 4 Bedrooms:", properties_over_4_bedrooms)
print("\n3. Property with the Largest Area:\n", largest_area_property)
