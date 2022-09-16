#import modules
from flask import Blueprint, render_template, request, flash, redirect, url_for  
from flask_login import LoginManager, login_user, login_required, current_user, logout_user 
from werkzeug.security import generate_password_hash

auth = Blueprint('auth', __name__)

#define login
@auth.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        from .models import User
        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                login_user(user)
                return redirect(url_for('profile'))
        else:
            return "Invalid Email or Password"
    
    return render_template('login.html')

#define logout
@auth.route('/logout')
def logout():
    logout_user()
    return render_template('home.html')


#define sign up
@auth.route("/sign-up", methods = ['GET','POST'])
def sign_up():
    #Get submissions from signup post
    if request.method == 'POST':
        from .models import User
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        new_user = User(firstName=firstName, email = email, password1 = password1, password2 = password2 )

        #sign up post restrictions
        if len(email) < 4:
            flash ("Email must be more than 4 characters long", category = 'error')
        elif len(firstName) < 2:
            flash ('first name must be more than 2 characters long', category = 'error')
        elif password1 != password2:
            flash ('password must be the same', category = 'error')
        elif len(password1) < 6:
            flash ('password cannot be less than 6 characters', category = 'error')
        else:
            #add user to database
            from . import User
            new_user = User(email=email, firstName=firstName, password=generate_password_hash(password1, method='sha256'))
            from . import db
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash ('Account created', category = 'success')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html')

