import pandas as pd
from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Normalize and Align Dates
def normalize_dates(news_data, stock_data):
    
    news_data.columns = news_data.columns.str.strip().str.lower()
    stock_data.columns = stock_data.columns.str.strip().str.lower()

    news_data['date'] = pd.to_datetime(news_data['date'], format='mixed', errors='coerce', utc='true')
    stock_data['date'] = pd.to_datetime(stock_data['date'], format='mixed', errors='coerce', utc='true')
    
    return news_data, stock_data

# Perform Sentiment Analysis
def analyze_sentiment(news_data):

    def get_sentiment(text):
        return TextBlob(text).sentiment.polarity
    
    news_data['sentiment'] = news_data['headline'].apply(get_sentiment)
    return news_data

# Aggregate Sentiments by Date
def aggregate_sentiments(news_data):

    daily_sentiment = news_data.groupby('date')['sentiment'].mean().reset_index()
    return daily_sentiment

# Calculate Daily Stock Returns
def calculate_stock_returns(stock_data):

    stock_data['Daily_Return'] = stock_data['close'].pct_change() * 100
    return stock_data

# Merge Datasets
def merge_datasets(sentiment_data, stock_data):

    merged_data = pd.merge(sentiment_data, stock_data, on='date', how='inner')
    return merged_data

# Correlation Analysis
def correlation_analysis(merged_data):

    correlation, p_value = pearsonr(merged_data['sentiment'], merged_data['Daily_Return'])
    return correlation, p_value

# Visualization
def plot_correlation(merged_data):

    plt.scatter(merged_data['sentiment'], merged_data['Daily_Return'])
    plt.title('Sentiment vs Stock Returns')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Daily Stock Return (%)')
    plt.show()
