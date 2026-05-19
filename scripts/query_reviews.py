import pandas as pd

from sqlalchemy import create_engine


DATABASE_URL = (
    "postgresql+psycopg2://postgres:1234@localhost:5432/fintech_reviews"
)

engine = create_engine(DATABASE_URL)


query = """
SELECT
    bank,
    sentiment_label,
    COUNT(*) AS total_reviews

FROM bank_reviews

GROUP BY bank, sentiment_label

ORDER BY bank;
"""


df = pd.read_sql(query, engine)

print(df)