WTF_CSRF_ENABLED = True

SECRET_KEY = 'you_suck'

# database setup 
import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'myapp.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# email server 
DEBUG = True
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'princetonresqu@gmail.com'
MAIL_PASSWORD = 'stealing1'

# administrator list
ADMINS = ['princetonresqu@gmail.com']
