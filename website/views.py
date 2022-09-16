#import modules
from flask import Blueprint, render_template, jsonify, redirect, url_for
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
#set up Blueprint
views = Blueprint('views', __name__)

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

#define saved reviews page 
@views.route("/saved-reviews")
def saved_reviews():
    return render_template("saved_reviews.html")


#define matrix page
#@views.route("/data")
#def get_data():
    #data = request.json
    #return jsonify(data)

#define professional practice page 
@views.route("/professional-practice", methods = ['GET','POST'])
def profprac():
    return render_template("professional_practice.html")

#define supervision practice page 
@views.route("/supervision-practice", methods = ['GET','POST'])
def superprac():
    return render_template("supervision_practice.html")

#define team practice page 
@views.route("/team-practice", methods = ['GET','POST'])
def teamprac():
    return render_template("team_practice.html")

#define administration practice page 
@views.route("/administration-practice", methods = ['GET','POST'] )
def adminprac():
    return render_template("administration_practice.html")   

#define redirect-to-home route
@views.route("/direct_home")
def direct_home():
    return redirect(url_for("views.home"))

#define appraisal matrix page 
@views.route("/create-appraisal")
def matrix():
    return render_template("supervisor_practice.html")

