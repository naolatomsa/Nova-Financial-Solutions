import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to handle missing values
def handle_missing_values(data):
    data = data.ffill()  
    return data

# Function to analyze statistical properties
def analyze_statistics(data, columns):
    """Display descriptive statistics for specific columns."""
    # print("\nDescriptive Statistics:")
    print(data[columns].describe())

# Function to visualize distributions
def plot_distributions(data, column, bins=50, title="Distribution"):
    """Plot the distribution of a specific column."""
    plt.figure(figsize=(10, 6))
    data[column].hist(bins=bins)
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

# Function to compute and visualize correlations
def analyze_correlations(data, columns):
    """Analyze and visualize correlations between columns."""
    correlation_matrix = data[columns].corr()
    print("\nCorrelation Matrix:")
    print(correlation_matrix)
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()

# Function to study volatility
def plot_volatility(data, value_col, date_col, window=20):
    """Plot rolling standard deviation (volatility). Volatility refers to the amount of variation or fluctuation in the stock prices over a certain period. It helps understand the risk or stability of a stock."""
    data['Rolling_Std'] = data[value_col].rolling(window=window).std()
    plt.figure(figsize=(12, 6))
    plt.plot(data[date_col], data['Rolling_Std'], label=f"Rolling Std Dev ({window} days)", color='purple')
    plt.title("Volatility Over Time")
    plt.xlabel("Date")
    plt.ylabel("Rolling Std Dev")
    plt.legend()
    plt.show()