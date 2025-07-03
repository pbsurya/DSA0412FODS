import pandas as pd
import matplotlib.pyplot as plt

# Simulated stock data
data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Close': [100, 102, 101, 105, 110, 108, 107, 111, 115, 117]
})

# Variability calculation
std_dev = data['Close'].std()
print("Standard Deviation of Closing Prices:", std_dev)

# Plot
data.set_index('Date')['Close'].plot(title="Stock Price Variability")
plt.ylabel("Closing Price")
plt.show()
