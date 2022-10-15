DROP TABLE IF EXISTS dwh_transa;
CREATE TABLE dwh_transaction (
--	date_transaction VARCHAR(25),
	year(date_transaction) DATE,
	amount INT
	);
