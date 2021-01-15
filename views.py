from .app import app, db
from flask import render_template, url_for, redirect, flash, request, Flask, request, jsonify
from .models import *
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired
from hashlib import sha256
from flask_login import login_user, current_user, logout_user, login_required

###################### FORMULAIRES ###################### 

class AlbumForm(FlaskForm):
    id = HiddenField('id')
    title = StringField('Modifier le nom', validators = [DataRequired()])
    annee = IntegerField('Modifier l\'annee', validators = [DataRequired()])
    genre = StringField('Modifier le genre', validators = [DataRequired()])
    auteur = StringField('Modifier l\'auteur', validators = [DataRequired()])
    img = StringField('Modifier l\'image', validators = [DataRequired()])

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

class InscriptionForm(FlaskForm):
    username    = StringField('Username')
    prenom      = StringField('First name')
    nom         = StringField('Last name')
    email       = StringField('Email')
    password    = PasswordField('Password')
    confirmePsw = PasswordField('Confirm Password')

    def valideUsername(self):
        user = User.query.get(self.username.data)
        if user is None:
            print(self.confirmePsw.data)
            return self if self.confirmePsw.data == self.password.data else 2
        else :
            return 1;

class CreationAlbumForm(FlaskForm):
    id = HiddenField('id')
    title = StringField('Ajouter un nom', validators = [DataRequired()])
    annee = IntegerField('Ajouter une annee', validators = [DataRequired()])
    genre = StringField('Ajouter un genre', validators = [DataRequired()])
    auteur = StringField('Ajouter un auteur', validators = [DataRequired()])
    img = StringField('Ajouter une image', validators = [DataRequired()])

###################### Routes ###################### 

@app.route("/add_album/", methods=("GET", "POST"))
@login_required
def add_album():
    a = None
    f = CreationAlbumForm()
    if f.validate_on_submit():
        title = f.title.data
        a = Album(img=f.img.data,
                title=f.title.data,
                genre=f.genre.data,
                annee=f.annee.data,
                auteur=f.auteur.data)
        db.session.add(a)
        db.session.commit()
        return redirect(url_for('listeDesAlbums'))
    return render_template("add_album.html", album = a, form = f,
    title="Ajouter Album")

@app.route("/")
def accueil():
    return render_template(
        "Accueil.html",
        title="PasSpotify"
    )

@app.route("/aPropos/")
def aPropos():
    return render_template(
        "aPropos.html",
        title="A Propos"
    )


@app.route("/listeDesAlbums/")
def listeDesAlbums():
    return render_template(
        "ListeDesAlbums.html",
        albums = get_sample(),
        title="Liste Des Albums"
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
        "Login.html", form = f,
        title="Login"
    )
    
from flask_login import logout_user
@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for('accueil'))

@app.route("/modificationAlbum/<id>")
def modificationAlbum(id):
    return render_template(
        "ModificationAlbum.html",
        album = get_details(id),
        title="Modification Album"
    )


@app.route("/delete/album/<int:id>")
def delete_album(id):
    sup_album(id)
    db.session.commit()
    return redirect(url_for('listeDesAlbums'))

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
    return render_template("edit_album.html", album = a, form = f,
    title="Edition Album")

@app.route("/save/album/", methods=["POST"])
def save_album():
    a = None
    f = AlbumForm()
    if f.validate_on_submit():
        if f.id.data != "":
            id = int(f.id.data)
            b = get_author(id)
            a = get_details(id) 
            a.title = f.title.data
            a.annee = f.annee.data
            a.genre = f.genre.data
            a.img   = f.img.data
            a.auteur = f.auteur.data
        db.session.commit()
        return redirect(url_for('listeDesAlbums', id = id))
    return render_template("edit_album.html", album = a, form = f,
    title="Sauvegarde Album")

@app.route('/album/<int:id>')
def one_author(id):
    return render_template('edit_album.html',
    author = get_author(id),
    albums = get_albums_by_author(id),
    title="PasSpotify"
    )

@app.route("/inscription/", methods=("GET","POST",))
def inscription():
    erreur = 0
    f = InscriptionForm()
    if f.validate_on_submit():
        user = f.valideUsername()
        if user!=1 and user!=2 and user :
            m = sha256()
            m.update(user.password.data.encode())
            u = User(username=user.username.data, prenom=user.prenom.data,
            nom=user.nom.data, email=user.email.data, password=m.hexdigest())
            db.session.add(u)
            db.session.commit()
            login_user(u)
            return redirect(url_for('accueil'))
        elif(user == 1):
            erreur = 1

        else :
            erreur = 2
    return render_template("Inscription.html",form=f, erreur=erreur, title="Inscription")



@app.route("/recherche/", methods=['POST', 'GET'])
def search():
    liste_albums = []
    recherche = ""
    type_recherche = ""
    liste_albums=get_sample()
    if request.method == "POST":
        recherche = request.form.get('research')
        type_recherche = request.form.get('type_research')
        if type_recherche == "Titre":
            liste_albums = recherche_titre(recherche)
        elif type_recherche == "Annee":
            liste_albums = recherche_annee(recherche)
        elif type_recherche == "Auteur":
            liste_albums = recherche_auteur(recherche)
        else:
            type_recherche == "Genre"
            liste_albums = recherche_genre(recherche)
    return render_template(
        "Recherche.html",
        type_recherche=type_recherche,
        recherche=recherche,
        la_liste=liste_albums)