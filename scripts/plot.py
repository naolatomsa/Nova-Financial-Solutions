import matplotlib.pyplot as plt

def plot_stock_price(data, title='Stock Price with Indicators'):

    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Close Price', color='blue')
    if 'SMA_20' in data:
        plt.plot(data['SMA_20'], label='20-Day SMA', color='orange')
    if 'EMA_20' in data:
        plt.plot(data['EMA_20'], label='20-Day EMA', color='green')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def plot_rsi(data, title='Relative Strength Index (RSI)'):

    plt.figure(figsize=(12, 6))
    plt.plot(data['RSI'], label='RSI', color='purple')
    plt.axhline(70, color='red', linestyle='--', label='Overbought')
    plt.axhline(30, color='green', linestyle='--', label='Oversold')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()
    plt.show()

def plot_macd(data, title='MACD (Moving Average Convergence Divergence)'):

    plt.figure(figsize=(12, 6))
    plt.plot(data['MACD'], label='MACD', color='blue')
    plt.plot(data['Signal'], label='Signal Line', color='red')
    plt.bar(data.index, data['Hist'], label='Histogram', color='grey', alpha=0.5)
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.show()
