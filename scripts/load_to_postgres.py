import pandas as pd

from sqlalchemy import create_engine


# -----------------------------
# Load dataset
# -----------------------------
try:

    df = pd.read_csv(
        "data/raw/bank_reviews_sentiment.csv"
    )
    df.rename(
    columns={"date": "review_date"},
    inplace=True
)

    print("Dataset loaded successfully.")
    print(df.shape)

except FileNotFoundError:

    print("Dataset file not found.")
    exit()


# -----------------------------
# PostgreSQL connection
# -----------------------------
DATABASE_URL = (
    "postgresql://postgres:1234"
    "@localhost:5432/fintech_reviews"
)

engine = create_engine(DATABASE_URL)


# -----------------------------
# Load into PostgreSQL
# -----------------------------
try:

    df.to_sql(
        "bank_reviews",
        engine,
        if_exists="append",
        index=False
    )

    print("\nData loaded into PostgreSQL successfully.")

except Exception as e:

    print("\nError loading data:")
    print(e)