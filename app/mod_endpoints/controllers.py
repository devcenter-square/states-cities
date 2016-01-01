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

@mod_endpoints.route('/state/<state_name_or_code>', methods=['GET'])
def get_state(state_name_or_code):
    state = State.get_one_state(urllib.unquote(state_name_or_code))
    return Response(dumps(state), mimetype='application/json')

@mod_endpoints.route('/state/<state_name_or_code>/lgas', methods=['GET'])
def get_lgas(state_name_or_code):
    lgas = LGA.get_all_lgas(urllib.unquote(state_name_or_code))
    return Response(dumps(lgas), mimetype='application/json')

@mod_endpoints.route('/state/<state_name_or_code>/cities', methods=['GET'])
def get_cities(state_name_or_code):
    cities = LGA.get_all_cities(urllib.unquote(state_name_or_code))
    return Response(dumps(cities), mimetype='application/json')
