#import modules
from flask_login import UserMixin
from sqlalchemy.sql import func

#define User table
from .__init__ import db
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    firstName = db.Column(db.String(255))
    
