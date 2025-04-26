'''
Customers Who Never Order: Table: Customers
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID and name of a customer.

Table: Orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
customerId is a foreign key (reference columns) of the ID from the Customers table.
Each row of this table indicates the ID of an order and the ID of the customer who ordered it.
'''

import pandas as pd
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result = customers[~customers['id'].isin(orders['customerId'])][['name']]
    return result.rename(columns={'name':'customers'})

customer_data = {
    'id': [1,2,3],
    'name': ['Alice','Bob','Charlie']
}

orders_data = {
    'id': [1,2],
    'customerId': [1,2]
}

customer_df = pd.DataFrame(customer_data)
order_df = pd.DataFrame(orders_data)
print(find_customers(customer_df, order_df))