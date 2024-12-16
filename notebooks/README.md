# Task 1 News Data Analysis Project

This repository contains the code and analysis for exploring and analyzing news datasets. The project focuses on Exploratory Data Analysis (EDA), text analysis, time series analysis, and publisher insights.
Project Overview

## 1. Repository Setup

    Created a GitHub repository with a dedicated branch: feature/task-1.
    Committed progress at least three times a day with descriptive messages.

## 2. Exploratory Data Analysis (EDA)

    Descriptive Statistics:
        Analyzed headline lengths to understand textual data distribution.
        Identified the most active publishers and their contributions.
        Studied publication dates to observe trends over time.

## 3. Text Analysis

    Sentiment Analysis: Classified headlines as Positive, Negative, or Neutral.
    Topic Modeling: Identified common keywords and significant topics like "FDA approval" and "price target".

## 4. Time Series Analysis

    Analyzed publication frequency trends and identified spikes in news activity.
    Studied publishing times to discover peak hours of news releases.

## 5. Publisher Analysis

    Identified top publishers and analyzed their focus areas.
    Extracted unique email domains (if available) to group contributors.

### How to Use

    Clone the Repository:

```bash
git clone https://github.com/naolatomsa/Nova-Financial-Solutions.git
cd Nova-Financial-Solutions

Switch to Task-1 Branch:

git checkout feature/task-1

Run the Notebook:

    Install dependencies:

        pip install -r requirements.txt

        Open and execute the Jupyter notebook.
  ```

## Key Files

    edaAnalysis.ipynb: Contains the analysis and visualizations.
    requirements.txt: List of required Python libraries.
    README.md: Documentation for this project.

## Technologies Used

    Libraries:
        pandas, matplotlib, seaborn: Data manipulation and visualization.
        TextBlob, NLTK: Sentiment analysis.
        sklearn, gensim: Topic modeling.
        wordcloud: Generate word clouds.


# Task 2 Quantitative analysis

This notebook analyzes stock price data by calculating technical indicators and financial metrics, and visualizing trends for better insights.

## Features

    Calculates technical indicators:
        Simple Moving Average (SMA)
        Relative Strength Index (RSI)
        Moving Average Convergence Divergence (MACD)
    Computes financial metrics:
        Daily Returns
        Cumulative Returns
    Visualizes stock trends and key indicators.

## Usage

    Ensure your dataset includes Open, High, Low, Close, and Volume columns.
    Replace the sample data loading function with your dataset.
    Run the notebook to calculate metrics and generate visualizations.



# Task 3: Correlation Between News and Stock Movement

# Objective

Analyze the relationship between news sentiment and stock price movements.

# Steps

    Data Alignment: Normalize dates in news and stock datasets.
    Sentiment Analysis: Assign sentiment scores (Positive, Negative, Neutral) to news headlines using tools like TextBlob.
    Stock Returns: Calculate daily percentage changes in closing prices.
    Correlation: Compute the Pearson correlation coefficient between average daily sentiment scores and stock returns.

# Development

    Create a task-3 branch for development.
    Commit progress with clear messages.
    Merge updates into main via a Pull Request (PR).

# KPIs

    Sentiment Analysis Accuracy
    Correlation Strength Analysis