from .app import app, db
from flask import render_template, url_for, redirect, flash, request
from .models import get_sample, get_details, get_author, get_livres_by_author, get_author_by_name, Author, User, Album
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, PasswordField
from wtforms.validators import DataRequired
from hashlib import sha256
from flask_login import login_user, current_user, logout_user, login_required

class AuthorForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('nom', validators = [DataRequired()])

class LoginForm(FlaskForm):
    username = StringField('Pseudo')
    password = PasswordField('Mot de passe')
    next = HiddenField()

    def get_authenticated_user(self):
        user = User.query.get(self.username.data)
        if user is None:
            return None
        m = sha256()
        m.update(self.password.data.encode())
        passwd = m.hexdigest()
        return user if passwd == user.password else None

@app.route("/")
def accueil():
    return render_template(
        "Accueil.html"
    )

@app.route("/aPropos")
def aPropos():
    return render_template(
        "aPropos.html"
    )

@app.route("/Inscription")
def lnscription():
    return render_template(
        "Inscription.html"
    )

@app.route("/ListeDesAlbums")
def listeDesAlbums():
    return render_template(
        "ListeDesAlbums.html",
        albums = get_sample()
    )

@app.route("/login")
def login():
    return render_template(
        "Login.html"
    )

@app.route("/ModificationAlbum")
def modificationAlbum():
    return render_template(
        "ModificationAlbum.html"
    )

@app.route("/ModificationArtiste")
def modificationArtiste():
    return render_template(
        "ModificationAriste.html"
    )

@app.route("/Recherche")
def recherche():
    return render_template(
        "Recherche.html"
    )

