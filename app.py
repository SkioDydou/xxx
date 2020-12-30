from flask import Flask
from flask_bootstrap import Bootstrap
import os.path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

def mkpath(p):
    return os.path.normpath(
        os.path.join(os.path.dirname(__file__),
        p)
    )

app = Flask(__name__)
Bootstrap(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'sqlite:///' + mkpath('../myapp.db')
)
app.config['SECRET_KEY'] = "7E9B2040-FFA0-4383-9BA9-4AC714F0F10B"
db = SQLAlchemy(app)