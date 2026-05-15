import pandas as pd
from transformers import pipeline


# -----------------------------
# Load cleaned dataset
# -----------------------------
df = pd.read_csv("data/raw/bank_reviews_cleaned.csv")

print("Dataset loaded successfully.")
print(df.shape)


# -----------------------------
# Load sentiment analysis model
# -----------------------------
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

print("\nDistilBERT model loaded.")


# -----------------------------
# Sentiment classification
# -----------------------------
sentiment_labels = []
sentiment_scores = []


for review in df["review"]:

    # Handle empty or invalid reviews
    if pd.isna(review) or str(review).strip() == "":
        sentiment_labels.append("neutral")
        sentiment_scores.append(0.0)
        continue

    try:
        result = sentiment_pipeline(str(review[:512]))[0]

        label = result["label"].lower()
        score = result["score"]

        # Create neutral category for low confidence
        if score < 0.60:
            label = "neutral"

        sentiment_labels.append(label)
        sentiment_scores.append(score)

    except Exception as e:
        print(f"Error processing review: {e}")

        sentiment_labels.append("neutral")
        sentiment_scores.append(0.0)


# -----------------------------
# Add results to dataframe
# -----------------------------
df["sentiment_label"] = sentiment_labels
df["sentiment_score"] = sentiment_scores


# -----------------------------
# Display summary
# -----------------------------
print("\nSentiment Distribution:")
print(df["sentiment_label"].value_counts())


# -----------------------------
# Save results
# -----------------------------
df.to_csv("data/raw/bank_reviews_sentiment.csv", index=False)

print("\nSentiment analysis completed successfully.")