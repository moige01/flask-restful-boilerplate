import click
from flask import Flask
from .config import *
from .Controllers import Apiv1Routes, ErrorRoutes
from .Models import User, Database 

# App init
app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
app.config.from_object(DevelopmentConfig)

# Database and Marshmallow init to avoid cycling import
Database.db.init_app(app)
Database.ma.init_app(app)

# Blueprint register
app.register_blueprint(Apiv1Routes.bp, url_prefix='/api/v1')
app.register_blueprint(ErrorRoutes.bp)

# CLI
@app.cli.command()
def init_db(): 
    click.echo('Dropping tables')
    Database.db.drop_all()
    click.echo('Creating tables')
    Database.db.create_all()
    Database.db.session.commit()

