from app import myapp

## Routes to the splash page 
## Splash page allows users to log in or sign up
@myapp.route('/')
@myapp.route('/index')
def home():
    return "Hello, World!"

## Routes to the login page
@myapp.route('/login')
def login():
    return "Here we log in"

## Routes to the signup page
@myapp.route('/signup')
def signup():
    return "Here we sign up"

## Routes to the order page
@myapp.route('/order')
def order():
    return "Here we make orders"

## Routes to the FAQ Page
@myapp.route ('/FAQ')
def faq():
    return "Here is a list of FAQ"


