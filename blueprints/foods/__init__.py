from flask import (
    Blueprint, render_template, session
)

from core.extensions import db
from core.models import Food

foods_bp = Blueprint('foods_bp', __name__)

@foods_bp.route('/manage_foods', methods=['GET', 'POST'])
def manage_foods():

    foods = db.session.execute(
        db.select(Food).filter_by(user_id=session['user_id'])
    ).scalars().all()

    return render_template('manage_foods.html', foods=foods)
    