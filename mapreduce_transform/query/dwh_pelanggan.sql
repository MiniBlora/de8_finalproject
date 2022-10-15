--DROP TABLE IF EXISTS dwh_pelanggan;
--CREATE TABLE dwh_pelanggan (
--	id_customer INT NOT NULL,
--	name_customer VARCHAR(255),
--	amount INT
--	);

DROP TABLE IF EXISTS dwh_pelanggan;
CREATE TABLE dwh_pelanggan (
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