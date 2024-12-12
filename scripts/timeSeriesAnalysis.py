import pandas as pd
import matplotlib.pyplot as plt

def prepare_news_data(news_data, date_column='date'):

    # Convert the date column to datetime format
    news_data[date_column] = pd.to_datetime(news_data[date_column])
    
    # Extract date and hour components
    news_data['date_only'] = news_data[date_column].dt.date
    news_data['hour'] = news_data[date_column].dt.hour
    
    return news_data


def analyze_publication_frequency(news_data, date_column='date_only', visualize=True):

    # Count the number of articles per day
    daily_counts = news_data.groupby(date_column).size().reset_index(name='article_count')
    daily_counts[date_column] = pd.to_datetime(daily_counts[date_column])

    # Plot the publication frequency
    if visualize:
        plt.figure(figsize=(12, 6))
        plt.plot(daily_counts[date_column], daily_counts['article_count'], label='Articles per Day')
        plt.title('Publication Frequency Over Time')
        plt.xlabel('Date')
        plt.ylabel('Number of Articles')
        plt.legend()
        plt.show()

    return daily_counts

def analyze_publishing_times(news_data, hour_column='hour', visualize=True):

    # Count the number of articles by hour
    hourly_counts = news_data.groupby(hour_column).size().reset_index(name='article_count')
    
    # Plot the publication frequency by hour
    if visualize:
        plt.figure(figsize=(12, 6))
        plt.bar(hourly_counts[hour_column], hourly_counts['article_count'], color='skyblue')
        plt.title('Publication Frequency by Hour of the Day')
        plt.xlabel('Hour of the Day')
        plt.ylabel('Number of Articles')
        plt.xticks(range(0, 24))  # Show all hours from 0 to 23
        plt.show()
    
    return hourly_counts


def overlay_market_events(publication_data, event_dates, date_column='date_only', visualize=True):

    # Add event descriptions to the publication data
    publication_data['event'] = publication_data[date_column].dt.strftime('%Y-%m-%d').map(event_dates)

    # Plot the publication frequency with events
    if visualize:
        plt.figure(figsize=(12, 6))
        plt.plot(publication_data[date_column], publication_data['article_count'], label='Articles per Day')
        for _, row in publication_data.iterrows():
            if pd.notnull(row['event']):
                plt.axvline(row[date_column], color='red', linestyle='--', alpha=0.6)
                plt.text(row[date_column], row['article_count'], row['event'], color='red', rotation=45)
        plt.title('Publication Frequency Over Time with Market Events')
        plt.xlabel('Date')
        plt.ylabel('Number of Articles')
        plt.legend()
        plt.show()

    return publication_data
