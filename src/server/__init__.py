import logging
import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_restless import APIManager

from .web import main as main_blueprint

db = SQLAlchemy()
migrate = Migrate()

from server.models import * # noqa

def create_app(env=None):
    """
    Bootstrap function to initialize Flask application
    """
    app = Flask(__name__)
    
    if env is None:
        env = os.getenv('OLYMPUS_PROJECT_ENV', 'Dev')
    
    app.config.from_object(f'server.config.{env}Config')

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main_blueprint)
    initialize_resources(app)

    return app


def initialize_resources(app):
    from server.api.health_check import HealthCheckAPI
    from server.api.race_resource import RaceAPI, race_deserializer, race_serializer
    from server.models.race import Race, RaceFollow
    from server.models.user import User
    from server.models.route import Route
    api = Api(
        app,
        default_mediatype='application/json',
        prefix='/api/v1'
    )
    api_manager = APIManager(
        app, 
        flask_sqlalchemy_db=db
    )
    api_manager.create_api(
        Race, 
        methods=['GET', 'PUT'], url_prefix='/api/v2',
        exclude_columns=['race_follows', 'routes', 'user_id'],
        serializer=race_serializer,
        deserializer=race_deserializer
    )
    api_manager.create_api(User, methods=['GET'])
    api_manager.create_api(Route, methods=['GET'])
    api_manager.create_api(RaceFollow, methods=['GET'])
    api.add_resource(HealthCheckAPI, '/health-check/')
    api.add_resource(RaceAPI, '/races/')