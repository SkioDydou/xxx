from .app import app, db
from flask import render_template, url_for, redirect, flash, request
from .models import get_sample, get_details, get_author, get_albums_by_author, get_author_by_name, Author, User, Album
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, PasswordField
from wtforms.validators import DataRequired
from hashlib import sha256
from flask_login import login_user, current_user, logout_user, login_required

class AuthorForm(FlaskForm):
    id = HiddenField('id')
    title = StringField('nom', validators = [DataRequired()])

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

@app.route("/ModificationAlbum/<id>")
def modificationAlbum(id):
    return render_template(
        "ModificationAlbum.html",
        album = get_details(id)
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
@app.route("/edit/author/")
@app.route("/edit/author/<int:id>")
def edit_author(id = None):
    nom = None
    if id is not None:
        a = get_details(id)
        nom = a.title
    else:
        a = None
    f = AuthorForm(id = id, name = nom)
    return render_template("edit-author.html", album = a, form = f)

@app.route("/save/author/", methods=["POST"])
def save_author():
    a = None
    f = AuthorForm()
    if f.validate_on_submit():
        if f.id.data != "":
            id = int(f.id.data)
            a = get_details(id)
            a.title = f.title.data
        else:
            a = Album(title = f.title.data)
            db.session.add(a) 
        db.session.commit()
        id = a.id
        return redirect(url_for('listeDesAlbums', id = id))
    return render_template("edit-author.html", album = a, form = f)

@app.route('/author/<int:id>')
def one_author(id):
    return render_template('edit-author.html',
    author = get_author(id),
    albums = get_albums_by_author(id)
    )