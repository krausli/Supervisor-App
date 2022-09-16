#import modules
from os import path
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, current_user, logout_user, UserMixin
from sqlalchemy.sql import func


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    from .models import User
    #db = SQLAlchemy()
    Authe = "authe.db"
    #secure cookies data
    app.config['SECRET_KEY'] = 'lolo'
    app.config ["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///tmp/authe.db'

    #initialise database
    db.init_app(app)

    #import routes 
    from .views import views
    from .auth import auth
    #blueprint
    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(auth, url_prefix = "/")

    #Set up loginmanager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "login"
    
    #def create_database(app)
    def create_database(app):
        if not path.exists('/' + Authe):
                db.create_all(app=app)
                print('Database created')

    #Create User Loader
    #from .models import User
    #login_manager = LoginManager()
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app

 
#define user permissions
#class Controller(UserMixin, db.Model):
    #id = db.Column(db.Integer, primary_key = True)
    #username = db.Column(db.String(20), unique = True, nullable = False)
    #email = db.Column(db.String(120), unique = True, nullable = False)
    #password = db.Column(db.String(60), nullable = False)
    #date_created = db.Column(db.DateTime(timezone = True), default = func.now())
    #define user permissions
    #def __repr__(self):
        #return f"User('{self.username}', '{self.email}', '{self.date_created}')"

