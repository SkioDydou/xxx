from .app import app
from flask import render_template
from .models import get_titre, Album, Artiste, get_album

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
        albums = get_album()
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
