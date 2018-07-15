# app/views.py

# contains routes

from flask import Flask, Blueprint, jsonify, request, make_response

# create entries and a single entry Blueprint and
# version the urls to have '/api/v1' prefix
entries_bp = Blueprint('entries',__name__, url_prefix='/api/v1')

ent_bp = Blueprint('ent', __name__, url_prefix='/api/v1')

@entries_bp.route('/', methods=['POST', 'GET'])
def index():
    """ root """
    if request.method == 'GET':

        # the following is a welcoming message (at the landing page)
        welcome_message = {"Message": [{
                                    "Welcome":"Hey! welcome thriller diary api"
                                    },
                                  ]}
        return make_response(jsonify(welcome_message)), 200

@entries_bp.route('/entries', methods=['GET'])
def entries():
    """Retrives all Entries"""
    if request.method == 'GET':
        return "OK! entries"