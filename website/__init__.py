#import modules
import os
import secrets
from os import path
from flask import Flask, abort, Blueprint, render_template, request, flash, redirect, url_for, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, current_user, logout_user, UserMixin
from flask_wtf.file import FileField, FileRequired, FileAllowed
from sqlalchemy.sql import func, select
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_mail import Mail




app = Flask(__name__)
db = SQLAlchemy(app)
views = Blueprint('views', __name__)
mail = Mail(app)

from .models import User, Files, Survey, Subscription
from .forms import StartUpForm, UploadForm, EditProfileForm,  StartUpForm
from . import mail

def create_app():
    #app = Flask(__name__)
    
    #db = SQLAlchemy()
    basedir = os.path.abspath(os.path.dirname(__file__))

    Authe = "authe.db"
    #secure cookies data
    app.config['SECRET_KEY'] = 'lolo'
    app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'authe.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #set up admin
    admin = Admin(app, name='control panel', template_mode='bootstrap3')
    #initialise database
    #db.init_app(app)

    #Create Class controller * change this
    class Controller(ModelView):
        def is_accessible(self):
            if current_user.is_admin == True:
                return current_user.is_authenticated
            else:
                return abort(404)
            #return current_user.is_authenticated
        def not_auth(self):
            return "You are not authorised to view this page"

            
    #create admin view
    admin.add_view(Controller(User, db.session))
    
    #Set up loginmanager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "login"
    login_manager.login_message_category = "info"

    
    #import routes
    from .views import views
    from .auth import auth

    #Create yearly product subscription function
    # def yearly_subscription():
    #     if request.method == "POST":
    #         # form = 
    #         #import subcription
            
    #         if subscription_name == "a":
    #             price = "100"
    #         elif subscription_name == "b":
    #             price = "100"
    #         elif subcription_name == "c":
    #             price = "100"
            # productid = request.form.get("email")
            # new_subscription = Subscription(email=email)
            #Create time-based subscription requirements
            #subscription_date = Subscription.data
            # new_subscription.date = func.now() + func.interval(1, 'year')
            

            # db.session.add(new_subscription)
            # db.session.commit()
        #     flash("You have ", category="success")
        #     return redirect(url_for("views.home"))
        # return render_template("home.html", user=current_user)

    #def create_database(app)
    if not path.exists('/' + Authe):
            db.create_all(app=app)
            print('Database created')

    #set up email
    app.config['MAIL_SERVER']='smtp.gmail.com' #127.0.0.1
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = None
    app.config['MAIL_PASSWORD'] = None
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = False
    #mail = Mail(app)

    

    #initialise database
    # db.init_app(app)

    #blueprint
    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(auth, url_prefix = "/")

    



    #Create User Loader
    #login_manager = LoginManager()
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app

 
