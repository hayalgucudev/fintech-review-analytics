import pytest
import pandas as pd


# -----------------------------
# Sample preprocessing function
# -----------------------------
def remove_duplicates(df):

    return df.drop_duplicates()


# -----------------------------
# Test duplicate removal
# -----------------------------
def test_remove_duplicates():

    data = {
        "review": [
            "Good app",
            "Good app",
            "Bad app"
        ],
        "rating": [5, 5, 1]
    }

    df = pd.DataFrame(data)

    cleaned_df = remove_duplicates(df)

    assert len(cleaned_df) == 2


# -----------------------------
# Test missing values
# -----------------------------
def test_missing_values():

    data = {
        "review": [
            "Good app",
            None,
            "Bad app"
        ],
        "rating": [5, 4, None]
    }

    df = pd.DataFrame(data)

    cleaned_df = df.dropna(
        subset=["review", "rating"]
    )

    assert cleaned_df.isnull().sum().sum() == 0