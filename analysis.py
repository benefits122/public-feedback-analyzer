"""
Public Feedback Analyzer
Author: Nwachukwu Charles

This script demonstrates a simple Natural Language Processing workflow
for analyzing public feedback text data.

The goal is to transform unstructured citizen complaints or survey responses
into structured insights such as sentiment scores and key themes.

This project supports multimodal communication and governance research.
"""

import pandas as pd
from textblob import TextBlob

# -----------------------------
# Step 1: Load Feedback Dataset
# -----------------------------

# Example dataset structure:
# feedback_id, category, feedback_text

data = {
    "feedback_id": [1, 2, 3, 4, 5],
    "category": ["Network", "Billing", "Customer Service", "Network", "Other"],
    "feedback_text": [
        "The network has been terrible for weeks.",
        "I was charged twice for the same service.",
        "Customer support was very helpful and polite.",
        "Calls keep dropping every day, very frustrating.",
        "The service is okay but could improve."
    ]
}

df = pd.DataFrame(data)

# -----------------------------
# Step 2: Sentiment Scoring
# -----------------------------

def get_sentiment(text):
    """
    Returns sentiment polarity score:
    -1 = negative, +1 = positive
    """
    return TextBlob(text).sentiment.polarity

df["sentiment_score"] = df["feedback_text"].apply(get_sentiment)

# -----------------------------
# Step 3: Basic Severity Labeling
# -----------------------------

def label_severity(score):
    """
    Converts sentiment score into simple severity levels.
    """
    if score <= -0.3:
        return "High Concern"
    elif score < 0.1:
        return "Moderate Concern"
    else:
        return "Low Concern"

df["severity_level"] = df["sentiment_score"].apply(label_severity)

# -----------------------------
# Step 4: Summary Insights
# -----------------------------

print("\n=== Public Feedback Analyzer Summary ===\n")
print(df[["feedback_id", "category", "sentiment_score", "severity_level"]])

print("\nAverage Sentiment Score:", round(df["sentiment_score"].mean(), 2))

print("\nTop Categories by Frequency:")
print(df["category"].value_counts())

# -----------------------------
# End of Script
# -----------------------------
