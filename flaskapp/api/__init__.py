from flask import Flask
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy

from config import config

# this must happen before importing the resources ...
db = SQLAlchemy()

# from .resources.cookie import CookieAPI, CookieListAPI
from api.resources.cookie import CookieListAPI, CookieAPI


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # initialize the DB using the app config info
    db.init_app(app)

    # initialize the API object:
    api_obj = Api(app)

    # set entry points
    api_obj.add_resource(
        CookieListAPI, '/cookies/api/v1.0/cookies', endpoint='cookies'
    )
    api_obj.add_resource(
        CookieAPI, '/cookies/api/v1.0/cookies/<int:id>', endpoint='cookie'
    )

    return app
