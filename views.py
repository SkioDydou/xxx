from .app import app, db
from flask import render_template, url_for, redirect, flash, request
from .models import get_sample, get_details, get_details2, get_author, get_albums_by_author, get_author_by_name, Author, User, Album
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, PasswordField, IntegerField
from wtforms.validators import DataRequired
from hashlib import sha256
from flask_login import login_user, current_user, logout_user, login_required

class AlbumForm(FlaskForm):
    id = HiddenField('id')
    title = StringField('Modifier le nom', validators = [DataRequired()])
    annee = IntegerField('Modifier l\'annee', validators = [DataRequired()])
    genre = StringField('Modifier le genre', validators = [DataRequired()])
    auteur = StringField('Modifier l\'auteur', validators = [DataRequired()])


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

@app.route("/login/", methods = ["GET", "POST"])
def login():
    f = LoginForm()
    if not f.is_submitted():
        f.next.data = request.args.get("next")
    elif f.validate_on_submit():
        user = f.get_authenticated_user()
        if user:
            login_user(user)
            next = f.next.data or (url_for('accueil'))
            return redirect(next)
    return render_template(
        "Login.html"
    )
@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('accueil'))

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
@app.route("/edit/album/")
@app.route("/edit/album/<int:id>")
def edit_album(id = None):
    albums = get_albums_by_author(id)
    nomAlbum = None
    if id is not None:
        a = get_details(id)
        nomAlbum = a.title
    else:
        a = None
    f = AlbumForm(id = id, name = nomAlbum )
    return render_template("edit-author.html", album = a, form = f)

@app.route("/save/album/", methods=["POST"])
def save_album():
    a = None
    f = AlbumForm()
    if f.validate_on_submit():
        if f.id.data != "":
            id = int(f.id.data)
            b = get_author(id)
            a = get_details(id)
            b.name = f.auteur.data
            a.title = f.title.data
            a.annee = f.annee.data
            a.genre = f.genre.data
        db.session.commit()
        return redirect(url_for('listeDesAlbums', id = id))
    return render_template("edit-author.html", album = a, form = f)

@app.route('/album/<int:id>')
def one_author(id):
    return render_template('edit-author.html',
    author = get_author(id),
    albums = get_albums_by_author(id)
    )