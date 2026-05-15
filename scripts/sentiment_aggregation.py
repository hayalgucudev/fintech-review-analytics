import pandas as pd


# -----------------------------
# Load sentiment dataset
# -----------------------------
df = pd.read_csv("data/raw/bank_reviews_sentiment.csv")

print("Dataset loaded successfully.")
print(df.shape)


# -----------------------------
# Sentiment distribution by bank
# -----------------------------
print("\nSentiment Distribution by Bank:\n")

bank_sentiment = pd.crosstab(
    df["bank"],
    df["sentiment_label"]
)

print(bank_sentiment)


# -----------------------------
# Average sentiment score by bank
# -----------------------------
print("\nAverage Sentiment Score by Bank:\n")

avg_sentiment = df.groupby("bank")["sentiment_score"].mean()

print(avg_sentiment)


# -----------------------------
# Average sentiment by rating
# -----------------------------
print("\nAverage Sentiment Score by Rating:\n")

rating_sentiment = df.groupby("rating")["sentiment_score"].mean()

print(rating_sentiment)


# -----------------------------
# Save aggregation results
# -----------------------------
bank_sentiment.to_csv(
    "data/raw/sentiment_distribution_by_bank.csv"
)

avg_sentiment.to_csv(
    "data/raw/average_sentiment_by_bank.csv"
)

rating_sentiment.to_csv(
    "data/raw/average_sentiment_by_rating.csv"
)

print("\nAggregation results saved successfully.")