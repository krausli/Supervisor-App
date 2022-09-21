from flask import Flask, Request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField, RadioField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename

class Professional(FlaskForm):
    title = BooleanField("1.1 Aware of and complies with current legislation relevant to the role")
    choices = RadioField('Label', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    comments = TextAreaField('Comments')
    evidence = TextAreaField('Evidence', validators=[DataRequired()])
    actions = TextAreaField('Actions', validators=[DataRequired()])
    title2 = BooleanField("1.2 1.2 Aware of and complies with organisation requirements")
    choices2 = RadioField('Label', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    comments2 = TextAreaField('Comments')
    evidence2 = TextAreaField('Evidence', validators=[DataRequired()])
    actions2 = TextAreaField('Actions', validators=[DataRequired()])
    title3 = BooleanField("1.3 Relevant professional learning completed")
    choices3 = RadioField('Label', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    comments3 = TextAreaField('Comments')
    evidence3 = TextAreaField('Evidence', validators=[DataRequired()])
    actions3 = TextAreaField('Actions', validators=[DataRequired()])
    title4 = BooleanField("1.4 Safe Workplace health and safety practices")
    choices4 = RadioField('Label', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    comments4 = TextAreaField('Comments')
    evidence4 = TextAreaField('Evidence', validators=[DataRequired()])
    actions4 = TextAreaField('Actions', validators=[DataRequired()])
    submit = SubmitField('Confirm')
    

class Supervision(FlaskForm):
    title = BooleanField("2.1 Contributes to safe activities and environment for all boarders.")
    choices = RadioField('Label', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    comments = TextAreaField('Comments')
    evidence = TextAreaField('Evidence', validators=[DataRequired()])
    actions = TextAreaField('Actions', validators=[DataRequired()])
    title2 = BooleanField("2.2 Has respectful professional relationships with all boarders.")
    choices2 = RadioField('Label', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    comments2 = TextAreaField('Comments')
    evidence2 = TextAreaField('Evidence', validators=[DataRequired()])
    actions2 = TextAreaField('Actions', validators=[DataRequired()])
    title3 = BooleanField("2.3 Supervises boarders effectively, supporting and meeting needs")
    choices3 = RadioField('Label', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    comments3 = TextAreaField('Comments')
    evidence3 = TextAreaField('Evidence', validators=[DataRequired()])
    actions3 = TextAreaField('Actions', validators=[DataRequired()])
    title4 = BooleanField("2.4 Facilitates positive boarder behaviours")
    choices4 = RadioField('Label', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    comments4 = TextAreaField('Comments')
    evidence4 = TextAreaField('Evidence', validators=[DataRequired()])
    actions4 = TextAreaField('Actions', validators=[DataRequired()])
    title5 = BooleanField("2.5 Provides sensitive appropriate cultural support")
    choices5 = RadioField('Label', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    comments5 = TextAreaField('Comments')
    evidence5 = TextAreaField('Evidence', validators=[DataRequired()])
    actions5 = TextAreaField('Actions', validators=[DataRequired()])
    submit = SubmitField('Confirm')

class Team(FlaskForm):
    title = BooleanField("1.1 Aware of and complies with current legislation relevant to the role")
    choices = RadioField('Label', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    comments = TextAreaField('Comments')
    evidence = TextAreaField('Evidence', validators=[DataRequired()])
    actions = TextAreaField('Actions', validators=[DataRequired()])
    title2 = BooleanField("1.2 1.2 Aware of and complies with organisation requirements")
    choices2 = RadioField('Label', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    comments2 = TextAreaField('Comments')
    evidence2 = TextAreaField('Evidence', validators=[DataRequired()])
    actions2 = TextAreaField('Actions', validators=[DataRequired()])
    title3 = BooleanField("1.3 Relevant professional learning completed")
    choices3 = RadioField('Label', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    comments3 = TextAreaField('Comments')
    evidence3 = TextAreaField('Evidence', validators=[DataRequired()])
    actions3 = TextAreaField('Actions', validators=[DataRequired()])
    submit = SubmitField('Confirm')
    
class Administration(FlaskForm):
    title = BooleanField("1.1 Aware of and complies with current legislation relevant to the role", validators=[DataRequired()])
    choices = RadioField('Label', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[DataRequired()])
    comments = TextAreaField('Comments', validators=[DataRequired()])
    evidence = TextAreaField('Evidence', validators=[DataRequired()])
    actions = TextAreaField('Actions', validators=[DataRequired()])
    title2 = BooleanField("1.2 1.2 Aware of and complies with organisation requirements", validators=[DataRequired()])
    choices2 = RadioField('Label', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[DataRequired()])
    comments2 = TextAreaField('Comments', validators=[DataRequired()])
    evidence2 = TextAreaField('Evidence', validators=[DataRequired()])
    actions2 = TextAreaField('Actions', validators=[DataRequired()])
    submit = SubmitField('submit')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    

class UploadForm(FlaskForm):
    file = FileField('Appraisal matrix', validators=[
        FileRequired(),
        FileAllowed('pdf', 'Upload supervisor appraisal matrix')
    ])
    filename = StringField('Filename')
    submit = SubmitField('Upload')