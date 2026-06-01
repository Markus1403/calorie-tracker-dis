from flask import Flask, render_template, request, redirect, url_for, flash
#from models import init_db
from datetime import date, timedelta
from dotenv import load_dotenv
import os



load_dotenv()


def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY")
    
    from blueprints import main_bp

    app.register_blueprint(main_bp)
    return app
    
    
