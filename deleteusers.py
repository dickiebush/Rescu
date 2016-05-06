from rescuapp import models, myapp, db


users = models.User.query.all()

for u in users:
    db.session.delete(u)
    db.session.commit()

