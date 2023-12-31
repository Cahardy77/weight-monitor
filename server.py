"""API WEBSITE: https://rapidapi.com/kidddevs/api/health-calculator-api/"""

"""Server for weight monitoring website"""
from flask import (Flask, render_template, request, session, redirect, flash, jsonify)
from sqlalchemy import text
#Model has our class files for User,Calorie, and Weight
from model import connect_to_db, db
from jinja2 import StrictUndefined
#Scripts for reading and updating the database
import crud
#Having issues with datetime from database, importing to striptime?
from datetime import datetime
#Api calls
import api_caller

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

@app.route("/logout")
def logout():
    session["email"] = None
    return redirect("/")

@app.route("/bmi")
def bmi():
    email = session["email"]
    user = crud.get_user_by_email(email)
    weights = crud.get_weights_by_email(email)
    height = user.height
    weight = weights[-1]
    bmi = api_caller.BMI(height, weight.weight)
    return bmi

@app.route("/get-water")
def get_water():
    email = session["email"]
    user = crud.get_user_by_email(email)
    waters = crud.get_water_by_email(email)
    weight = todays_weight("kg")
    water_list = []
    water_dates_list = []
    todays_water_list = []
    needed_water = api_caller.water_intake(weight, user.activity_level)["water_intake"]
    todays_water = 0
    #calculate how much water was eaten today
    for water in waters:
        if str(water.date).rsplit(" ")[0] == str(todays_date()).split(" ")[0]:
            todays_water_list.append(water)
            todays_water += water.water
            water_dates_list.append(f"{water.date.month}/{water.date.day}/{water.date.year}")
    #make list with total water eaten and water left to eat


    
    water_list.append(todays_water)
    water_list.append(needed_water-todays_water)
    

    water_dict = {"waters": water_list}
    return water_dict

@app.route("/get-weights")
def get_weights():
    weights = crud.get_weights_by_email(session["email"])
    weights_list = []
    weight_dates_list = []
    weight_comments = []

    for weight in weights:
        
        weights_list.append(weight.weight)
        weight_dates_list.append(f"{weight.date.month}/{weight.date.day}/{weight.date.year}")
        weight_comments.append(f"Date: {weight_dates_list[-1]} Weight: {weight.weight} Comment: {weight.comment}")
  
    weights_dict = {"weights": weights_list[-5:], "weights_dates": weight_dates_list[-5:], "weight_comments": weight_comments[-5:]}
    
    return weights_dict

@app.route("/get-calories")
def get_calories():
    user = crud.get_user_by_email(session["email"])
    calories = crud.get_calories_by_email(session["email"])
    calories_list = []
    calories_dates_list = []
    todays_calories_list = []
    calories_comments = []
    age = todays_date().year - user.birth.year
    weight = todays_weight("kg")
    height = user.height * 2.54 #convert inches to cm for api
    needed_calories = api_caller.caloric_intake(age,weight,height,user.gender,user.activity_level,user.goal)
    needed_calories = float(needed_calories["caloric_needs"]["calories"].split(" ")[0])
    needed_calories = round(needed_calories)
    todays_calories = 0
    #calculate how many calories were eaten today
    for calorie in calories:
        if str(calorie.date).rsplit(" ")[0] == str(todays_date()).split(" ")[0]:
            todays_calories_list.append(calorie)
            calories_comments.append(f"Date: {calorie.date.month}/{calorie.date.day}/{calorie.date.year} Calories: {calorie.calories} Comment: {calorie.comment}")
            todays_calories += calorie.calories
    #make list with total calories eaten and calories left to eat
    calories_list.append(todays_calories)
    calories_list.append(int(needed_calories)-todays_calories)
    calories_dates_list.append(f"{calorie.date.month}/{calorie.date.day}/{calorie.date.year}")
    calories_dict = {"calories": calories_list, "dates": calories_dates_list, "comments": calories_comments}
    return calories_dict

        

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
    height = request.form.get("height")
    gender = request.form.get("gender")
    activity_level = request.form.get("activity-level")
    goal = request.form.get("goal")
    weight = request.form.get("current-weight")

    if crud.get_user_by_email(email) :
        flash("User email already exists!")
        return redirect("/register")
    else:
        new_user = crud.create_user(email, password, first_name, last_name, birth_date, height, gender, activity_level, goal)
        db.session.add(new_user)
        db.session.commit()
        new_weight = crud.create_weight(new_user.user_id, weight, todays_date())
        db.session.add(new_weight)
        db.session.commit()
        new_calorie = crud.create_calorie(new_user.user_id, 0, todays_date())
        db.session.add(new_calorie)
        db.session.commit()
        new_water = crud.create_water(new_user.user_id, 0, todays_date())
        db.session.add(new_water)
        db.session.commit()
        session["email"] = new_user.email
        flash(f"Thank you and welcome, {new_user.fname}!")
        return redirect("/")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/profile")
def show_user():
    """Show details on a particular user."""
    try:
        if session["email"]: #
            
            user = crud.get_user_by_email(session["email"])

            return render_template("profile.html", user=user)
        else:# 
            flash("User not logged in!")
            return redirect("/login")
    except:
        flash("User not logged in!")
        return redirect("/login")
    
@app.route("/is-logged-in")
def is_logged_in():
    if not session["email"]:
        return "False"
    else:
        return "True"
    
@app.route("/add-weight", methods=["POST"])
def add_weight():
    new_weight = request.form.get("new-weight")
    new_comment = request.form.get("new-weight-comment")
    current_date = todays_date()
    email = session["email"]
    user = crud.get_user_by_email(email)
    new_weight = crud.create_weight(user.user_id,new_weight,current_date,new_comment)
    db.session.add(new_weight)
    db.session.commit()
    return redirect("/profile")

@app.route("/add-calorie", methods=["POST"])
def add_calorie():
    new_calorie = request.form.get("new-calorie")
    new_comment = request.form.get("new-calorie-comment")
    current_date = todays_date()
    email = session["email"]
    user = crud.get_user_by_email(email)
    new_calorie = crud.create_calorie(user.user_id,new_calorie,current_date,new_comment)
    db.session.add(new_calorie)
    db.session.commit()
    return redirect("/profile")

@app.route("/add-water", methods=["POST"])
def add_water():
    new_water = request.form.get("new-water")
    current_date = todays_date()
    email = session["email"]
    user = crud.get_user_by_email(email)
    add_water = crud.create_water(user.user_id,new_water,current_date)
    db.session.add(add_water)
    db.session.commit()
    return redirect("/profile")

def todays_weight(conversion):
    weights = crud.get_weights_by_email(session["email"])
    weight = weights[-1]
    if conversion == "kg":
        return (weight.weight / 2.205)
    else:
        return weight.weight

    
def todays_date():
    date = str(datetime.now()).rsplit(".")
    current_date = datetime.strptime(date[0], "%Y-%m-%d %H:%M:%S")
    return current_date

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)