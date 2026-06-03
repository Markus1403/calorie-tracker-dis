from functools import wraps
from datetime import date

from flask import (
    Blueprint, render_template, request, redirect, url_for, flash, session
)

from core.extensions import db
from sqlalchemy import text
from core.models import Food, User, FoodLog, CalorieProfile

main_bp = Blueprint('main_bp', __name__)


def calculate_calories(carbs, fats, protein):
    carbs = float(carbs)
    fats = float(fats)
    protein = float(protein)
    return carbs * 4 + protein * 4 + fats * 9


def insert_standard_foods(input_user_id):

    # Direct sql query to fulfill project requirements
    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Sødmælk",
            "carbs": 4.8,
            "fat": 3.5,
            "protein": 3.4,
            "calories": 64,
        },
    )

    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Apple",
            "carbs": 25,
            "fat": 0.3,
            "protein": 0.4,
            "calories": 95,
        },
    )

    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Orange",
            "carbs": 27,
            "fat": 0.2,
            "protein": 1.2,
            "calories": 62,
        },
    )

    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Lemon",
            "carbs": 9.3,
            "fat": 0.3,
            "protein": 1.1,
            "calories": 29,
        },
    )

    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Peach",
            "carbs": 9.3,
            "fat": 0.3,
            "protein": 0.9,
            "calories": 39,
        },
    )


    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Strawberry",
            "carbs": 7.7,
            "fat": 0.3,
            "protein": 0.7,
            "calories": 32,
        },
    )

    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Avocado",
            "carbs": 8.5,
            "fat": 14.7,
            "protein": 2,
            "calories": 160,
        },
    )

    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Mango",
            "carbs": 15,
            "fat": 0.4,
            "protein": 0.8,
            "calories": 60,
        },
    )

    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Grapes",
            "carbs": 18.1,
            "fat": 0.2,
            "protein": 0.7,
            "calories": 69,
        },
    )

    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Watermelon",
            "carbs": 7.6,
            "fat": 0.2,
            "protein": 0.6,
            "calories": 30,
        },
    )


    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Pineapple",
            "carbs": 13.1,
            "fat": 0.1,
            "protein": 0.5,
            "calories": 50,
        },
    )


    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Pineapple",
            "carbs": 13.1,
            "fat": 0.1,
            "protein": 0.5,
            "calories": 50,
        },
    )
    
    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Pear",
            "carbs": 15.2,
            "fat": 0.1,
            "protein": 0.4,
            "calories": 57,
        },
    )
    
    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Kiwi",
            "carbs": 14.7,
            "fat": 0.5,
            "protein": 1.1,
            "calories": 61,
        },
    )

    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Chicken Breast",
            "carbs": 0,
            "fat": 3.6,
            "protein": 31,
            "calories": 165,
        },
    )

    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Beef",
            "carbs": 0,
            "fat": 15.4,
            "protein": 26.1,
            "calories": 250,
        },
    )

    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "John Pork",
            "carbs": 0,
            "fat": 14,
            "protein": 27.3,
            "calories": 242,
        },
    )    

    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Lamb",
            "carbs": 0,
            "fat": 20.9,
            "protein": 24.4,
            "calories": 294,
        },
    ) 

    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Chicken Thigh",
            "carbs": 0,
            "fat": 10.9,
            "protein": 26,
            "calories": 209,
        },
    )


    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Chicken Thigh",
            "carbs": 0,
            "fat": 10.9,
            "protein": 26,
            "calories": 209,
        },
    )

    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Ground Beef",
            "carbs": 0,
            "fat": 20,
            "protein": 17.2,
            "calories": 254,
        },
    )
    
    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Bacon",
            "carbs": 1.4,
            "fat": 42,
            "protein": 36,
            "calories": 541,
        },
    )

    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Duck",
            "carbs": 0,
            "fat": 28.4,
            "protein": 19,
            "calories": 337,
        },
    )

    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Salmon",
            "carbs": 0,
            "fat": 13.4,
            "protein": 20.4,
            "calories": 208,
        },
    )

    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Tuna",
            "carbs": 0,
            "fat": 1.3, 
            "protein": 28.2,
            "calories": 132,
        },
    )

    db.session.execute(
        text("""
            INSERT INTO foods (user_id, name, carbs, fat, protein, calories)
            VALUES (:user_id, :name, :carbs, :fat, :protein, :calories)
        """),
        {
            "user_id": input_user_id,
            "name": "Mackerel",
            "carbs": 0,
            "fat": 13.9,
            "protein": 18.6,
            "calories": 205,
        },
    )
 
 
 
 
    banana = Food(user_id=input_user_id, name='Banana', carbs=27.0, fat=0.30, protein=1.30, calories=105)
    db.session.add(banana)


    db.session.commit()


def insert_standard_profile(input_user_id):
    standard_profile = CalorieProfile(user_id=input_user_id, name="Standard Calorie Profile", carbs=400, fat=67.0, protein=200.0, calories=3083.1)


    standard_goal = DailyGoal(
                user_id=input_user_id,
                profile_id= standard_profile.id,
                date = date(1980, 0, 0)
            )


    db.session.add(standard_profile)
    db.session.commit()
