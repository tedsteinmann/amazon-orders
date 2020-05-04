from classes.reader import Read
from classes.writer import Write

orders = Read('amazon-orders.csv')
df = orders.df

df['Total'] = (df['Item Total'].replace( '[\$,)]','', regex=True ).replace( '[(]','-',   regex=True ).astype(float))

orders_grouped = df.groupby('Category').agg({'Total':['sum','count']}).reset_index().sort_values(by='Category',ascending=False)

print(orders_grouped)
