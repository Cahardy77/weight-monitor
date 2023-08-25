from model import User, Weight, Calorie, connect_to_db, db

def create_user(email, password, fname, lname, birth):
    user = User(email=email, password=password, fname=fname, lname=lname, birth=birth)
    return user
    
def read_user(user_id):
    User.query.get(user_id)

def create_calorie(user_id, calories, date):
    calorie = Calorie(user_id=user_id, calories=calories, date=date)
    return calorie

def read_calorie(user_id):
    return Calorie.query.filter(Calorie.user_id == user_id).all()

def create_weight(user_id, weight, date):
    weight = Weight(user_id=user_id, date=date, weight=weight)
    return weight

def read_weight(user_id):
    return Weight.query.filter(Weight.user_id == user_id).all()

def get_calories_by_email(email):
    user = User.query.filter(email)
    read_calorie(user.user_id)

def get_weights_by_email(email):
    user = User.query.filter(email)
    read_weight(user.user_id)

def check_password_by_email(email, password):
    user = User.query.filter(User.email == email).first()
    if user:
        return user.password == password
    else:
        return False
    
def get_user_by_email(email_user):
    return User.query.filter(User.email == email_user).first()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)