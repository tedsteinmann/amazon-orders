from classes.reader import Read
from classes.writer import Write
from classes.mapper import Map

orders = Read('amazon-orders.csv')
df = orders.df #['Order Date','Category','Quantity','Item Total']
df = df[['Order Date','Category','Quantity','Item Total']].copy(deep=False)
#print(df.head())

df['Total'] = (df['Item Total'].replace( '[\$,)]','', regex=True ).astype(float))

orders_grouped = df.groupby(['Category'],sort=True).sum().reset_index()
orders_grouped = orders_grouped.sort_values(by=['Total','Quantity'], ascending=[False,False])

#print(orders_grouped)
Write(orders_grouped,'orders_grouped')

mapper = Map('categories.csv','Category')

mapped_orders = mapper.map_data(orders_grouped,'Category')

#print(mapped_orders)
Write(mapped_orders,'mapped_orders')

# make a month column to preserve the order
# mapped_orders['month'] = pd.to_datetime(df['date']).dt.strftime('%m')
