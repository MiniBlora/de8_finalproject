select bp."Product"  , sum(bt.amount_transaction) as amount --, bp."Type"
from bigdata_transaction bt 
left join bigdata_product bp 
on bt.product_transaction = bp."Type" 
group by bp."Product" --,bp."Type" 
order by amount desc