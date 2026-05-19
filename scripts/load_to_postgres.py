import logging
import os
import pandas as pd

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

logging.basicConfig(level=logging.INFO)

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

DB_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

try:

    engine = create_engine(DB_URL)

    df = pd.read_csv(
        "data/processed/bank_reviews_sentiment.csv"
    )

    print("\nDATAFRAME COLUMNS:")
    print(df.columns)

    # Rename date column
    if "date" in df.columns:
        df.rename(
            columns={"date": "review_date"},
            inplace=True
        )

    # Add identified_theme column
    if "identified_theme" not in df.columns:
        df["identified_theme"] = "General Feedback"

    # Unique banks only
    banks_df = pd.DataFrame({
        "bank_name": df["bank"].unique()
    })

    # Insert banks
    banks_df.to_sql(
        "banks",
        engine,
        if_exists="append",
        index=False
    )

    # Read banks table
    banks = pd.read_sql(
        "SELECT * FROM banks",
        engine
    )

    print("\nBANKS TABLE:")
    print(banks)

    # Merge bank_id
    df = df.merge(
        banks,
        left_on="bank",
        right_on="bank_name",
        how="left"
    )

    print("\nAFTER MERGE:")
    print(df.columns)

    review_columns = [
        "bank_id",
        "review",
        "rating",
        "review_date",
        "sentiment_label",
        "sentiment_score",
        "identified_theme"
    ]

    df[review_columns].to_sql(
        "reviews",
        engine,
        if_exists="append",
        index=False
    )

    logging.info(
        "Database loading successful."
    )

except FileNotFoundError:

    logging.error(
        "Dataset file not found."
    )

except SQLAlchemyError as e:

    logging.error(e)

except Exception as e:

    logging.error(e)