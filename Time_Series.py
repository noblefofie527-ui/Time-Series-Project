import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Generating Random Time Series Data
np.random.seed(82)
time_steps = 730
timeline = pd.date_range(start='2024-03-15', periods=time_steps, freq='D')

# Combining and Structuring
base_line = np.linspace(50, 150, time_steps)
weekly_cycle = 20 * np.sin(2 * np.pi * timeline.dayofweek / 7)
noise = np.random.normal(0, 10, time_steps)
values = base_line + weekly_cycle + noise
 
df = pd.DataFrame({'Date': timeline, 'Sales': values})
df.set_index('Date', inplace=True)

# Visualisation: Plotting Patterns
plt.figure(figsize=(12, 5))
plt.plot(df['Sales'], label='Daily Sales', color='skyblue')
plt.title('Time Series Data Visualisation')
plt.xlabel('Date')
plt.ylabel('Sales Units')
plt.legend()
plt.show()

# Moving Average Smoothing
# Using a 7-day window
df['weekly_avg'] = df['Sales'].rolling(window=7, center=True).mean()

plt.figure(figsize=(12, 5))
plt.plot(df['Sales'], alpha=0.3, label='Actual Sales')
plt.plot(df['weekly_avg'], color='red', linewidth=2, label='7-Day Moving Average')
plt.title('Moving Average Smoothing')
plt.legend()
plt.show()

# Seasonal Decomposition
# We specify period=7 because the data is weekly and we expect weekly cycles
decomposition = seasonal_decompose(df['Sales'], model='additive', period=7)

# Plotting the decomposition components
fig = decomposition.plot()
fig.set_size_inches(12, 8)
plt.suptitle('Time Series Decomposition')
plt.show()

print("Analysis Complete: Data generated, smoothed, and decomposed!")