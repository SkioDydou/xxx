from .app import db

class Album(db.Model):
    id  =   db.Column(db.Integer, primary_key=True)
    titre    =  db.Column(db.String(100))
    nomArtiste  =   db.Column(db.String(100))
    nombreSons  =   db.Column(db.Integer)
    genre   =   db.Column(db.String(100))
    img =   db.Column(db.String(100))
    def __repr__(self):
        return "<Album (%d) %s>" % (self.id)

class Artiste(db.Model):
    id  =   db.Column(db.Integer, primary_key=True)
    nomDeScene  =   db.Column(db.String(100))
    prenom  =   db.Column(db.String(100))
    dateNaiss   =   db.Column(db.String(100))
    img =   db.Column(db.String(100))
    def __repr__(self):
        return "<Artiste (%d) %s>" % (self.id)

def get_titre(self):
    return self.titre
    
def get_album():
    return Album.query.all()
