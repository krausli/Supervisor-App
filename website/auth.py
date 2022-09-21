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

#define login
@auth.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                login_user(user)
                return redirect(url_for('profile'))      
    return render_template('login.html', form = form)

#define logout
@auth.route('/logout')
def logout():
    logout_user()
    return render_template('home.html')


#define sign up
@auth.route("/sign-up", methods = ['GET','POST'])
def sign_up():
    #Get submissions from signup post
    # if request.method == 'POST':
    form = RegistrationForm()
    if form.validate_on_submit():
        if len(form.email.data) < 4:
            flash ("Email must be more than 4 characters long", category = 'error')
        elif len(form.username.data) < 2:
            flash ('first name must be more than 2 characters long', category = 'error')
        elif form.password.data != form.confirm_password.data:
            flash ('password must be the same', category = 'error')
        elif len(form.password.data) < 6:
            flash ('password cannot be less than 6 characters', category = 'error')
        else:
            #add user to database
            new_user = User(name = form.username.data, email = form.email.data, password1 = form.password.data , password2 = form.confirm_password.data )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash ('Account created', category = 'success')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html', form = form)

#define admin sign up route
@auth.route("/admin-sign-up", methods = ['GET','POST'])
def admin_sign_up():
    from .models import User
    if request.method =='POST':
        new_user = User(email = request.form['email'], password = request.form['password'] )
    return render_template('admin_sign_up.html')

