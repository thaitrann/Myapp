from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from .index import index
from .register import register
from .login import login