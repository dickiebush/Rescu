from rescuapp import myapp, db, lm
from .forms import LoginForm, SignUpForm, OrderForm 
from flask.ext.login import login_user, logout_user, current_user, login_required 
from .models import User, Order
from flask import make_response, render_template, request, redirect, flash, session, url_for, request, g

## Routes to the splash page 
## Splash page allows users to log in or sign up
@myapp.route('/')
@myapp.route('/index')
def splash():

    ## login form in case of reroute 
    form = LoginForm()

    ## if user has seen this before, take them to the login page 
    if request.cookies.get('rescuSplash') == 'yes':
        print("cookie confirmed")
        return redirect('/login')
    else:
        resp = make_response(render_template('splash.html'))
        resp.set_cookie('rescuSplash', 'yes')   
        return resp

## Routes to the login page
@myapp.route('/login', methods=['GET','POST'])
def login():

    ## if user is cached and already logged in, take them to order page 
    if g.user is not None and g.user.is_authenticated:
        return order()

    form = LoginForm()

    ## if sending a post request and form validates
    if form.validate_on_submit():
        ## query into database looking for user with email name
        user = User.query.get(form.email.data)
        ## (if a user exists)
        if user: 
            ## verify password 
            if form.password.data == user.password:
                if form.remember_me.data:
                    session['remember_me'] = True
                    login_user(user, remember=True)
                else:
                    login_user(user, remember=False)
                ## succesful login
                return order()
            ## wrong password 
            else: 
                return render_template('login.html', form=form, msg1="Incorrect password")
        ## no user 
        else: 
            return render_template('login.html', form=form, msg2="Please enter a valid email")

    return render_template('login.html', form=form)

## Routes to the signup page
@myapp.route('/signup', methods=['GET','POST'])
def signup():

    form = SignUpForm()

    if form.validate_on_submit():

        if User.query.get(form.email.data) is None:

            ## create a user from form data 
            u = User(email=form.email.data, password=form.password.data, fullname=form.fullName.data,
            dormHall=form.dormHall.data, dormNum = form.dormNum.data)

            db.session.add(u)
            db.session.commit()
            login_user(u, remember=True);

            return redirect('/order')

        ## Send back error saying email is already signed up 
        else:
            print("This email is already signed up")
    else:
        print "Form is not validating"
    ## LEFTOFF -- Put together sin up front end and backend 
    return render_template('signup.html', form=form)

## Routes to the order page
@myapp.route('/order')
def order():

    form = OrderForm()
    return render_template('order.html', form=form)

## Routes to the FAQ Page
@myapp.route ('/faq')
def faq():
    return render_template('FAQ.html')

##############################
#     Helper functions       #
##############################
@lm.user_loader
def load_user(id):
    return User.query.get(id)

@myapp.before_request
def before_request():
    g.user = current_user



