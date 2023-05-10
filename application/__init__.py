from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../snap.db'
app.config['SECRET_KEY'] = "-80:,bPrVzTXp*zXZ0[9T/ZT=1ej08"
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
flask_bcrypt = Bcrypt(app)


from application.users import models as user_models
from application.users.views import users
from application.snaps.views import snaps
from application.cme.views import cme
from application.nasdaq.views import nasdaq
from application.nyse.views import nyse



app.register_blueprint(users, url_prefix='')
app.register_blueprint(snaps, url_prefix='/snap')
app.register_blueprint(cme, url_prefix='/cme')
app.register_blueprint(nasdaq, url_prefix='/nasdaq')
app.register_blueprint(nyse, url_prefix='/nyse')


@login_manager.user_loader
def load_user(user_id):
    return user_models.User.query.get(int(user_id))
