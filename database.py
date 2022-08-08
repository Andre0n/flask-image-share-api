from click import command, echo
from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


def setup(app: Flask) -> None:
    db.init_app(app)
    ma.init_app(app)
    app.db = db
    app.ma = ma


@command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    db.drop_all()
    db.create_all()
    db.session.commit()
    echo('Initialized the database.')
