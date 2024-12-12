import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def analyze_publisher_contribution(data, publisher_column='publisher', top_n=10):

    # Count the number of articles per publisher
    publisher_counts = data[publisher_column].value_counts()

    # Plot the top publishers
    publisher_counts.head(top_n).plot(kind='bar', figsize=(12, 6), color='skyblue')
    plt.title(f'Top {top_n} Publishers by Article Count')
    plt.xlabel('Publisher')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=45)
    plt.show()

    return publisher_counts


def analyze_headlines_by_publisher(data, publisher, publisher_column='publisher', headline_column='headline'):

    # Filter data for the selected publisher
    publisher_data = data[data[publisher_column] == publisher]

    # Concatenate all headlines into one string
    all_headlines = " ".join(publisher_data[headline_column].dropna())

    # Generate a word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_headlines)

    # Display the word cloud
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Most Common Words in Headlines by {publisher}')
    plt.show()


def extract_unique_domains(data, publisher_column='publisher', top_n=10):

    # Extract the domain part of the email
    data['domain'] = data[publisher_column].str.extract(r'@([a-zA-Z0-9.-]+)')

    # Count the number of articles per domain
    domain_counts = data['domain'].value_counts()

    # Plot the top domains
    domain_counts.head(top_n).plot(kind='bar', figsize=(12, 6), color='green')
    plt.title(f'Top {top_n} Domains by Article Count')
    plt.xlabel('Domain')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=45)
    plt.show()

    return domain_counts

