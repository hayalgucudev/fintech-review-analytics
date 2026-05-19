import pandas as pd


# Load dataset
df = pd.read_csv(
    "data/raw/bank_reviews_sentiment.csv"
)


# Overall sentiment
print("\nOverall Sentiment Distribution:\n")

print(
    df["sentiment_label"].value_counts()
)


# Average ratings
print("\nAverage Ratings by Bank:\n")

print(
    df.groupby("bank")["rating"].mean()
)


# Negative review counts
print("\nNegative Reviews by Bank:\n")

negative_reviews = df[
    df["sentiment_label"] == "negative"
]

print(
    negative_reviews["bank"].value_counts()
)