from .app import db, login_manager
from flask_login import UserMixin

###################### AUTEUR ######################

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    def __repr__(self):
        return (self.name)

def get_author_by_name(name):
    if Author.query.filter(Author.name == name).all():
        return Author.query.filter(Author.name == name).one() 
    else:
        return None

def get_author(id):
    return Author.query.get_or_404(id)

def get_auteurs():
    return Author.query.filter(Auteur.name).all()

###################### ALBUM ###################### 

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    img = db.Column(db.String(1000))
    annee = db.Column(db.String(100))
    genre = db.Column(db.String(100))
    auteur = db.Column(db.String(100))
    note = db.Column(db.String(100))
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("Author", backref = db.backref("albums", lazy="dynamic"))
    def __repr__(self):
        return "<Album : (%d) %s>" % (self.id, self.title)

@login_manager.user_loader
def load_user(username):
    return User.query.get(username)

def get_sample():
    return Album.query.all()

def get_album(title):
    return Album.query.get_or_404(titre)

def get_details(id):
    return Album.query.get_or_404(id)

def recherche_titre(recherche):
    return Album.query.filter(Album.title.contains(recherche)).order_by(Album.title.asc()).all()

def recherche_annee(recherche):
    return Album.query.filter(Album.annee.contains(recherche)).order_by(Album.annee.asc()).all()

def recherche_auteur(recherche):
    return Album.query.filter(Album.auteur.contains(recherche)).order_by(Album.auteur.asc()).all()

def recherche_genre(recherche):
    return Album.query.filter(Album.genre.contains(recherche)).order_by(Album.genre.asc()).all()

def get_albums_by_author(id):
    return Album.query.filter(Album.author_id == id).all()

def sup_album(id):
    return Album.query.filter(Album.id==id).delete()



###################### USER ###################### 

class User(db.Model, UserMixin):
    __tablename__='user'
    username    = db.Column(db.String(50), primary_key=True)
    password    = db.Column(db.String(64))
    nom         = db.Column(db.String(72))
    prenom      = db.Column(db.String(72))
    email       = db.Column(db.String(120), nullable=False)

    def get_id(self):
        return self.username

@login_manager.user_loader
def load_user(username):
    return User.query.get(username)