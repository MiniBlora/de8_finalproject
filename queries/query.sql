select
	bc.id_customer,
	bc.birthdate_customer,
	bc.country_customer,
	date_part('year',age(TO_DATE(bc.birthdate_customer,'YYYY-MM-DD'))) age,
	bc.gender_customer,
	bp."Type",
	bt.id_transaction,
	year(bt.date_transaction),
	bt.product_transaction,
	bt.amount_transaction
from bigdata_customer bc
	left join bigdata_transaction bt on bc.id_customer = bt.id_customer
	left join bigdata_product bp on bp."Type" = bt.product_transaction
