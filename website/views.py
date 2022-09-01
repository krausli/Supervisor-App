#import modules
from flask import Blueprint, render_template, jsonify, redirect, url_for
#set up Blueprint
views = Blueprint('views', __name__)

#define home page 
@views.route("/")
def home():
    return render_template("home.html")

#define profile page 
@views.route("/profile")
def profile():
    return render_template("profile.html")

#define appraisal matrix page 
@views.route("/create-appraisal")
def matrix():
    return render_template("matrix.html")

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

#define redirect-to-home route
@views.route("/direct_home")
def direct_home():
    return redirect(url_for("views.home"))


