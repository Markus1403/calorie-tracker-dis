from datetime import datetime, timezone, date
from core.extensions import db


MEALTIMES = ("breakfast", "lunch", "dinner", "snack")

class User(db.Model):
    __tablename__ = "users"

    id       = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    password = db.Column(db.String(80), nullable=False)

    foods    = db.relationship("Food", back_populates="user", cascade="all, delete-orphan")
    profiles = db.relationship("CalorieProfile", back_populates="user", cascade="all, delete-orphan")
    logs     = db.relationship("FoodLog", back_populates="user", cascade="all, delete-orphan")

class CalorieProfile(db.Model):
    __tablename__ = "calorie_profiles"

    id       = db.Column(db.Integer, primary_key = True)
    user_id  = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    name     = db.Column(db.String(80), unique=False, nullable=False)

    carbs    = db.Column(db.Numeric(8, 2), nullable=False)
    fat      = db.Column(db.Numeric(8, 2), nullable=False)
    protein  = db.Column(db.Numeric(8, 2), nullable=False)
    calories = db.Column(db.Numeric(8, 2), nullable=False)

    user = db.relationship("User", back_populates="profiles")

class Food(db.Model):
    __tablename__ = "foods"

    id       = db.Column(db.Integer, primary_key=True)
    user_id  = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    name     = db.Column(db.String(80), unique=False, nullable=False)
    user     = db.relationship("User", back_populates="foods")


    carbs    = db.Column(db.Numeric(8, 2), nullable=False)
    fat      = db.Column(db.Numeric(8, 2), nullable=False)
    protein  = db.Column(db.Numeric(8, 2), nullable=False)
    calories = db.Column(db.Numeric(8, 2), nullable=False)


class FoodLog(db.Model):
    __tablename__  = "food_log"

    id             = db.Column(db.Integer, primary_key=True)
    user_id        = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    date           = db.Column(db.Date, nullable=False, default=date.today)
    mealtime       = db.Column(db.Enum(*MEALTIMES, name="mealtime"), nullable=False)

    food_id        = db.Column(db.Integer, db.ForeignKey("foods.id"), nullable=True)
    quantity_grams = db.Column(db.Numeric(8, 2), nullable=True)

    # If food is quick added, values are stored directly. Otherwise it is derived by using a join with Food on food_id. Name should be set as "QUICK" if food_id is null
    carbs          = db.Column(db.Numeric(8, 2), nullable=True)
    fat            = db.Column(db.Numeric(8, 2), nullable=True)
    protein        = db.Column(db.Numeric(8, 2), nullable=True)
    calories       = db.Column(db.Numeric(8, 2), nullable=True)
    
    user = db.relationship("User", back_populates="logs")
    food = db.relationship("Food") 
