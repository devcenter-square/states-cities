from flask import Blueprint, Response
from json import dumps

# Import module models
from app.mod_endpoints.models import State
from app.mod_endpoints.models import LocalGovernmentArea

# Define the blueprint: 'endpoints', set its url prefix: app.url/api/v1
mod_endpoints = Blueprint('api/v1', __name__, url_prefix='/api/v1')

# Set the route and accepted methods
@mod_endpoints.route('/states', methods=['GET'])
def get_states():
    states = State.get_all_states()
    return Response(dumps(states), mimetype='application/json')

@mod_endpoints.route('/<state_name>/lgas', methods=['GET'])
def get_lgas(state_name):
    lgas = LocalGovernmentArea.get_all_lgas_with_state_name(state_name)
    return Response(dumps(lgas), mimetype='application/json')

@mod_endpoints.route('/<state_name>', methods=['GET'])
def get_state(state_name):
    state = State.get_one_state(state_name)
    return Response(dumps(state), mimetype='application/json')
