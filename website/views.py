#import modules
import os.path
from flask import Blueprint, render_template, jsonify, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
#from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from flask_mail import Mail, Message
#from flask_uploads import UploadSet, configure_uploads, IMAGES
#set up Blueprint
views = Blueprint('views', __name__)

from .models import db, User, Questionnaire, Sections, Questions, SubQuestions1, SubQuestions2, SubQuestions3, SubQuestions4, Files
from .forms import Professional, Administration, Supervision, Team, UploadForm
from . import mail
#define home page 
@views.route("/")
def home():
    return render_template("home.html")

#define profile page 
@views.route("/profile")
#@login_required
def profile():
    return render_template("profile.html")

#define unprotected page
@views.route("/unprotected")
def unprotect():
    return "Unprotected Page"

#define start-up page 
@views.route("/start-up")
def start_up():
    return render_template("start_up.html")


# #define saved reviews page 
@views.route("/saved-reviews")
def saved_reviews():
    # posts = Reviews.query.all()
    return render_template('saved_reviews.html')
    

#define professional practice page 
@views.route("/professional-practice", methods = ['GET','POST'])
def profprac():
    form = Professional()
    if form.validate_on_submit():
        response = SubQuestions1()
        form.populate_obj(response)
        db.session.add(response)
        db.session.commit()
        flash ('Your response has been saved')
        return redirect('/professional-practice')
    return render_template("professional_practice.html", form = form)

#define supervision practice page 
@views.route("/supervision-practice", methods = ['GET','POST'])
def superprac():
    form = Supervision()
    if form.validate_on_submit():
        response = SubQuestions2()
        form.populate_obj(response)
        db.session.add(response)
        db.session.commit()
        flash('Your response has been saved.')
        return redirect('/supervision-practice')
    return render_template("supervision_practice.html", form = form)

#define team practice page 
@views.route("/team-practice", methods = ['GET','POST'])
def teamprac():
    form = Team()
    if form.validate_on_submit():
        response = SubQuestions3()
        form.populate_obj(response)
        db.session.add(response)
        db.session.commit()
        flash ('Your response has been saved')
        return redirect('/team-practice')
    return render_template("team_practice.html", form = form)

#define administration practice page 
@views.route("/administration-practice", methods = ['GET','POST'] )
def adminprac():
    form = Administration()
    if form.validate_on_submit():
        response = SubQuestions4()
        form.populate_obj(response)
        db.session.add(response)
        db.session.commit()
        flash ('Your response has been saved')
    return render_template("administration_practice.html", form = form)   

#define redirect-to-home route
@views.route("/direct_home")
def direct_home():
    return redirect(url_for("views.home"))

#define file upload page
@views.route("/upload", methods = ['GET','POST'])
def file_upload():
    form = UploadForm()
    if form.validate_on_submit():
        file = Files()
        form.populate_obj(file)
        db.session.add(file)
        db.session.commit()
        flash ('Your file has been uploaded')
        return redirect(('saved_reviews'))
    return render_template("upload.html", form = form)

#define email reminder page
@views.route("/email")
def reminder():
    msg = Message("Hello",
                  sender="from@example.com",
                  recipients=["to@example.com"])
    msg.body = "Hi, this is a reminder to complete your review"
    msg.html = "<b>reminder</b>"
    mail.send(msg)


#define appraisal matrix page 
@views.route("/create-appraisal")
def matrix():
    return render_template("supervisor_practice.html")

