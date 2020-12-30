import click
from .app import app, db
import yaml
from .models import Author, User, Album
from hashlib import sha256

@app.cli.command()
@click.argument('filename')
def loaddb(filename):
    ''' Creates the tables and populates them with data. '''

    db.create_all()
    albums = yaml.load(open (filename))
    authors = {}

    for x in albums:
        a = x["author"]
        if a not in authors:
            u = Author(name = a)
            db.session.add(u)
            authors[a] = u
    db.session.commit()

    for x in albums:
        a = authors[x["author"]]
        u = Album(
            title = x["title"],
            img = x["img"],
            annee = x["annee"],
            genre = x["genre"],
            author_id = a.id
        )
        db.session.add(u)
    db.session.commit()

    
@app.cli.command()
def syncdb():
    db.create_all()

@app.cli.command()
@click.argument('username')
@click.argument('password')
def newuser(username, password):
    m = sha256()
    m.update(password.encode())
    u = User(username = username, password = m.hexdigest())
    db.session.add(u)
    db.session.commit()

@app.cli.command()
@click.argument('username')
@click.argument('password')
def passwd(username, password):
    m = sha256()
    m.update(password.encode())
    u = User.query.get(username)
    if u:
        u.password = m.hexdigest()
        db.session.commit()
    else:
        print("****************************************************")
        print("Il n'y a pas de compte associé au pseudo " + username)
        print("****************************************************")
