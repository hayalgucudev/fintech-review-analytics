import logging
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

logging.basicConfig(level=logging.INFO)

try:

    df = pd.read_csv(
        "data/processed/bank_reviews_sentiment.csv"
    )

    # Create cleaned_review if missing
    if "cleaned_review" not in df.columns:

        df["cleaned_review"] = (
            df["review"]
            .astype(str)
            .str.lower()
        )

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=20
    )

    tfidf_matrix = vectorizer.fit_transform(
        df["cleaned_review"]
    )

    keywords = vectorizer.get_feature_names_out()

    keywords_df = pd.DataFrame({
        "keyword": keywords
    })

    keywords_df.to_csv(
        "data/outputs/tfidf_keywords.csv",
        index=False
    )

    logging.info(
        "TF-IDF thematic analysis completed."
    )

except FileNotFoundError:

    logging.error(
        "Sentiment dataset not found."
    )

except Exception as e:

    logging.error(e)