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
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'sqlite:///' + mkpath('../myapp.db')
)
app.config['SECRET_KEY'] = "1f5e8ff9-7c55-445b-b1e4-f22e64ccb97e"

db = SQLAlchemy(app)

