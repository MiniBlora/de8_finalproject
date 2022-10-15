DROP TABLE IF EXISTS dim_transactions;
CREATE TABLE dim_transactions (
	id_customer INT NOT NULL,
	birthdate_customer DATE NOT NULL,
	country_customer VARCHAR(255),
	age INT NOT NULL,
	gender_customer VARCHAR(255),
	Type VARCHAR(255),
	id_transaction VARCHAR(255),
	date_transaction DATE,
	product_transaction VARCHAR(255),
	amount_transaction INT
	);