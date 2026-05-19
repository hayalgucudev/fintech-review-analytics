DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS banks;

CREATE TABLE banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    bank_id INTEGER REFERENCES banks(bank_id),

    review TEXT,
    rating INTEGER,
    review_date DATE,

    sentiment_label VARCHAR(50),
    sentiment_score FLOAT,

    identified_theme VARCHAR(255)
);