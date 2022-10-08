#import modules
from cgitb import enable
from importlib.metadata import MetadataPathFinder
import os
import secrets
from os import path
from flask import Flask, abort, Blueprint, render_template, request, flash, redirect, url_for, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, current_user, logout_user, UserMixin
from flask_wtf.file import FileField, FileRequired, FileAllowed
from sqlalchemy import inspect, create_engine
from sqlalchemy.sql import func, select
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_migrate import Migrate




app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://ops:ops2022@127.0.0.1/ops'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
views = Blueprint('views', __name__)
mail = Mail(app)

from .models import SubscriptionByOrder, User, Files, Survey, Subscription
from .forms import UploadForm, EditProfileForm
from . import mail

def create_app():
    #app = Flask(__name__)
    
    #directory for sqlite
    basedir = os.path.abspath(os.path.dirname(__file__))

    #initialise database
    # db.init_app(app)

    #secure cookies data
    app.config['SECRET_KEY'] = 'lolo'
    # app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://ops:ops2022@127.0.0.1/ops'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #set up admin
    admin = Admin(app, name='control panel', template_mode='bootstrap3')
    #initialise database
    #db.init_app(app)

    #Create Class controller view  * change this
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

    #Import models
    from .models import School

    
    #import routes
    from .views import views
    from .auth import auth

        

    #def create_database(app) 
    #Find string in an array
    engine = create_engine('mysql://ops:ops2022@127.0.0.1/ops')
    insp = inspect(engine)
    table_names = insp.get_table_names()
    # if True == False:## FIXME: need condition to see if 'subscription' is an element of table_names
    if 'subscription' not in table_names:
        db.create_all(app=app)
        in_school = School(school_name = "UniOlly")
        db.session.add(in_school)
        db.session.commit()
        print('Database created')

          #if not engine.has_table(engine, 'subscription'):  #to test if a database exists
         #metadata = MetadataPathFinder(engine) 
           #ops.create(engine, checkfirst=True)
           #Table('subscription', metadata)
           #     Column('Id', Integer, primary_key=True, nullable=False),
           #     Column('First Name', varchar, nullable=False),
           #     Column('Last Name', varchar, nullable=False),
           #     Column('EmailID', varchar, nullable=False),
           #     Column('School Name', varchar, nullable=False),
           #     Column('Phone Number', integer, nullable=False)
           #if not database_exists(engine.url):
    #create_database(engine.url)
#else:
    #engine.connect()

    #set up email
    # app.config['MAIL_SERVER']='smtp.gmail.com' #127.0.0.1
    # app.config['MAIL_PORT'] = 465
    # app.config['MAIL_USERNAME'] = None
    # app.config['MAIL_PASSWORD'] = None
    # app.config['MAIL_USE_TLS'] = False
    # app.config['MAIL_USE_SSL'] = False
    # mail = Mail(app)

    app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
    app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
    mail = Mail(app)

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

 
