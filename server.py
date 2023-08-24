"""Server for weight monitoring website"""
from flask import (Flask, render_template, request, flash, session,
                   redirect)
#Model has our class files for User,Calorie, and Weight
from model import connect_to_db, db
from jinja2 import StrictUndefined
#Scripts for reading and updating the database
import crud

app = Flask(__name__)
app.secret_key = "SuperSecret"
app.jinja_env.undefined = StrictUndefined

#Display the homepage when going to the index
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template("about.html")



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)