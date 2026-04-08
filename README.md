# Time Series Analysis Project
This project demonstrates an intermediate-level analysis of time-series data using Python.

## Features
* **Data Generation:** Generates dataset starting from March 2024, simulating 730 days (2 years) of business operations.
* **Rolling Window Smoothing:** Implements a 7-day centered moving average to filter our daily fluctuations and reveal the underlying weekly momentum.
* **Decomposition:** Breaks the signal into Trend, Seasonal (Weekly), and Residual components using statsmodels.

## Tools Used
* Pandas for time-indexing and rolling window calculations.
* Matplotlib for multi-layer data visualisation.
* Statsmodels for advanced seasonal decomposition. 
* NumPy for generating periodic signals and normal distributions.
