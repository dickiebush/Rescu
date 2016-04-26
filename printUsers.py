from rescuapp import myapp, db, models

## get all users
users = models.User.query.all()

## write all users to file users.txt
file = open('users.txt', 'w')
for u in users:
    userAsString = u.__repr__()
    file.write(userAsString)
    file.write('\n')
file.close()