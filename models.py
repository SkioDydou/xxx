from .app import db, login_manager
from flask_login import UserMixin

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    def __repr__(self):
        return (self.name)

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    img = db.Column(db.String(1000))
    annee = db.Column(db.String(100))
    genre = db.Column(db.String(100))
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("Author", backref = db.backref("albums", lazy="dynamic"))
    def __repr__(self):
        return "<Album : (%d) %s>" % (self.id, self.title)

@login_manager.user_loader
def load_user(username):
    return User.query.get(username)

from flask_login import UserMixin
class User(db.Model, UserMixin):
    __tablename__='user'
    username    = db.Column(db.String(50), primary_key=True)
    password    = db.Column(db.String(64))
    nom         = db.Column(db.String(72))
    prenom      = db.Column(db.String(72))
    email       = db.Column(db.String(120), nullable=False)


    def get_id(self):
        return self.username


def get_sample():
    return Album.query.all()


def get_details(id):
    #return Album.query.get(id)
    return Album.query.get_or_404(id)

def get_details2(id):
    return Author.query.get_or_404(id)

def get_author(id):
    return Author.query.get_or_404(id)

def get_albums_by_author(id):
    return Album.query.filter(Album.author_id == id).all()
    
def get_author_by_name(name):
    if Author.query.filter(Author.name == name).all():
        return Author.query.filter(Author.name == name).one() 
    else:
        return None

@login_manager.user_loader
def load_user(username):
    return User.query.get(username)


def sup_album(id):
    return Album.query.filter(Album.id==id).delete()

