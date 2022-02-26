from flask import Flask
from flask_migrate import Migrate

from config import app
from models import db

"""
app = Flask(__name__, instance_relative_config=True)
migrate = Migrate(app, db)
from models import *
"""


if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)
