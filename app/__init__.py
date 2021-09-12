from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from .index import index
from .register import register
from .login import login
# from .models import user, note

from app import db
from .models.user import User
from .models.note import Note

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Note': Note}