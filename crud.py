from model import User, Weight, Calorie, Water, connect_to_db, db
from sqlalchemy import text
import server
#<!--#age,weight,height,gender,activity_level,goal-->
def create_user(email, password, fname, lname, birth, height, gender, activity_level, goal):
    user = User(email=email, password=password, fname=fname, lname=lname, birth=birth, height=height, gender=gender, activity_level=activity_level, goal=goal)
    return user
    
def read_user(user_id):
    User.query.get(user_id)

def create_calorie(user_id, calories, date, comment="No comment"):
    if comment == "":
        comment = "No Comment"
    calorie = Calorie(user_id=user_id, calories=calories, date=date, comment=comment)
    return calorie

def read_calorie(user_id):
    return Calorie.query.filter(Calorie.user_id == user_id).all()

def create_weight(user_id, weight, date, comment="No comment"):
    if comment == "":
        comment = "No Comment"
    weight = Weight(user_id=user_id, date=date, weight=weight, comment=comment)
    return weight

def read_weight(user_id):
    return Weight.query.filter(Weight.user_id == user_id).all()

def get_calories_by_email(email):
    user = User.query.filter(User.email == email).first()
    return read_calorie(user.user_id)

def get_weights_by_email(email):
    user = User.query.filter(User.email == email).first()
    return read_weight(user.user_id)

def create_water(user_id, water, date):
    water = Water(user_id=user_id, date=date, water=water)
    return water

def read_water(user_id):
    return Water.query.filter(Water.user_id == user_id).all()

def get_water_by_email(email):
    user = User.query.filter(User.email == email).first()
    return read_water(user.user_id)

def check_password_by_email(email, password):
    user = User.query.filter(User.email == email).first()
    print("222222222222222222222222")
    print(user)
    if user:
        print(f"User password is {user.password == password}")
        return user.password == password
    
    else:
        return False
    
def get_user_by_email(email_user):
    user = User.query.filter(User.email == email_user).first()
    if user:
        return user
    else:
        return False

if __name__ == '__main__':
    from server import app
    connect_to_db(app)