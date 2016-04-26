from rescuapp import db 

## Eventually link to CAS
## For now, take email, password, etc. 
class User(db.Model):
    email    = db.Column(db.String(120), index=True, unique=True, primary_key=True)
    password = db.Column(db.String(120), index=True)
    fullname = db.Column(db.String(64), index=True)
    dormHall = db.Column(db.String(64), index=True)
    dormNum  = db.Column(db.Integer)
    orders   = db.relationship('Order', backref='Orderer', lazy='dynamic')

    def __repr__(self):
        return '<User {} lives in {} {}>'.format(self.email, self.dormHall, self.dormNum)

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
class Order(db.Model):
    id       = db.Column(db.Integer, primary_key=True, unique=True)
    email    = db.Column(db.String(120), db.ForeignKey('user.email'), index=True)
    dormHall = db.Column(db.String(64), index=True)
    dormNum  = db.Column(db.Integer)
    time     = db.Column(db.String(10))
    item1    = db.Column(db.String(200))
    item2    = db.Column(db.String(200))
    item3    = db.Column(db.String(200))
    item4    = db.Column(db.String(200))
    item5    = db.Column(db.String(200))
    item6    = db.Column(db.String(200))
    item7    = db.Column(db.String(200))
    date     = db.Column(db.DateTime)

    def __repr__(self):

        return '< {} User {}, delivered to {} {} at {}, ordered {},{},{},{},{},{} and {}>'.format(self.date, self.email, self.dormHall, self.dormNum, self.time,  self.item1, self.item2, self.item3, self.item4 ,self.item5 ,self.item6, self.item7)