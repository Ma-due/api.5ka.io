from flask import Flask
from flask_smorest import Api
from resources.projects import blp as ProjectBlueprint
from resources.teams import blp as TeamsBlueprint
from db import db
import auth
import models

def create_app():
    app = Flask(__name__)
    login = auth.info
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dbuser:1234@1.220.201.109:33306/5ka'
    #app.config["SQLALCHEMY_DATABASE_URI"] = ('mysql+pymysql://'+login[user]+':'+login[passwd]+'@'+login[host]+'/'+login[db])
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(TeamsBlueprint)
    api.register_blueprint(ProjectBlueprint)

    return app