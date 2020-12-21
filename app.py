from flask import Flask
from flask_bootstrap import Bootstrap
import os.path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy(app)
