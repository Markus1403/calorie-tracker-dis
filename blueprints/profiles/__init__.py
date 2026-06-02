
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


    return render_template('manage_profiles.html')





