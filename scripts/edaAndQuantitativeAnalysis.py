import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import talib
import pynance as pn
import numpy as np

def validate_columns(data, required_columns):
    """Ensure the data contains the required columns."""
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        raise ValueError(f"The following required columns are missing: {', '.join(missing_columns)}")
    else:
        print("All required columns are present.")


# Function to handle missing values
def handle_missing_values(data):
    data = data.ffill()  
    return data

# Function to analyze statistical properties
def analyze_statistics(data, columns):
    print(data[columns].describe())

# Function to visualize distributions
def plot_distributions(data, column, bins=50, title="Distribution"):
    plt.figure(figsize=(10, 6))
    data[column].hist(bins=bins)
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

# Function to compute and visualize correlations
def analyze_correlations(data, columns):
    correlation_matrix = data[columns].corr()
    print("\nCorrelation Matrix:")
    print(correlation_matrix)
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()

# Function to study volatility
def plot_volatility(data, value_col, date_col, window=20):
    data['Rolling_Std'] = data[value_col].rolling(window=window).std()
    plt.figure(figsize=(12, 6))
    plt.plot(data[date_col], data['Rolling_Std'], label=f"Rolling Std Dev ({window} days)", color='purple')
    plt.title("Volatility Over Time")
    plt.xlabel("Date")
    plt.ylabel("Rolling Std Dev")
    plt.legend()
    plt.show()
    
    


#Quantitative Analysis

# Function to calculate technical indicators
def calculate_indicators(data):
    """Calculate SMA, RSI, and MACD using TA-Lib."""
    data['SMA_20'] = talib.SMA(data['Close'], timeperiod=20)  # 20-day SMA
    data['RSI'] = talib.RSI(data['Close'], timeperiod=14)  # 14-day RSI
    data['MACD'], data['MACD_signal'], data['MACD_hist'] = talib.MACD(
        data['Close'], fastperiod=12, slowperiod=26, signalperiod=9
    )
    return data

# Function to calculate financial metrics using PyNance
def calculate_financial_metrics(data):
    """Calculate financial metrics like daily returns and cumulative returns."""
    def calculate_daily_returns(close_prices):
        """Helper to calculate daily logarithmic returns."""
        return np.log(close_prices / close_prices.shift(1))

    def calculate_cumulative_returns(daily_returns):
        """Helper to calculate cumulative returns."""
        return (1 + daily_returns).cumprod()

    data['Daily_Return'] = calculate_daily_returns(data['Close'])
    data['Cumulative_Return'] = calculate_cumulative_returns(data['Daily_Return'])
    return data

# Function to visualize stock prices and SMA
def plot_stock_and_sma(data):
    """Plot stock prices and SMA."""
    plt.figure(figsize=(14, 7))
    plt.plot(data['Date'], data['Close'], label='Close Price', alpha=0.7)
    plt.plot(data['Date'], data['SMA_20'], label='SMA_20', linestyle='--', alpha=0.9)
    plt.title('Stock Prices with SMA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()

# Function to visualize RSI
def plot_rsi(data):
    """Plot RSI with overbought and oversold levels."""
    plt.figure(figsize=(14, 5))
    plt.plot(data['Date'], data['RSI'], label='RSI', color='orange')
    plt.axhline(y=70, color='r', linestyle='--', label='Overbought')
    plt.axhline(y=30, color='g', linestyle='--', label='Oversold')
    plt.title('Relative Strength Index (RSI)')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()
    plt.grid()
    plt.show()

# Function to visualize MACD
def plot_macd(data):
    """Plot MACD, Signal Line, and MACD Histogram."""
    plt.figure(figsize=(14, 7))
    plt.plot(data['Date'], data['MACD'], label='MACD', color='blue')
    plt.plot(data['Date'], data['MACD_signal'], label='Signal Line', color='red', linestyle='--')
    plt.bar(data['Date'], data['MACD_hist'], label='MACD Histogram', alpha=0.3)
    plt.title('MACD Indicator')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid()
    plt.show()

# Function to visualize financial metrics
def plot_financial_metrics(data):
    """Plot daily returns and cumulative returns."""
    plt.figure(figsize=(14, 7))
    plt.plot(data['Date'], data['Cumulative_Return'], label='Cumulative Return', color='green')
    plt.title('Cumulative Return')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.legend()
    plt.grid()
    plt.show()

    plt.figure(figsize=(14, 7))
    plt.plot(data['Date'], data['Daily_Return'], label='Daily Return', color='purple')
    plt.title('Daily Return')
    plt.xlabel('Date')
    plt.ylabel('Daily Return')
    plt.legend()
    plt.grid()
    plt.show()
