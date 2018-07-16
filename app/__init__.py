import os
from . views import *
# instantiate flask app
from flask_api import FlaskAPI

from app.models import Entry
from app.views import entries_bp, ent_bp

# local import
from instance.config import app_config

def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    return app
    
config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name)
# register the blueprints
app.register_blueprint(ent_bp)
app.register_blueprint(entries_bp)
