--select bc.id_customer as id_customer, bc.name_customer as name_customer , sum(bt.amount_transaction) as amount
--from bigdata_customer bc 
--left join bigdata_transaction bt 
--on bc.id_customer = bt.id_customer 
--group by bc.id_customer, bc.name_customer

select
	bc.id_customer,
	bc.birthdate_customer,
	bc.country_customer,
	date_part('year',age(TO_DATE(bc.birthdate_customer,'YYYY-MM-DD'))) age,
	bc.gender_customer,
	bp."Type",
	bt.id_transaction,
	bt.date_transaction,
	bt.product_transaction,
	bt.amount_transaction
from bigdata_customer bc
	left join bigdata_transaction bt on bc.id_customer = bt.id_customer
	left join bigdata_product bp on bp."Type" = bt.product_transaction
