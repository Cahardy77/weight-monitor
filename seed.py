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

#Open all json files and load data
with open("data/users.json") as data_user:
    user_data = json.loads(data_user.read())

with open("data/calories.json") as data_calorie:
    calorie_data = json.loads(data_calorie.read())

with open("data/weights.json") as data_weight:
    weight_data = json.loads(data_weight.read())
"""
# This doesn't work for some reason. Dict error
for user in user_data:
    print(user["fname"])
    #Dict Error?
    #current_user = crud.create_user(user["email"],user["password"],user["fname"],user["lname"],user["birth"])
    email, password, fname, lname, birth = (user["email"],user["password"],user["fname"],user["lname"],user["birth"])
    current_user = crud.create_user(email, password, fname, lname, birth)
    users_list.append(current_user)
print(users_list)
model.db.session.add_all(user_data)
model.db.session.commit()

"""
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
    height = 104
    gender = "male"
    activity_level = "sedentary"
    goal = "maintenance"

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
    date = datetime.strptime(weight["date"], "%m-%d-%Y %H:%M")

    new_weight = crud.create_weight(user_id, weight_var, date)
    calories_list.append(new_weight)
    
model.db.session.add_all(users_list)
model.db.session.add_all(calories_list)
model.db.session.add_all(weights_list)
model.db.session.commit()