import pandas as pd
import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer


# Download resources
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")


# -----------------------------
# Load dataset
# -----------------------------
try:
    df = pd.read_csv("data/raw/bank_reviews_sentiment.csv")

    print("Dataset loaded successfully.")
    print(df.shape)

except FileNotFoundError:
    print("Dataset file not found.")
    exit()


# -----------------------------
# Stopwords
# -----------------------------
stop_words = set(stopwords.words("english"))


# -----------------------------
# Text cleaning
# -----------------------------
def clean_text(text):

    text = str(text).lower()

    text = re.sub(r"http\S+", "", text)

    text = re.sub(r"[^a-zA-Z\s]", "", text)

    tokens = word_tokenize(text)

    filtered_tokens = [
        word for word in tokens
        if word not in stop_words and len(word) > 2
    ]

    return " ".join(filtered_tokens)


# Apply cleaning
df["cleaned_review"] = df["review"].apply(clean_text)

print("\nText cleaning completed.")


# -----------------------------
# Per-bank keyword extraction
# -----------------------------
banks = df["bank"].unique()

all_results = []


for bank in banks:

    print(f"\n========== {bank} ==========")

    bank_reviews = df[df["bank"] == bank]

    vectorizer = TfidfVectorizer(
        max_features=5,
        ngram_range=(1, 2)
    )

    X = vectorizer.fit_transform(
        bank_reviews["cleaned_review"]
    )

    keywords = vectorizer.get_feature_names_out()

    print("\nTop Keywords:")

    for keyword in keywords:
        print(keyword)

        all_results.append({
            "bank": bank,
            "keyword": keyword
        })


# -----------------------------
# Save results
# -----------------------------
results_df = pd.DataFrame(all_results)

results_df.to_csv(
    "data/raw/bank_keywords.csv",
    index=False
)

print("\nPer-bank thematic analysis completed.")