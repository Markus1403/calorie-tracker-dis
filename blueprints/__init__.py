from functools import wraps

from flask import (
    Blueprint, render_template, request, redirect, url_for, flash, session
)

from core.extensions import db
from sqlalchemy import text
from core.models import Food, User, FoodLog, CalorieProfile, DailyGoal, safe_float
from core.helpers import insert_standard_foods, insert_standard_profile, calculate_calories
from datetime import date, timedelta

import re

main_bp = Blueprint('main_bp', __name__)



def login_required(view):
    """Redirect to the login page if no user is in the session."""
    @wraps(view)
    def wrapped(*args, **kwargs):
        if session.get('user_id') is None:
            return redirect(url_for('main_bp.login'))
        return view(*args, **kwargs)
    return wrapped

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        input_username = request.form['username']
        password = request.form['password']

        existing = db.session.execute(
            db.select(User).filter_by(username=input_username)
        ).scalar_one_or_none()

        if not input_username or not password:
            flash('Username and password are required.')
        elif existing is not None:
            flash('That username is already taken.')
        else:
            user = User(username=input_username, password=password)
            pattern = r"[`~!@#$%^&*()_\-=+\[{\]}\\|;:'\",<.>/?]"
            special_check = re.findall(pattern, user.password)
            pattern = r"[A-Z]"
            capital_check = re.findall(pattern, user.password)
            final_check = True
            if len(password) < 5: 
                flash('Length of password must be atleast 5 characters')
                final_check = False
            if not special_check:
                flash('Password must contain atleast 1 special character')
                final_check = False
            if not capital_check:
                flash('Password must contain atleast 1 capital character')
                final_check = False
            if final_check == True:
                db.session.add(user)
                db.session.commit()
                insert_standard_foods(user.id)
                insert_standard_profile(user.id) 
                return redirect(url_for('main_bp.login'))

    return render_template('register.html')


@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        input_username = request.form['username']
        password = request.form['password']

        user = db.session.execute(
            db.select(User).filter_by(username=input_username)
        ).scalar_one_or_none()

        if user is None or user.password != password:
            flash('Invalid username or password.')
        else:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main_bp.index'))

    return render_template('login.html')


@main_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main_bp.login'))


@main_bp.route('/', methods=['GET','POST'])
@login_required
def index():
    foods = db.session.execute(
        db.select(Food).filter_by(user_id=session['user_id'])
    ).scalars().all()

    calorie_profiles = db.session.execute(
        db.select(CalorieProfile).filter_by(user_id=session['user_id'])
    ).scalars().all()
    
    curr_date_str = request.args.get('date')
    if curr_date_str:
        curr_date_nonISO = date.fromisoformat(curr_date_str)
    else:
        curr_date_nonISO = date.today()

    curr_date = curr_date_nonISO.isoformat()
    
    prev_date = (curr_date_nonISO - timedelta(days=1)).isoformat()
    next_date = (curr_date_nonISO + timedelta(days=1)).isoformat()
    
    log_row = db.session.scalars(db.select(FoodLog).where(FoodLog.date == curr_date).filter_by(user_id=session['user_id'])).all()
    
    log = []
    for row in log_row:
        rounded_row = {col.name: getattr(row, col.name) for col in row.__table__.columns}
        
        rounded_row['protein'] = round(rounded_row['protein'], 2)
        rounded_row['carbs'] = round(rounded_row['carbs'], 2)
        rounded_row['fat'] = round(rounded_row['fat'], 2)
        log.append(rounded_row)
    
    total = {'calories': 0, 'protein': 0, 'carbs': 0, 'fat': 0}
    for entry in log_row:
        total['protein'] += entry.protein
        total['carbs'] += entry.carbs
        total['fat'] += entry.fat
    
    #UPDATE FORMULA LATER
    total['calories'] = total['protein'] * 4 + total['carbs'] * 4 + total['fat'] * 9

    for key in total:
        total[key] = round(total[key],2)

    stmt = db.select(DailyGoal).where(DailyGoal.date <= curr_date).where(DailyGoal.user_id == session['user_id']).order_by(DailyGoal.date.desc())
    
    goal = db.session.scalars(stmt).first()
    
    
    goals = {'name': 'value',  'calories': 0, 'protein': 0, 'carbs': 0, 'fat': 0}
    if goal:
        goals['calories'] = goal.calorie_profile.calories
        goals['protein'] = goal.calorie_profile.protein
        goals['carbs'] = goal.calorie_profile.carbs
        goals['fat'] = goal.calorie_profile.fat
        goals['name'] = goal.calorie_profile.name
        
    goalsLeft = {
        'calories': round(goals['calories'] - total['calories'], 2), 
        'protein': round(goals['protein'] - total['protein'], 2), 
        'carbs': round(goals['carbs'] - total['carbs'], 2), 
        'fat': round(goals['fat'] - total['fat'], 2)
    }

    return render_template('index.html', foods=foods, calorie_profiles=calorie_profiles, log=log, total = total, goals=goals, goalsLeft=goalsLeft, curr_date=curr_date, prev_date=prev_date, next_date=next_date)



@main_bp.route('/add_macros', methods=['POST'])
def quick_add_macros():
    curr_date = request.form.get("date")
    protein = safe_float(request.form.get('protein', None))
    carbs = safe_float(request.form.get('carbs', None))
    fat = safe_float(request.form.get('fat', None))
    meal_time = request.form.get('mealtime')
    calories = calculate_calories(carbs, fat, protein)
    
    new_food_entry = FoodLog(
        user_id=session['user_id'],
        date=curr_date,
        mealtime = meal_time,
        food_id = None, 
        quantity_grams = 0, 
        protein= protein,
        carbs=carbs,
        fat=fat,
        calories = calories 
        )
    db.session.add(new_food_entry)
    db.session.commit()
    
    return redirect(f'/?date={curr_date}')

@main_bp.route('/add_food', methods=['POST'])
def add_food():
    curr_date = request.form.get("date")
    food_id = int(request.form['food_id'])
    meal_time = request.form.get("meal_time")
    grams = float(request.form.get("grams"))
    multiplier = float(grams/100)
    
    stmt = db.select(Food).where(Food.user_id == session['user_id']).where(Food.id == food_id)
    food = db.session.scalars(stmt).first()
    
    if not food:
        return "Food not found", 404
    
    new_food_entry = FoodLog(
        user_id=session['user_id'],
        date=curr_date,
        mealtime = meal_time,
        food_id = food_id, 
        quantity_grams = grams, 
        protein= safe_float(food.protein) * multiplier,
        carbs= safe_float(food.carbs) * multiplier,
        fat= safe_float(food.fat) * multiplier,
        calories = safe_float(food.calories) * multiplier 
        )
    db.session.add(new_food_entry)
    db.session.commit()
    
    return redirect(f'/?date={curr_date}')

#Delete might be buggy
@main_bp.route('/delete_entry', methods=['POST'])
def delete_entry():
    entry_id = request.form.get("entry_id")
    curr_date = request.form.get("date")
    
    entry = db.session.scalar(db.select(FoodLog).where(FoodLog.id == entry_id).where(FoodLog.user_id == session['user_id']))
    if entry:
        db.session.delete(entry)
        db.session.commit()
    
    return redirect(f'/?date={curr_date}')
