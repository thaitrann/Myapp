from flask import Flask
from flask_mail import Mail
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_mgr = LoginManager(app)
login_mgr.login_view = 'login'
mail = Mail(app)

from .home import home
from .register import register
from .login import login
from .index import index
from .email import email

from app import db
from .models.user import User
from .models.note import Note

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Note': Note}