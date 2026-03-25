from flask import Blueprint, jsonify
from app.mod_endpoints.models import State
from app.mod_endpoints.models import LGA

# Define the blueprint: 'endpoints', set its url prefix: app.url/api/v1
mod_endpoints = Blueprint('api/v1', __name__, url_prefix='/api/v1')


@mod_endpoints.route('/states', methods=['GET'])
def get_states():
    return jsonify(State.get_all_states())

@mod_endpoints.route('/state/<state_name_or_code>', methods=['GET'])
def get_state(state_name_or_code):
    return jsonify(State.get_one_state(state_name_or_code))

@mod_endpoints.route('/state/<state_name_or_code>/lgas', methods=['GET'])
def get_lgas(state_name_or_code):
    return jsonify(LGA.get_all_lgas(state_name_or_code))

@mod_endpoints.route('/state/<state_name_or_code>/cities', methods=['GET'])
def get_cities(state_name_or_code):
    return jsonify(LGA.get_all_cities(state_name_or_code))
