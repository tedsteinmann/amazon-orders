from classes.reader import Read
from classes.writer import Write

orders = Read('amazon-orders.csv')
df = orders.df

df['Total'] = (df['Item Total'].replace( '[\$,)]','', regex=True ).replace( '[(]','-',   regex=True ).astype(float))

orders_grouped = df.groupby(['Category'],sort=True).sum().reset_index()
orders_grouped = orders_grouped.sort_values(by=['Total','Quantity'], ascending=[False,False])


print(orders_grouped)
