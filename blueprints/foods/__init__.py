from flask import (
    Blueprint, render_template, request, redirect, url_for, flash, session
)

from core.helpers import calculate_calories
from core.extensions import db
from core.models import Food
from sqlalchemy import text

foods_bp = Blueprint('foods_bp', __name__)

@foods_bp.route('/manage_foods', methods=['GET', 'POST'])
def manage_foods():

    foods = db.session.execute(
        db.select(Food).filter_by(user_id=session['user_id']).order_by(Food.id)
    ).scalars().all()

    return render_template('manage_foods.html', foods=foods)
    
@foods_bp.route('/manage_foods/delete_food', methods=['POST'])
def delete_food():
    food_id = request.form.get("food_id")
    db.session.execute(
        text("""
            DELETE FROM foods
            WHERE id = :food_id
                AND user_id = :user_id
        """),
        {
            "food_id": food_id,
            "user_id": session["user_id"]
        }
    )
    db.session.commit()
    return redirect(url_for('foods_bp.manage_foods'))

@foods_bp.route('/manage_foods/update_food', methods=['POST'])
def update_food():
    food_id = request.form.get("food_id")
    name = request.form.get("name")
    protein = request.form.get("protein")
    carbs = request.form.get("carbs")
    fat = request.form.get("fat")

    db.session.execute(
        text("""
            UPDATE foods
            SET name = :name,
                protein = :protein,
                carbs = :carbs,
                fat = :fat
            WHERE id = :food_id
                AND user_id = :user_id
        """),
        {
            "food_id": food_id,
            "user_id": session["user_id"],
            "name": name,
            "carbs": carbs,
            "protein": protein,
            "fat": fat
        }
    )
    db.session.commit()
    return redirect(url_for('foods_bp.manage_foods'))


@foods_bp.route('/manage_foods/insert_food', methods=['POST'])
def insert_food():
    food_id = request.form.get("food_id")
    name = request.form.get("name")
    protein = request.form.get("protein")
    carbs = request.form.get("carbs")
    fat = request.form.get("fat")

    calories = calculate_calories(carbs, fat, protein)

    db.session.execute(
            text("""
                INSERT INTO foods (user_id, name, protein, carbs, fat, calories)
                VALUES (:user_id, :name, :protein, :carbs, :fat, :calories)
            """),
            {
                "food_id": food_id,
                "user_id": session["user_id"],
                "name": name,
                "carbs": carbs,
                "protein": protein,
                "fat": fat,
                "calories": calories
            }
        )
    db.session.commit()
    return redirect(url_for('foods_bp.manage_foods'))