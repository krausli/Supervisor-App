#import modules
import os
from os import path
from flask import Flask, abort, Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, current_user, logout_user, UserMixin
from sqlalchemy.sql import func, select
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_mail import Mail




app = Flask(__name__)
db = SQLAlchemy(app)
views = Blueprint('views', __name__)
mail = Mail(app)


def create_app():
    #app = Flask(__name__)
    
    #db = SQLAlchemy()
    
    Authe = "authe.db"
    #secure cookies data
    app.config['SECRET_KEY'] = 'lolo'
    app.config ["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///tmp/authe.db'

    from .models import User

    #import routes
    from .views import views
    from .auth import auth

    #set up email
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = None
    app.config['MAIL_PASSWORD'] = None
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    #mail = Mail(app)

    #set up admin
    admin = Admin(app, name='control panel', template_mode='bootstrap3')

    #initialise database
    # db.init_app(app)

    #blueprint
    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(auth, url_prefix = "/")

    #Set up loginmanager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "login"

    #from . import models
    User()

    #Create Class controller
    class Controller(ModelView):
        def is_accessible(self):
            if current_user.is_admin == True:
                return current_user.is_authenticated
            else:
                return abort(404)
            return current_user.is_authenticated
        def not_auth(self):
            return "You are not authorised to view this page"

    #create admin view
    admin.add_view(Controller(User, db.session))
    
    #def create_database(app)
    
    if not path.exists('/' + Authe):
            db.create_all(app=app)
            print('Database created')

    #Create User Loader
    #login_manager = LoginManager()
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app

 
