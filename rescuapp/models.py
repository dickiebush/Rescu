from app import db 

## Eventually link to CAS
## For now, take email, password, etc. 
class User(db.Model):
    email    = db.Column(db.String(120), index=True, unique=True, primary_key=True)
    password = db.Column(db.String(120), index=True)
    fullname = db.Column(db.String(64), index=True)
    dormHall = db.Column(db.String(64), index=True)
    dormNum  = db.Column(db.Integer)

    def __repr__(self):
        return ('<User %r lives in %r %d>' % (self.email), self.dormHall, self.dormNum)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.email)  # python 2
        except NameError:
            return str(self.email)

## Order model 
## Email, location, items, time
class Order(db.Model)
    id      = db.Column(db.Integer, primary_key=True)
    email   = db.Column(db.String(120), index=True, unique=True, primary_key=True)
    dormNum = dormHall = db.Column(db.String(64), index=True)
    dormNum = db.Column(db.Integer)
    time    = db.Column(db.String(10))
    items   = db.Column(db.ARRAY(Integer))

    def __repr__(self):

        s = ",".join(items);
        return ('<User %r, delivered to %r %d at %r, ordered %r>', % self.email, self.dormHall, self.dormNum, self.time, s)

