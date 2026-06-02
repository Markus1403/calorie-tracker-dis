
from functools import wraps

from flask import (
    Blueprint, render_template, request, redirect, url_for, flash, session
)

from core.extensions import db
from sqlalchemy import text
from core.models import Food, User, FoodLog, CalorieProfile

profiles_bp = Blueprint('profiles_bp', __name__)

@profiles_bp.route('/manage_profiles', methods=['GET','POST'])
def manage_profiles():

    profiles = db.session.execute(
        db.select(CalorieProfile).filter_by(user_id=session['user_id'])
    ).scalars().all()





    return render_template('manage_profiles.html', calorie_profiles=profiles)





