from functools import wraps
from datetime import date

from flask import (
    Blueprint, render_template, request, redirect, url_for, flash, session
)

from core.extensions import db
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

    return redirect(url_for('profiles_bp.manage_profiles'))

@profiles_bp.route('/manage_profiles/delete_profile', methods=['GET', 'POST'])
def delete_profile():
    curr_date = request.form.get("date") 
    return redirect(url_for('profiles_bp.manage_profiles'))


@profiles_bp.route('/manage_profiles/update_profile', methods=['POST'])
def update_profile():
    curr_date = date # request.form.get("date") 
    return redirect(url_for('profiles_bp.manage_profiles'))

@profiles_bp.route('/manage_profiles/set_profile', methods=['GET', 'POST'])
def set_profile():
    curr_date = request.form.get("date") 
    return redirect(url_for('profiles_bp.manage_profiles'))
