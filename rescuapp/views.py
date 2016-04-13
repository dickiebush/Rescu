from rescuapp import myapp, db
from .forms import LoginForm, SignUpForm, OrderForm 
from flask.ext.login import login_user, logout_user, current_user, login_required 
from .models import User, Order
from flask import make_response, render_template, request, redirect, flash, session, url_for, request, g

## Routes to the splash page 
## Splash page allows users to log in or sign up
@myapp.route('/')
@myapp.route('/index')
def home():
    return render_template('splash.html')

## Routes to the login page
@myapp.route('/login')
def login():

    ## LEFTOFF -- Handle Login backend processing
    form = LoginForm()
    return render_template('login.html', form=form)

## Routes to the signup page
@myapp.route('/signup')
def signup():

    ## LEFTOFF -- Put together sin up front end and backend 
    return render_template('signup.html')

## Routes to the order page
@myapp.route('/order')
def order():
    return render_template('order.html')

## Routes to the FAQ Page
@myapp.route ('/faq')
def faq():
    return render_template('FAQ.html')

