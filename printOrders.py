from rescuapp import myapp, db, models

## get all orders
orders = models.Order.query.all()

## write all users to file users.txt
file = open('order.txt', 'w')
for o in orders:
    orderAsString = o.__repr__()
    file.write(orderAsString)
    file.write('\n')
file.close()