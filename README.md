# Fintech Review Analytics

Customer Experience Analytics for Ethiopian Banking Apps

## Project Overview

This project analyzes customer reviews from Ethiopian banking applications on the Google Play Store. The objective is to extract customer sentiment, identify recurring themes, and generate business insights that can help improve mobile banking experiences.

The analysis focuses on three Ethiopian banks:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

---

## Project Structure

```text
fintech-review-analytics/
│
├── data/
├── notebooks/
├── scripts/
├── src/
├── tests/
├── .github/workflows/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Task 1: Data Collection and Preprocessing

### Data Collection Methodology

Google Play Store reviews were scraped using the `google-play-scraper` Python library.

The following information was collected:

- Review text
- Rating (1–5)
- Review date
- Bank name
- Source

### Applications Scraped

| Bank | App ID |
|---|---|
| CBE | com.combanketh.mobilebanking |
| BOA | com.boa.boaMobileBanking |
| Dashen | com.dashen.dashensuperapp |

### Data Volume

A minimum of 400 reviews per bank was targeted.

Total reviews collected: 1500+ reviews.

### Preprocessing Steps

The following preprocessing steps were performed:

- Removed duplicate reviews
- Removed rows with missing review text or ratings
- Normalized dates to YYYY-MM-DD format
- Standardized output columns

Final dataset columns:

- review
- rating
- date
- bank
- source

---

## Technologies Used

- Python
- pandas
- google-play-scraper
- scikit-learn
- transformers
- PostgreSQL
- matplotlib
- seaborn

---

## CI/CD

GitHub Actions was configured to automatically install dependencies and validate the project workflow on every push to the `main` branch.

---

## Limitations

- Google Play review availability varies by application.
- Some reviews may contain multilingual or very short text.
- Review availability depends on Play Store rate limits and regional availability.

---

## Author

Remetula Ali