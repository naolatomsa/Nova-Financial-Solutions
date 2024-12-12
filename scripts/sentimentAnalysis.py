from textblob import TextBlob

def perform_sentiment_analysis(data, text_column='headline'):

    # Ensure the column exists
    if text_column not in data.columns:
        raise ValueError(f"Column '{text_column}' does not exist in the dataset.")
    
    # Perform sentiment analysis
    data['sentiment'] = data[text_column].apply(lambda x: TextBlob(x).sentiment.polarity)
    
    # Categorize sentiment as positive, negative, or neutral
    data['sentiment_category'] = data['sentiment'].apply(
        lambda x: 'positive' if x > 0 else ('negative' if x < 0 else 'neutral')
    )
    return data
