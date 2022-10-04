#import modules
from flask import Blueprint, render_template, request, flash, redirect, url_for  
from flask_login import LoginManager, login_user, login_required, current_user, logout_user 
from werkzeug.security import generate_password_hash

from website.forms import LoginForm, RegistrationForm

auth = Blueprint('auth', __name__)

#import views

from .views import views

#import models

from .models import db, User


#Define authentication approval request route
# @auth.route('/approval', methods=['GET', 'POST'])
# def approval():
#     user = User()
#     if user.is_approved:


#define login
@auth.route('/login', methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.profile'))
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        if current_user.is_approved:
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(email=email).first()
            if user:
                if user.password == password:
                    login_user(user, remember = form.remember.data)
                    return redirect(url_for('views.profile'))      
    return render_template('login.html', form = form)

#define logout
@auth.route('/logout')
def logout():
    logout_user()
    return "you have logged out Click here to go back to the <a href='/'>home page</a>"


#define sign up
@auth.route("/sign-up", methods = ['GET','POST'])
def sign_up():
    #Get submissions from signup post
    if current_user.is_authenticated:
        return redirect(url_for('views.profile'))
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        if current_user.is_approved:
            new_user = User(name = form.username.data, email = form.email.data, password = form.password.data )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash ('Account created', category = 'success')
            return redirect(url_for('views.profile'))
        else:
            flash ('Account not approved by Head of Boarding', category = 'error')
            return redirect (url_for('auth.sign_up'))

    return render_template('sign_up.html', form = form)

#define admin sign up route
@auth.route("/admin-sign-up", methods = ['GET','POST'])
def admin_sign_up():
    form = RegistrationForm()
    if form.validate_on_submit and request.method == 'POST':
        new_user = User(email = form.email.data, password = form.password.data, name = form.username.data, admin = True)
        current_user.is_admin = True
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        flash ('Account created', category = 'success')
        
    return render_template('admin_sign_up.html')

# #define admin login route * remember to add more to this
@auth.route("/admin-login", methods = ['GET','POST'])
def admin_login():
    form = LoginForm()
    if request.method =='POST':
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                login_user(user)
                return redirect(url_for('views.admin'))
    return render_template('admin_login.html')





