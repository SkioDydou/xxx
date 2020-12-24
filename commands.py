import click
from .app import app, db
from .models import artiste, album


@app.cli.command()
@click.argument('filename')
def loaddb(filename):
    '''
     Create all tables and populate them with data in filename
    '''
    db.create_all()

    import yaml
    test = yaml.load(open(filename))
    db.session.commit()