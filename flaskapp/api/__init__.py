from flask import Flask
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy

from config import config

# this must happen before importing the resources to avoid import conflicts
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # initialize the DB using the app config info
    db.init_app(app)

    # initialize the API object:
    from api.resources.cookie import CookieListAPI, CookieAPI
    api_obj = Api(app)

    # set entry points
    api_obj.add_resource(
        CookieListAPI, '/v1.0/cookies', endpoint='cookies',
        subdomain='api'
    )
    api_obj.add_resource(
        CookieAPI, '/v1.0/cookies/<int:id>', endpoint='cookie',
        subdomain='api'
    )

    return app
