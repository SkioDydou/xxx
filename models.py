from .app import db

class album(db.Model):
    id  =   db.Column(db.Integer, primary_key=True)
    titre    =  db.Column(db.String(100))
    nomArtiste  =   db.Column(db.String(100))
    nombreSons  =   db.Column(db.Integer)
    genre   =   db.Column(db.String(100))
    img =   db.Column(db.String(100))

class artiste(db.Model):
    id  =   db.Column(db.Integer, primary_key=True)
    nomDeScene  =   db.Column(db.String(100))
    prenom  =   db.Column(db.String(100))
    dateNaiss   =   db.Column(db.String(100))
    img =   db.Column(db.String(100))

def get_titre(self):
    return self.titre