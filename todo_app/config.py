import os
import connexion

basedir = os.path.abspath(os.path.dirname(__file__))

connex_app = connexion.App(__name__, specification_dir='./')
connex_app.add_api('swagger.yml')

app = connex_app.app
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///todo_list"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

