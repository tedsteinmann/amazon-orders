from classes.reader import Read
from classes.writer import Write

orders = Read('amazon-orders.csv')
order_count = orders.df.shape[0]
print("Orders: ",order_count)
