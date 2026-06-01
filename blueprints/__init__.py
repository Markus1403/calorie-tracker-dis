from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
#from models import init_db
from datetime import date, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

main_bp = Blueprint('main_bp', __name__)

@main_bp .route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')
