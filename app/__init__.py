import os
from flask import request
from flask_api import FlaskAPI
from flask_cors import CORS
# local import
from . views import *
from app.models import Entry
from instance.config import app_config

def create_app(config_name):
    # instantiate flask app
    app = FlaskAPI(__name__, instance_relative_config=True)
    
    # app settings config
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    # for cross origin resource sharing
    CORS(app)

    # fix not found error(testing)
    app.url_map.strict_slashes = False

    # register the blueprints
    app.register_blueprint(ent_bp)
    app.register_blueprint(entries_bp)

    @app.errorhandler(404)
    def error_404(error=None):
        message = {
                'status': '404',
                'message': request.url + ' Was not found in this server',
        }
        response = jsonify(message)
        response.status_code = 404

        return response
    return app
