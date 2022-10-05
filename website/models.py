#import modules
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from datetime import datetime
from sqlalchemy import PrimaryKeyConstraint, ForeignKeyConstraint, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


#import db
from . import db
#define User table
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    image_file = db.Column(db.String(255), nullable=False, default='default.jpg')
    position = db.Column(db.String(255))
    reviews = db.relationship('Survey', backref='author', lazy=True)
    is_approved = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_manager = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.image_file}')"

#Define school table
class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(255), nullable=False)
      
#Define Administrator Table
class SuperUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admin_name = db.Column(db.String(255), nullable=False)
    admin_email = db.Column(db.String(255), nullable=False)
    admin_phone = db.Column(db.String(255), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    
#Define Manager table
class Manager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    school = db.relationship('School', backref=db.backref('managers', lazy=True))
    
    def __repr__(self):
        return f"Manager('{self.name}', '{self.email}', '{self.phone}')"

#Define Supervisor table with school and manager as foreign keys
class Supervisor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey('manager.id'), nullable=False)
    school = db.relationship('School', backref=db.backref('supervisors', lazy=True))
    manager = db.relationship('Manager', backref=db.backref('supervisors', lazy=True))
    
    def __repr__(self):
        return f"Supervisor('{self.name}', '{self.email}', '{self.phone}')"


