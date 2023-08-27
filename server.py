"""Server for weight monitoring website"""
from flask import (Flask, render_template, request, session, redirect, flash)
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
        return redirect("/")
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



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)