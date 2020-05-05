from classes.reader import Read
from classes.writer import Write
from classes.mapper import Map

import pandas as pd

#READ ORDERS
#----------------------
orders = Read('amazon-orders.csv')
orders_df = orders.df #['Order Date','Category','Quantity','Item Total']
orders_df = orders_df[['Order Date','Category','Quantity','Item Total']].copy(deep=False)
#print(df.head())

# DFINE CATEGORY MAPPINGS
#----------------------
mapper = Map('categories.csv','Category')


# REMOVE $ CHARACTER
#----------------------
orders_df['Total'] = (orders_df['Item Total'].replace( '[\$,)]','', regex=True ).astype(float))


# ORDERS BY MONTHLY SPEND
#----------------------
mapped_orders = mapper.map_data(orders_df,'Category')

# make a month column to preserve the order
mapped_orders['month'] = pd.to_datetime(mapped_orders['Order Date']).dt.strftime('%m')

# create the pivot table with this numeric month column
orders_df_pivot = mapped_orders.pivot_table(index='month',columns=['Parent Category'],values=['Total'],aggfunc=sum, fill_value=0).T

# print(orders_df_pivot)

Write(orders_df_pivot,'orders_by_monthly_spend')


# ORDERS GROUPED BY CATEGORY
#-------------------
orders_grouped = orders_df.groupby(['Category'],sort=True).sum().reset_index()

orders_grouped = orders_grouped.sort_values(by=['Total','Quantity'], ascending=[False,False])

#print(orders_grouped)
Write(orders_grouped,'orders_by_category')

# ORDERS GROUPED BY PARENT CATEGORY
#----------------------

mapped_grouped_orders = mapper.map_data(orders_grouped,'Category')

mapped_grouped_orders = mapped_grouped_orders.groupby(['Parent Category'],sort=True).sum().reset_index()
mapped_grouped_orders = mapped_grouped_orders.sort_values(by=['Total','Quantity'], ascending=[False,False])

#print(mapped_orders)
Write(mapped_grouped_orders,'orders_by_parent_category')
