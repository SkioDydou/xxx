import click
from .app import app, db

@app.cli.command()
@click.argument('filename')
def loaddb(filename):
    ''' Creates the tables and populates them with data. '''

    db.create_all()
    artistes = yaml.load(open (artiste.yml))
    albums = yaml.load(open (album.yml))
    
    for z in albums:
        w = Album(
            id = z["id"],
            titre = z["titre"],
            nomArtiste = z["nomArtiste"],
            nombreSons = z["nombreSons"],
            genre = z["genre"],
            img = z["img"]
        )
        db.session.add(w)
    db.session.commit()
    
    for b in books:
        a = authors[b["author"]]
        o = Book(
            price = b["price"],
            title = b["title"],
            url = b["url"],
            img = b["img"],
            author_id = a.id
        )
        db.session.add(o)
    db.session.commit()
    

@app.cli.command()
def syncdb():
    db.create_all()

