import os
import json
import crud
import server
import model
from datetime import datetime

#Clear database and reconnect to database
os.system("dropdb weight-monitor")
os.system("createdb weight-monitor")
model.connect_to_db(server.app)
model.db.create_all()

#Lists for storing objects later
users_list = []
calories_list = []
weights_list = []
water_list = []

#Open all json files and load data
with open("data/users.json") as data_user:
    user_data = json.loads(data_user.read())

with open("data/calories.json") as data_calorie:
    calorie_data = json.loads(data_calorie.read())

with open("data/weights.json") as data_weight:
    weight_data = json.loads(data_weight.read())

with open("data/water.json") as data_water:
    water_data = json.loads(data_water.read())

#Make user objects and add to list
for user in user_data:
    email, password, fname, lname = (
        user["email"],
        user["password"],
        user["fname"],
        user["lname"]
    )
    #birth = datetime.strptime(user["birth"], "%Y-%m-%d")
    birth = user["birth"]
    height = 72
    gender = "male"
    activity_level = "moderately_active"
    goal = "weight_loss"

    new_user = crud.create_user(email, password, fname, lname, birth, height, gender, activity_level, goal)
    users_list.append(new_user)

#Make calorie objects and add to list
for calorie in calorie_data:
    user_id, calories = (
        calorie["user_id"],
        calorie["calories"]
    )
    date = datetime.strptime(calorie["date"], "%m-%d-%Y %H:%M")
    #time = f"{date.hour}:{date.minute}"
    new_calorie = crud.create_calorie(user_id, calories, date)
    calories_list.append(new_calorie)

#Make weight objects and add to list
for weight in weight_data:
    user_id, weight_var= (
        weight["user_id"],
        weight["weight"]
    )
    if "comment" in weight.keys():
        comment = weight["comment"]
    else:
        comment = "No Comment."
    date = datetime.strptime(weight["date"], "%m-%d-%Y %H:%M")

    new_weight = crud.create_weight(user_id, weight_var, date, comment)
    calories_list.append(new_weight)

for water in water_data:
    user_id, water_var= (
        water["user_id"],
        water["water"]
    )
    date = datetime.strptime(water["date"], "%m-%d-%Y %H:%M")

    new_water = crud.create_water(user_id, water_var, date)
    water_list.append(new_water)
    
model.db.session.add_all(users_list)
model.db.session.add_all(calories_list)
model.db.session.add_all(weights_list)
model.db.session.add_all(water_list)
model.db.session.commit()