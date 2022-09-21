#import modules
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from datetime import datetime
from sqlalchemy import PrimaryKeyConstraint, ForeignKeyConstraint


#define User table
from . import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    firstName = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean, default=False)
    is_manager = db.Column(db.Boolean, default=False)

#define reviews table
class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    title = db.Column(db.String(100))
    #content = db.relationship('Questionnaire', backref='reviews')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return f'<Reviews "{self.title}">'

#define Questionnaire table
class Questionnaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer)
    review_id = db.Column(db.Integer)
    title = db.Column(db.String)
    ForeignKeyConstraint(
                ['user_id', 'review_id'],
                ['user.id', 'reviews.id'],
                onupdate="CASCADE", ondelete="SET NULL"
    )
        
#define survey sections
class Sections(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'))
    title = db.Column(db.String(100))
    def __repr__(self):
        return f'<SurveySections "{self.title}">'

#define survey questions 
class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    questionnaire_id = db.Column(db.Integer)
    section_id = db.Column(db.Integer)
    ForeignKeyConstraint(
                ['questionnaire_id', 'section_id'],
                ['questionnaire.id', 'sections.id'],
                onupdate="CASCADE", ondelete="SET NULL"
    )
    def __repr__(self):
        return f'<SurveyQuestions "{self.title}">'


# #define survey sub-questions1
class SubQuestions1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100))
    questionnaire_id = db.Column(db.Integer)
    section_id = db.Column(db.Integer)
    question_id = db.Column(db.Integer)
    choices = db.Column(db.String(255))
    comments = db.Column(db.String(255))
    evidence = db.Column(db.String(255))
    actions = db.Column(db.String(255))
    choices2 = db.Column(db.String(255))
    comments2 = db.Column(db.String(255))
    evidence2 = db.Column(db.String(255))
    actions2 = db.Column(db.String(255))
    choices3 = db.Column(db.String(255))
    comments3 = db.Column(db.String(255))
    evidence3 = db.Column(db.String(255))
    actions3 = db.Column(db.String(255))
    choices4 = db.Column(db.String(255))
    comments4 = db.Column(db.String(255))
    evidence4 = db.Column(db.String(255))
    actions4 = db.Column(db.String(255))
    ForeignKeyConstraint(
                ['questionnaire_id', 'section_id', 'question_id'],
                ['questionnaire.id', 'sections.id', 'questions.id'],
                onupdate="CASCADE", ondelete="SET NULL"
    )
    def __repr__(self):
        return f'<SurveySubQuestions "{self.text}">'

# #define survey sub-questions2
class SubQuestions2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100))
    questionnaire_id = db.Column(db.Integer)
    section_id = db.Column(db.Integer)
    question_id = db.Column(db.Integer)
    choices = db.Column(db.String(255))
    comments = db.Column(db.String(255))
    evidence = db.Column(db.String(255))
    actions = db.Column(db.String(255))
    choices2 = db.Column(db.String(255))
    comments2 = db.Column(db.String(255))
    evidence2 = db.Column(db.String(255))
    actions2 = db.Column(db.String(255))
    choices3 = db.Column(db.String(255))
    comments3 = db.Column(db.String(255))
    evidence3 = db.Column(db.String(255))
    actions3 = db.Column(db.String(255))
    choices4 = db.Column(db.String(255))
    comments4 = db.Column(db.String(255))
    evidence4 = db.Column(db.String(255))
    actions4 = db.Column(db.String(255))
    choices5 = db.Column(db.String(255))
    comments5 = db.Column(db.String(255))
    evidence5 = db.Column(db.String(255))
    actions5 = db.Column(db.String(255))
    ForeignKeyConstraint(
                ['questionnaire_id', 'section_id', 'question_id'],
                ['questionnaire.id', 'sections.id', 'questions.id'],
                onupdate="CASCADE", ondelete="SET NULL"
    )
    def __repr__(self):
        return f'<SurveySubQuestions "{self.text}">'

# #define survey sub-questions3
class SubQuestions3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100))
    questionnaire_id = db.Column(db.Integer)
    section_id = db.Column(db.Integer)
    question_id = db.Column(db.Integer)
    choices = db.Column(db.String(255))
    comments = db.Column(db.String(255))
    evidence = db.Column(db.String(255))
    actions = db.Column(db.String(255))
    choices2 = db.Column(db.String(255))
    comments2 = db.Column(db.String(255))
    evidence2 = db.Column(db.String(255))
    actions2 = db.Column(db.String(255))
    choices3 = db.Column(db.String(255))
    comments3 = db.Column(db.String(255))
    evidence3 = db.Column(db.String(255))
    actions3 = db.Column(db.String(255))
    ForeignKeyConstraint(
                ['questionnaire_id', 'section_id', 'question_id'],
                ['questionnaire.id', 'sections.id', 'questions.id'],
                onupdate="CASCADE", ondelete="SET NULL"
    )
    def __repr__(self):
        return f'<SurveySubQuestions "{self.text}">'

# #define survey sub-questions4
class SubQuestions4(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100))
    questionnaire_id = db.Column(db.Integer)
    section_id = db.Column(db.Integer)
    question_id = db.Column(db.Integer)
    choices = db.Column(db.String(255))
    comments = db.Column(db.String(255))
    evidence = db.Column(db.String(255))
    actions = db.Column(db.String(255))
    choices2 = db.Column(db.String(255))
    comments2 = db.Column(db.String(255))
    evidence2 = db.Column(db.String(255))
    actions2 = db.Column(db.String(255))
    ForeignKeyConstraint(
                ['questionnaire_id', 'section_id', 'question_id'],
                ['questionnaire.id', 'sections.id', 'questions.id'],
                onupdate="CASCADE", ondelete="SET NULL"
    )
    def __repr__(self):
        return f'<SurveySubQuestions "{self.text}">'


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