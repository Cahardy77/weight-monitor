"""Server for weight monitoring website"""
from flask import (Flask, render_template, request, session, redirect, flash)
from sqlalchemy import text
#Model has our class files for User,Calorie, and Weight
from model import connect_to_db, db
from jinja2 import StrictUndefined
#Scripts for reading and updating the database
import crud
#Having issues with datetime from database, importing to striptime?
from datetime import datetime

app = Flask(__name__)
app.secret_key = "SuperSecret"
app.jinja_env.undefined = StrictUndefined

#Display the homepage when going to the index
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_database():
    email = request.form.get("email")
    password = request.form.get("password")
    if crud.check_password_by_email(email, password) :
        user = crud.get_user_by_email(email)
        session["email"] = user.email
        return redirect("/profile")
    else:
        flash("Invalid Login")
        return redirect("/login")
    
        

@app.route("/register", methods=["GET"])
def register_new_user():
    return render_template("/register.html")

@app.route("/register", methods=["POST"])
def register_database():
    email = request.form.get("email")
    password = request.form.get("password")
    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    birth_date = request.form.get("birth")
    if crud.get_user_by_email(email) :
        flash("User email already exists!")
        return redirect("/register")
    else:
        new_user = crud.create_user(email, password, first_name, last_name, birth_date)
        db.session.add(new_user)
        db.session.commit()
        flash(f"Thank you and welcome, {new_user.fname}!")
        return redirect("/")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/profile")
def show_user():
    """Show details on a particular user."""
    if session["email"]: #try:
        session["email"]
        email = session["email"]
        user = crud.get_user_by_email(email)
        weights = crud.get_weights_by_email(email)

        weights_list = []
        weight_dates_list = []
        for weight in weights:
            weights_list.append(weight.weight)
            weight_dates_list.append(f"{weight.date.month}/{weight.date.day}/{weight.date.year}")

        calories = crud.get_calories_by_email(email)
        calories_list = []
        calories_dates_list = []
        for calorie in calories:
            calories_list.append(calorie.calories)
            calories_dates_list.append(f"{calorie.date.month}/{calorie.date.day}/{calorie.date.year}")

        return render_template("profile.html", user=user, calories=calories_list, calories_dates=calories_dates_list, weights=weights_list, weights_dates=weight_dates_list)
    else:# except:
        flash("User not logged in!")
        return redirect("/login")
    
@app.route("/add-weight", methods=["POST"])
def add_weight():
    new_weight = request.form.get("new-weight")
    date = datetime.now
    print(date)
    #crud.create_weight(user_id,new_weight,date)
    return redirect("/profile")

@app.route("/add-calorie", methods=["POST"])
def add_calorie():
    return redirect("/profile")



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)