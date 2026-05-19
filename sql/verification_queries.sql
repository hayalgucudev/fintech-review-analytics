SELECT COUNT(*) FROM reviews;

SELECT bank_name, COUNT(*)
FROM reviews
JOIN banks
ON reviews.bank_id = banks.bank_id
GROUP BY bank_name;

SELECT bank_name,
AVG(sentiment_score)
FROM reviews
JOIN banks
ON reviews.bank_id = banks.bank_id
GROUP BY bank_name;

SELECT *
FROM reviews
WHERE identified_theme IS NULL;