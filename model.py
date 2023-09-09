from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(20))
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(20))
    birth = db.Column(db.DateTime)
    height = db.Column(db.Integer)
    gender = db.Column(db.String(7))
    activity_level = db.Column(db.String(30))
    goal = db.Column(db.String(30))
    

    calories = db.relationship("Calorie", back_populates="user")
    weights = db.relationship("Weight", back_populates="user")

class Calorie(db.Model):
    __tablename__ = "calories"

    calorie_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    calories = db.Column(db.Integer)
    # DateTime may cause issues?
    date = db.Column(db.DateTime)
    comment = db.Column(db.String(200))

    user = db.relationship("User", back_populates="calories")

    def __repr__(self):
        return f'<User user_id={self.user_id} calorie={self.calories}>'
    

class Weight(db.Model):
    __tablename__ = "weights"

    weight_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    weight = db.Column(db.Float)
    # DateTime may cause issues?
    date = db.Column(db.DateTime)
    comment = db.Column(db.String(200))
    
    user = db.relationship("User", back_populates="weights")

    def __repr__(self):
        return f'<User user_id={self.user_id} weight={self.weight}>'

def connect_to_db(flask_app, db_uri="postgresql:///weight-monitor", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)