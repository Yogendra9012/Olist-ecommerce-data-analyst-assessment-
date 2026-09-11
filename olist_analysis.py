import pandas as pd, numpy as np

orders=pd.read_csv('olist_orders_dataset.csv')
items=pd.read_csv('olist_order_items_dataset.csv')
customers=pd.read_csv('olist_customers_dataset.csv')
payments=pd.read_csv('olist_order_payments_dataset.csv')
reviews=pd.read_csv('olist_order_reviews_dataset.csv')
products=pd.read_csv('olist_products_dataset.csv')
translation=pd.read_csv('product_category_name_translation.csv')

date_cols=['order_purchase_timestamp','order_approved_at','order_delivered_carrier_date',
'order_delivered_customer_date','order_estimated_delivery_date']
for c in date_cols:
    orders[c]=pd.to_datetime(orders[c],errors='coerce')

items2=items.merge(products,on='product_id',how='left').merge(
    translation,on='product_category_name',how='left')

items_agg=items2.groupby('order_id').agg(
    order_items=('order_item_id','count'),
    revenue=('price','sum'),
    freight=('freight_value','sum'),
    unique_products=('product_id','nunique'),
    avg_item_price=('price','mean'),
    product_category=('product_category_name_english',
                      lambda x:x.dropna().mode().iloc[0] if len(x.dropna()) else 'Unknown')
).reset_index()

pay_agg=payments.groupby('order_id').agg(
    payment_value=('payment_value','sum'),
    payment_installments=('payment_installments','max'),
    payment_type=('payment_type',lambda x:x.mode().iloc[0])
).reset_index()

review_agg=reviews.groupby('order_id').agg(
    review_score=('review_score','mean'),
    review_count=('review_id','count')
).reset_index()

processed=(orders.merge(items_agg,on='order_id',how='left')
.merge(pay_agg,on='order_id',how='left')
.merge(review_agg,on='order_id',how='left')
.merge(customers[['customer_id','customer_unique_id','customer_state','customer_city']],
       on='customer_id',how='left'))

processed['delivery_days']=(processed.order_delivered_customer_date-
processed.order_purchase_timestamp).dt.total_seconds()/86400
processed['delivery_vs_estimated_days']=(processed.order_delivered_customer_date-
processed.order_estimated_delivery_date).dt.total_seconds()/86400
processed['on_time']=processed.delivery_vs_estimated_days<=0
processed['freight_pct']=processed.freight/processed.revenue
processed['month']=processed.order_purchase_timestamp.dt.to_period('M').astype(str)

delivered=processed[processed.order_status=='delivered']
print('Delivered orders:',len(delivered))
print('Delivered revenue:',delivered.revenue.sum())
print('Average review:',delivered.review_score.mean())
print('On-time rate:',delivered.on_time.mean())
