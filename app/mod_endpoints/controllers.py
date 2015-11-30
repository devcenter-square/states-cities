from flask import Blueprint, Response
from json import dumps
# Import module models
from app.mod_endpoints.models import State
from app.mod_endpoints.models import LGA

# Define the blueprint: 'endpoints', set its url prefix: app.url/api/v1
mod_endpoints = Blueprint('api/v1', __name__, url_prefix='/api/v1')


# Set the route and accepted methods
@mod_endpoints.route('/states', methods=['GET'])
def get_states():
    states = State.get_all_states()
    return Response(dumps(states), mimetype='application/json')


@mod_endpoints.route('/state_with_code/<state_code>', methods=['GET'])
def get_state_with_state_code(state_code):
    state = State.get_one_state_with_state_code(state_code.upper())
    return Response(dumps(state), mimetype='application/json')


@mod_endpoints.route('/state_with_name/<state_name>', methods=['GET'])
def get_state(state_name):
    state = State.get_one_state(state_name.capitalize())
    return Response(dumps(state), mimetype='application/json')


@mod_endpoints.route('/lgas_with_state_name/<state_name>/', methods=['GET'])
def get_lgas(state_name):
    lgas = LGA.get_all_lgas_with_state_name(state_name.capitalize())
    return Response(dumps(lgas), mimetype='application/json')


@mod_endpoints.route('/lgas_with_state_code/<state_code>/', methods=['GET'])
def get_lgas_with_state_code(state_code):
    lgas = LGA.get_all_lgas_with_state_code(state_code.upper())
    return Response(dumps(lgas), mimetype='application/json')



