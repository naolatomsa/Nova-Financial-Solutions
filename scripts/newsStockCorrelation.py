import pandas as pd
from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Load datasets
def load_data(news_path, stock_path):

    news_data = pd.read_csv(news_path)
    stock_data = pd.read_csv(stock_path)
    return news_data, stock_data

# Normalize and Align Dates
def normalize_dates(news_data, stock_data):

    news_data['Date'] = pd.to_datetime(news_data['Date']).dt.date
    stock_data['Date'] = pd.to_datetime(stock_data['Date']).dt.date
    return news_data, stock_data

# Perform Sentiment Analysis
def analyze_sentiment(news_data):

    def get_sentiment(text):
        return TextBlob(text).sentiment.polarity
    
    news_data['Sentiment'] = news_data['Headline'].apply(get_sentiment)
    return news_data

# Aggregate Sentiments by Date
def aggregate_sentiments(news_data):

    daily_sentiment = news_data.groupby('Date')['Sentiment'].mean().reset_index()
    return daily_sentiment

# Calculate Daily Stock Returns
def calculate_stock_returns(stock_data):

    stock_data['Daily_Return'] = stock_data['Close'].pct_change() * 100
    return stock_data

# Merge Datasets
def merge_datasets(sentiment_data, stock_data):

    merged_data = pd.merge(sentiment_data, stock_data, on='Date', how='inner')
    return merged_data

# Correlation Analysis
def correlation_analysis(merged_data):

    correlation, p_value = pearsonr(merged_data['Sentiment'], merged_data['Daily_Return'])
    return correlation, p_value

# Visualization
def plot_correlation(merged_data):

    plt.scatter(merged_data['Sentiment'], merged_data['Daily_Return'])
    plt.title('Sentiment vs Stock Returns')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Daily Stock Return (%)')
    plt.show()
