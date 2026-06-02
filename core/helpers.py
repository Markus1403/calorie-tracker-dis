from functools import wraps

from flask import (
    Blueprint, render_template, request, redirect, url_for, flash, session
)

from core.extensions import db
from sqlalchemy import text
from core.models import Food, User, FoodLog, CalorieProfile

main_bp = Blueprint('main_bp', __name__)


def insert_standard_foods(input_user_id):

    # Direct sql query to fulfill projext requirements. 
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

    banana = Food(user_id=input_user_id, name='Banana', carbs=27.0, fat=0.30, protein=1.30, calories=105)
    db.session.add(banana)


    db.session.commit()
