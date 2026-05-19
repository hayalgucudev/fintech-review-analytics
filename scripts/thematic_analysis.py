import pandas as pd
import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")


# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("data/raw/bank_reviews_sentiment.csv")

print("Dataset loaded successfully.")
print(df.shape)


# -----------------------------
# Stopwords
# -----------------------------
stop_words = set(stopwords.words("english"))


# -----------------------------
# Text cleaning function
# -----------------------------
def clean_text(text):

    text = str(text).lower()

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove special characters
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Tokenize
    tokens = word_tokenize(text)

    # Remove stopwords
    filtered_tokens = [
        word for word in tokens
        if word not in stop_words and len(word) > 2
    ]

    return " ".join(filtered_tokens)


# -----------------------------
# Apply cleaning
# -----------------------------
df["cleaned_review"] = df["review"].apply(clean_text)

print("\nText cleaning completed.")


# -----------------------------
# TF-IDF Vectorizer
# -----------------------------
vectorizer = TfidfVectorizer(
    max_features=30,
    ngram_range=(1, 2)
)

X = vectorizer.fit_transform(df["cleaned_review"])


# -----------------------------
# Extract keywords
# -----------------------------
keywords = vectorizer.get_feature_names_out()

print("\nTop Keywords and N-grams:\n")

for keyword in keywords:
    print(keyword)


# -----------------------------
# Save keywords
# -----------------------------
keywords_df = pd.DataFrame({
    "keyword": keywords
})

keywords_df.to_csv(
    "data/raw/tfidf_keywords.csv",
    index=False
)

print("\nKeyword extraction completed.")