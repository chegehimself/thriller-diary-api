import os

from flask_api import FlaskAPI
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

    return app
    
config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name)
# register the blueprints
app.register_blueprint(ent_bp)
app.register_blueprint(entries_bp)
