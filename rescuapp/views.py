from rescuapp import myapp, db, lm, mail
from .forms import LoginForm, SignUpForm, OrderForm 
from flask.ext.login import login_user, logout_user, current_user, login_required 
from .models import User, Order
from flask import make_response, render_template, request, redirect, flash, session, url_for, request, g
from flask.ext.mail import Message
from config import ADMINS
from datetime import datetime
## Routes to the splash page 
## Splash page allows users to log in or sign up


@myapp.route('/')
@myapp.route('/index')
def splash():

    ## login form in case of reroute 
    form = LoginForm()

    ## if user is cached and already logged in, take them to order page 
    if g.user is not None and g.user.is_authenticated:
        return redirect('/order')

    """ if user has seen this before, take them to the login page 
    if request.cookies.get('rescuSplash') == 'yes':
        print("cookie confirmed")
        resp1 = make_response(redirect('/login'))
        return resp1
    else:
        resp = make_response(render_template('splash.html'))
        resp.set_cookie('rescuSplash', 'yes')   
        return resp
    """

 
## Routes to the login page
@myapp.route('/login', methods=['GET','POST'])
def login():

    ##msg = Message('heres some text', sender=ADMINS[0], recipients=ADMINS)
    ##msg.body = 'heres some text'
    ##mail.send(msg)

    form = LoginForm()

    if request.method == 'GET':
        return render_template('login.html', form = form)

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
                print "successful login"
                return redirect(url_for('order'))
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

    ## error handling a signed in user going here directly 
    logout_user()

    form = SignUpForm()

    if request.method == 'GET':
        flash("hello world")
        return render_template('signup.html', form = form)
   
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
@myapp.route('/order', methods=['GET', 'POST'])
@login_required
def order():

    form = OrderForm()

    # render template if page load 
    if request.method == 'GET':
        return render_template('order.html', form=form)

    # if user is submitting an order 
    if 'order' in request.form:
        print "going here"
        # if user submitted every field 
        if form.validate_on_submit():

            orders = Order.query.all()
            num = len(orders)
            # possibly cbeck user hasnt submitted an item 
            # possibly parse database making sure item is in stock
            order = Order(id=num+1, email=g.user.email, dormHall=g.user.dormHall, dormNum=g.user.dormNum, time=form.time.data, item1=form.item1.data, item2=form.item2.data, item3=form.item3.data, item4=form.item4.data, item5=form.item5.data, item6=form.item6.data, item7=form.item7.data, date=datetime.now()) 
            db.session.add(order)
            db.session.commit()

            msg = Message('resqU Order Confirmation  ', sender=ADMINS[0], recipients=[g.user.email])
            msg.body = 'Hey! We just got note of your order. This email is to confirm your order, and to request payment. Your order is as follows: {} {} {} {} {} {}. It will be delivered to {} {} at {}.  Your total comes out to $21.96. Using Venmo, payment must be sent to @resqUprinceton within 30 minutes or your order is nullified. When we receive your payment, you will receive another confirmation email. Thanks for using resqU!'.format(order.item1, order.item2, order.item3, order.item4, order.item5, order.item6, order.dormNum, order.dormHall, order.time)
            mail.send(msg)
            return redirect(url_for('thankyou'))
        else: 
            return render_template('order.html', form=form)

       

    # if user wants to cancel their order 
    elif 'cancelorder' in request.form:
        user = g.user 

        # final all orders by this user 
        orders = user.orders.all()

        # delete their most recent order 
        
        db.session.delete(orders[len(orders)-1])
        db.session.commit()
        flash("order canceled successfully")

        form = OrderForm()
        return render_template('order.html', form=form)

    print "just returning here"
    return render_template('order.html', form=form)

@myapp.route('/thankyou')
@login_required
def thankyou():
    return "Your order has been sent, thanks!"

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



