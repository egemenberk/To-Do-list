from flask import Flask
import os
import connexion
from flask_migrate import Migrate

from models import db

def create_app():

    connex_app = connexion.App(__name__, specification_dir='./')
    connex_app.add_api('swagger.yml')

    app = connex_app.app

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///todo_list"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)
    return app

