from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

#define login
@auth.route('/login')
def login():
    return render_template('login.html')

#define logout
@auth.route('/logout')
def logout():
    return "<h1>You have logged out</h1>"

#define sign up
@auth.route("/sign-up")
def sign_up():
    return render_template('sign_up.html')

