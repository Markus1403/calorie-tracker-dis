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
    banana = Food(user_id=input_user_id, name='Banana', carbs=27.0, fat=0.30, protein=1.30, calories=105)
    db.session.add(banana)


    db.session.commit()




def inser_standard_profile(input_user_id):
    standard_profile = CalorieProfile(user_id=input_user_id, name="Standard Calorie Profile", carbs=400, fat=67.0, protein=200.0, calories=3083.1)
    db.session.add(standard_profile)
    db.session.commit()



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
            db.session.add(user)
            db.session.commit()
            insert_standard_foods(user.id)
            inser_standard_profile(user.id)
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


@main_bp.route('/', methods=['GET'])
@login_required
def index():
    foods = db.session.execute(
        db.select(Food).filter_by(user_id=session['user_id'])
    ).scalars().all()

    calorie_profiles = db.session.execute(
        db.select(CalorieProfile).filter_by(user_id=session['user_id'])
    ).scalars().all()


    return render_template('index.html', foods=foods, calorie_profiles=calorie_profiles)
