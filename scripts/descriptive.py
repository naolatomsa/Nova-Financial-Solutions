import pandas as pd
import matplotlib.pyplot as plt

def get_headline_length_stats(data, headline_column='headline'):
    
    # Ensure the column exists
    if headline_column not in data.columns:
        raise ValueError(f"Column '{headline_column}' does not exist in the dataset.")
    
    # Add a column for headline lengths
    data['headline_length'] = data[headline_column].str.len()
    
    # Get descriptive statistics
    headline_stats = data['headline_length'].describe()
    return headline_stats

def analyze_publisher_activity(data, publisher_column='publisher', top_n=10, visualize=True):
    
    # Ensure the column exists
    if publisher_column not in data.columns:
        raise ValueError(f"Column '{publisher_column}' does not exist in the dataset.")
    
    # Count the number of articles per publisher
    publisher_counts = data[publisher_column].value_counts()

    # Visualize the top publishers if required
    if visualize:
        publisher_counts.head(top_n).plot(kind='bar', figsize=(10, 6), title=f'Top {top_n} Publishers by Article Count')
        plt.xlabel('Publisher')
        plt.ylabel('Number of Articles')
        plt.show()

    return publisher_counts
