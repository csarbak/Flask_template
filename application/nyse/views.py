from flask import Blueprint, render_template, url_for, redirect, current_app, flash
from flask_login import login_required, current_user
from sqlalchemy import exc

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired
# from .models import Snap
from application import db

nyse = Blueprint('nyse', __name__, template_folder='templates')

@nyse.route('/', methods=['GET','POST'])
def home():
    return render_template('nyse/homePage.html')


