from flask import Flask
from flask_bootstrap import Bootstrap
import os.path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy(app)

def mkpath(p):
    return os.path.normpath(
        os.path.join(
            os.path.dirname(__file__),
            p))

app.config['SQLALCHEMY_DATABASE_URI'] = (
    'sqlite:///'+mkpath('../myapp.db'))
db = SQLAlchemy(app)