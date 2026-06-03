from functools import wraps
from datetime import date

from flask import (
    Blueprint, render_template, request, redirect, url_for, flash, session
)

from core.extensions import db
from core.helpers import calculate_calories
from sqlalchemy import text
from core.models import Food, User, FoodLog, CalorieProfile

profiles_bp = Blueprint('profiles_bp', __name__)

@profiles_bp.route('/manage_profiles', methods=['GET','POST'])
def manage_profiles():
   curr_date = request.form.get("date") 

   profiles = db.session.execute(
       db.select(CalorieProfile).filter_by(user_id=session['user_id'])
   ).scalars().all()

   return render_template('manage_profiles.html', curr_date=curr_date, profiles=profiles)


@profiles_bp.route('/manage_profiles/save_profile', methods=['GET','POST'])
def save_profile():
    curr_date = request.form.get("date") 

    goal_name = request.form.get("name")
    protein   = float(request.form.get("protein"))
    carbs     = float(request.form.get("carbs"))
    fat       = float(request.form.get("fat"))
    calories  = calculate_calories(carbs, fat, protein)

    goal = CalorieProfile(
            user_id  = session['user_id'],
            name     = goal_name,
            protein  = protein,
            carbs    = carbs,
            fat      = fat,
            calories = calories
            ) 
    db.session.add(goal)
    db.session.commit()
    return redirect(url_for('profiles_bp.manage_profiles'))
    

@profiles_bp.route('/manage_profiles/delete_profile', methods=['GET', 'POST'])
def delete_profile():
    curr_date = request.form.get("date") 
    return redirect(url_for('profiles_bp.manage_profiles'))


@profiles_bp.route('/manage_profiles/update_profile', methods=['POST'])
def update_profile():
    curr_date = date # request.form.get("date") 

    profile_id = request.form.get("id")
    new_name   = request.form.get("name", "").strip()
    protein    = float(request.form.get("protein", 0))
    carbs      = float(request.form.get("carbs", 0))
    fat        = float(request.form.get("fat", 0))
    calories  = calculate_calories(carbs, fat, protein)

    db.session.execute(
        text('''
        UPDATE calorie_profiles
        SET 
            name     = :name,
            protein  = :protein,
            carbs    = :carbs,
            fat      = :fat,
            calories = :calories
        WHERE id = :id
    '''),
    {
        "name": new_name,    
        "protein": protein,  
        "carbs": carbs,      
        "fat": fat,          
        "calories": calories,
        "id": profile_id
    },
        )
    
    db.session.commit()
    return redirect(url_for('profiles_bp.manage_profiles'))

@profiles_bp.route('/manage_profiles/set_profile', methods=['GET', 'POST'])
def set_profile():
    curr_date = request.form.get("date") 
    return redirect(url_for('profiles_bp.manage_profiles'))