#Define Subsciption table
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subscription_name = db.Column(db.String(255), nullable=False)
    subscription_price = db.Column(db.String(255), nullable=False)
    subscription_duration = db.Column(db.String(255), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    school = db.relationship('School', backref=db.backref('subscriptions', lazy=True))
    
    def __repr__(self):
        return f"Subscription('{self.subscription_name}', '{self.subscription_price}', '{self.subscription_duration}')"

#define Order Table
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_name = db.Column(db.String(255), nullable=False)
    order_price = db.Column(db.String(255), nullable=False)
    order_duration = db.Column(db.String(255), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    school = db.relationship('School', backref=db.backref('orders', lazy=True))
    
    def __repr__(self):
        return f"Order('{self.order_name}', '{self.order_price}', '{self.order_duration}')"

#define subscription by order table
class SubscriptionByOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subscription_id = db.Column(db.Integer, db.ForeignKey('subscription.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    subscription = db.relationship('Subscription', backref=db.backref('subscription_by_order', lazy=True))
    order = db.relationship('Order', backref=db.backref('subscription_by_order', lazy=True))
    
    def __repr__(self):
        return f"SubscriptionByOrder('{self.subscription_id}', '{self.order_id}')"


# #define reviews table
# class Reviews(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
#     title = db.Column(db.String(100))
#     document_file = db.Column(db.String(255))
#     survey = db.relationship('Survey', backref='review', lazy=True)
#     def __repr__(self):
#         return f"Reviews('{self.title}', '{self.date}')"


#Define survey table
class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_posted = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    title = db.Column(db.String(100))
    document_file = db.Column(db.String(255))
    choices = db.Column(db.String(255))
    comments = db.Column(db.String(255))
    evidence = db.Column(db.String(255))
    actions = db.Column(db.String(255))
    date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    choices2 = db.Column(db.String(255))
    comments2 = db.Column(db.String(255))
    evidence2 = db.Column(db.String(255))
    actions2 = db.Column(db.String(255))
    date2 = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    choices3 = db.Column(db.String(255))
    comments3 = db.Column(db.String(255))
    evidence3 = db.Column(db.String(255))
    actions3 = db.Column(db.String(255))
    date3 = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    choices4 = db.Column(db.String(255))
    comments4 = db.Column(db.String(255))
    evidence4 = db.Column(db.String(255))
    actions4 = db.Column(db.String(255))
    date4 = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    choices5 = db.Column(db.String(255))
    comments5 = db.Column(db.String(255))
    evidence5 = db.Column(db.String(255))
    actions5 = db.Column(db.String(255))
    date5 = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    choices6 = db.Column(db.String(255))
    comments6 = db.Column(db.String(255))
    evidence6 = db.Column(db.String(255))
    actions6 = db.Column(db.String(255))
    date6 = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    choices7 = db.Column(db.String(255))
    comments7 = db.Column(db.String(255))
    evidence7 = db.Column(db.String(255))
    actions7 = db.Column(db.String(255))
    date7 = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    choices8 = db.Column(db.String(255))
    comments8 = db.Column(db.String(255))
    evidence8 = db.Column(db.String(255))
    actions8 = db.Column(db.String(255))
    date8 = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    choices9 = db.Column(db.String(255))
    comments9 = db.Column(db.String(255))
    evidence9 = db.Column(db.String(255))
    actions9 = db.Column(db.String(255))
    date9 = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    choices10 = db.Column(db.String(255))
    comments10 = db.Column(db.String(255))
    evidence10 = db.Column(db.String(255))
    actions10 = db.Column(db.String(255))
    date10 = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    choices11 = db.Column(db.String(255))
    comments11 = db.Column(db.String(255))
    evidence11 = db.Column(db.String(255))
    actions11 = db.Column(db.String(255))
    date11 = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    choices12 = db.Column(db.String(255))
    comments12 = db.Column(db.String(255))
    evidence12 = db.Column(db.String(255))
    actions12 = db.Column(db.String(255))
    date12 = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    choices13 = db.Column(db.String(255))
    comments13 = db.Column(db.String(255))
    evidence13 = db.Column(db.String(255))
    actions13 = db.Column(db.String(255))
    date13 = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    choices14 = db.Column(db.String(255))
    comments14 = db.Column(db.String(255))
    evidence14 = db.Column(db.String(255))
    actions14 = db.Column(db.String(255))

    def __repr__(self):
        return f"Survey('{self.id}', '{self.date_posted}', '{self.title}', '{self.document_file}')"



# #define Questionnaire table
# class Questionnaire(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date = db.Column(db.DateTime(timezone=True), default=func.now())
#     user_id = db.Column(db.Integer)
#     review_id = db.Column(db.Integer)
#     title = db.Column(db.String)
#     ForeignKeyConstraint(
#                 ['user_id', 'review_id'],
#                 ['user.id', 'reviews.id'],
#                 onupdate="CASCADE", ondelete="SET NULL"
#     )
        
# #define survey sections
# class Sections(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'))
#     title = db.Column(db.String(100))
#     def __repr__(self):
#         return f'<SurveySections "{self.title}">'

# #define survey questions 
# class Questions(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100))
#     questionnaire_id = db.Column(db.Integer)
#     section_id = db.Column(db.Integer)
#     ForeignKeyConstraint(
#                 ['questionnaire_id', 'section_id'],
#                 ['questionnaire.id', 'sections.id'],
#                 onupdate="CASCADE", ondelete="SET NULL"
#     )
#     def __repr__(self):
#         return f'<SurveyQuestions "{self.title}">'


# #define survey sub-questions1
# class SubQuestions1(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String(100))
#     questionnaire_id = db.Column(db.Integer)
#     section_id = db.Column(db.Integer)
#     question_id = db.Column(db.Integer)
#     choices = db.Column(db.String(255))
#     comments = db.Column(db.String(255))
#     evidence = db.Column(db.String(255))
#     actions = db.Column(db.String(255))
#     choices2 = db.Column(db.String(255))
#     comments2 = db.Column(db.String(255))
#     evidence2 = db.Column(db.String(255))
#     actions2 = db.Column(db.String(255))
#     choices3 = db.Column(db.String(255))
#     comments3 = db.Column(db.String(255))
#     evidence3 = db.Column(db.String(255))
#     actions3 = db.Column(db.String(255))
#     choices4 = db.Column(db.String(255))
#     comments4 = db.Column(db.String(255))
#     evidence4 = db.Column(db.String(255))
#     actions4 = db.Column(db.String(255))
#     ForeignKeyConstraint(
#                 ['questionnaire_id', 'section_id', 'question_id'],
#                 ['questionnaire.id', 'sections.id', 'questions.id'],
#                 onupdate="CASCADE", ondelete="SET NULL"
#     )
#     def __repr__(self):
#         return f'<SurveySubQuestions "{self.text}">'

# # #define survey sub-questions2
# class SubQuestions2(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String(100))
#     questionnaire_id = db.Column(db.Integer)
#     section_id = db.Column(db.Integer)
#     question_id = db.Column(db.Integer)
#     choices = db.Column(db.String(255))
#     comments = db.Column(db.String(255))
#     evidence = db.Column(db.String(255))
#     actions = db.Column(db.String(255))
#     choices2 = db.Column(db.String(255))
#     comments2 = db.Column(db.String(255))
#     evidence2 = db.Column(db.String(255))
#     actions2 = db.Column(db.String(255))
#     choices3 = db.Column(db.String(255))
#     comments3 = db.Column(db.String(255))
#     evidence3 = db.Column(db.String(255))
#     actions3 = db.Column(db.String(255))
#     choices4 = db.Column(db.String(255))
#     comments4 = db.Column(db.String(255))
#     evidence4 = db.Column(db.String(255))
#     actions4 = db.Column(db.String(255))
#     choices5 = db.Column(db.String(255))
#     comments5 = db.Column(db.String(255))
#     evidence5 = db.Column(db.String(255))
#     actions5 = db.Column(db.String(255))
#     ForeignKeyConstraint(
#                 ['questionnaire_id', 'section_id', 'question_id'],
#                 ['questionnaire.id', 'sections.id', 'questions.id'],
#                 onupdate="CASCADE", ondelete="SET NULL"
#     )
#     def __repr__(self):
#         return f'<SurveySubQuestions "{self.text}">'

# # #define survey sub-questions3
# class SubQuestions3(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String(100))
#     questionnaire_id = db.Column(db.Integer)
#     section_id = db.Column(db.Integer)
#     question_id = db.Column(db.Integer)
#     choices = db.Column(db.String(255))
#     comments = db.Column(db.String(255))
#     evidence = db.Column(db.String(255))
#     actions = db.Column(db.String(255))
#     choices2 = db.Column(db.String(255))
#     comments2 = db.Column(db.String(255))
#     evidence2 = db.Column(db.String(255))
#     actions2 = db.Column(db.String(255))
#     choices3 = db.Column(db.String(255))
#     comments3 = db.Column(db.String(255))
#     evidence3 = db.Column(db.String(255))
#     actions3 = db.Column(db.String(255))
#     ForeignKeyConstraint(
#                 ['questionnaire_id', 'section_id', 'question_id'],
#                 ['questionnaire.id', 'sections.id', 'questions.id'],
#                 onupdate="CASCADE", ondelete="SET NULL"
#     )
#     def __repr__(self):
#         return f'<SurveySubQuestions "{self.text}">'

# # #define survey sub-questions4
# class SubQuestions4(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String(100))
#     questionnaire_id = db.Column(db.Integer)
#     section_id = db.Column(db.Integer)
#     question_id = db.Column(db.Integer)
#     choices = db.Column(db.String(255))
#     comments = db.Column(db.String(255))
#     evidence = db.Column(db.String(255))
#     actions = db.Column(db.String(255))
#     choices2 = db.Column(db.String(255))
#     comments2 = db.Column(db.String(255))
#     evidence2 = db.Column(db.String(255))
#     actions2 = db.Column(db.String(255))
#     ForeignKeyConstraint(
#                 ['questionnaire_id', 'section_id', 'question_id'],
#                 ['questionnaire.id', 'sections.id', 'questions.id'],
#                 onupdate="CASCADE", ondelete="SET NULL"
#     )
#     def __repr__(self):
#         return f'<SurveySubQuestions "{self.text}">'


#define Files Tables
class Files(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255))
    file = db.Column(db.LargeBinary)
    user_id = db.Column(db.Integer)
    review_id = db.Column(db.Integer)
    ForeignKeyConstraint(
                ['user_id', 'review_id'],
                ['user.id', 'reviews.id'],
    )
    def __repr__(self):
        return f'<Files "{self.filename}">'

# Define datefield table * (For reminders) Change this one
class DateField(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer)
    review_id = db.Column(db.Integer)
    ForeignKeyConstraint(
                ['user_id', 'review_id'],
                ['user.id', 'reviews.id'],
    )
    def __repr__(self):
        return f'<DateField "{self.date}">'