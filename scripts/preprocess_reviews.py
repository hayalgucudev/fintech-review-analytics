import pandas as pd


# Load raw dataset
df = pd.read_csv("data/raw/bank_reviews_raw.csv")

print("Initial dataset shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)


# -----------------------------
# Remove duplicate reviews
# -----------------------------
duplicates = df.duplicated().sum()

print(f"\nNumber of duplicate rows: {duplicates}")

df = df.drop_duplicates()


# -----------------------------
# Handle missing values
# -----------------------------
missing_before = df.isnull().sum()

print("\nMissing values before cleaning:")
print(missing_before)


# Drop rows missing critical fields
df = df.dropna(subset=["review", "rating"])


missing_after = df.isnull().sum()

print("\nMissing values after cleaning:")
print(missing_after)


# -----------------------------
# Normalize date format
# -----------------------------
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")


# -----------------------------
# Keep only required columns
# -----------------------------
df = df[["review", "rating", "date", "bank", "source"]]


# -----------------------------
# Final dataset info
# -----------------------------
print("\nFinal dataset shape:")
print(df.shape)

print("\nSample data:")
print(df.head())


# -----------------------------
# Save cleaned dataset
# -----------------------------
df.to_csv("data/raw/bank_reviews_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully.")

"""
Preprocess customer reviews by:
- removing punctuation
- converting text to lowercase
- removing stopwords
- preparing text for sentiment analysis
"""