import pandas as pd
import matplotlib.pyplot as plt

def convert_to_datetime(data, date_column='date'):

    if date_column not in data.columns:
        raise ValueError(f"Column '{date_column}' does not exist in the dataset.")
    data[date_column] = pd.to_datetime(data[date_column])
    return data

def articles_per_day(data, date_column='date', visualize=True):

    articles_by_date = data.groupby(data[date_column].dt.date).size()
    if visualize:
        articles_by_date.plot(figsize=(12, 6), title='Articles Published Over Time')
        plt.xlabel('Date')
        plt.ylabel('Number of Articles')
        plt.show()
    return articles_by_date

def articles_by_weekday(data, date_column='date', visualize=True):

    data['day_of_week'] = data[date_column].dt.day_name()
    articles_weekday = data['day_of_week'].value_counts()
    if visualize:
        articles_weekday.plot(kind='bar', figsize=(10, 6), title='Articles by Day of the Week')
        plt.xlabel('Day of the Week')
        plt.ylabel('Number of Articles')
        plt.show()
    return articles_weekday

def filter_by_date_range(data, date_column='date', start_date=None, end_date=None):

    if start_date:
        data = data[data[date_column] >= start_date]
    if end_date:
        data = data[data[date_column] <= end_date]
    return data