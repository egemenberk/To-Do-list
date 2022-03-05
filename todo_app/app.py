import os

import connexion
from flask import Flask
from flask_migrate import Migrate

from todo_app.models import db


def create_app(settings=None):

    connex_app = connexion.App(__name__, specification_dir="./")
    connex_app.add_api("swagger.yml")

    app = connex_app.app
    if not settings:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "DATABASE_URL", "postgresql:///todo_list"
        ).replace("postgres://", "postgresql://")
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    else:
        app.config.update(settings)

    db.init_app(app)
    Migrate(app, db)
    return app
