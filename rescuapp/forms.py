from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, IntegerField, SelectField
from wtforms import validators 
from rescuapp import db, models

## Log in form, based on necessary information of db.User model
class LoginForm(Form):
    email       = StringField('email', validators=[validators.DataRequired(), validators.email()])
    password    = PasswordField('password', validators=[validators.DataRequired()])
    remember_me = BooleanField('remember_me', default=True)

## Sign up form, based on all information of db.User model 
class SignUpForm(Form):
    email    = StringField('email', validators=[validators.DataRequired(message="Forgot this one!"), validators.Email(message="This doesn't look like an email.."), validators.Length(message="4 to 25 characters please!",min=4, max=25)])
    password = PasswordField('password', validators=[validators.DataRequired("Whoops!"), validators.EqualTo('conPass', message="Passwords must match"), validators.Length(message="6 to 25 characters please!", min=6, max=25)])
    conPass  = PasswordField('conPass', validators=[validators.DataRequired("You forgot me!"), validators.EqualTo('password')],)
    fullname = StringField('fullname', validators=[validators.DataRequired("You forgot me!")])
    dormHall = StringField('dormHall', validators = [validators.DataRequired("Please enter a valid dorm")])
    dormNum  = IntegerField('dorm', validators = [validators.DataRequired("Please enter a valid dorm number")])

## Order form -- some data pulled from user submitting and rest put through this form 
class OrderForm(Form):
    time  = SelectField(u'time', choice=[('9:00 AM', '10:00 AM', '11:00 AM')])
    item1 = StringField('first item', validators=[validators.DataRequired("You have to order something!")])
    item2 = StringField('second item')
    item3 = StringField('third item')
    item4 = StringField('fourth item')
    item5 = StringField('fifth item')
    item6 = StringField('sixth item')
    item7 = StringField('seventh item')

