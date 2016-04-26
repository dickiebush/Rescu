from flask import Flask 
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail

## Create the app with name
myapp = Flask(__name__)


## Create the configuration
myapp.config.from_object('config')

mail = Mail(myapp)

## Suppress this warning when migrating or creating database 
myapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

## Set up the datbase 
db = SQLAlchemy(myapp)

import os 
from flask.ext.login import LoginManager
from config import basedir

lm = LoginManager()
lm.init_app(myapp)

from rescuapp import views, models

