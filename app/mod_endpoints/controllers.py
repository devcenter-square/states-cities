from flask import Blueprint, jsonify, request
from app.mod_endpoints.models import State
from app.mod_endpoints.models import LGA

# Define the blueprint: 'endpoints', set its url prefix: app.url/api/v1
mod_endpoints = Blueprint('api/v1', __name__, url_prefix='/api/v1')


@mod_endpoints.after_request
def add_cache_headers(response):
    response.headers['Cache-Control'] = 'public, max-age=86400'
    return response


@mod_endpoints.route('/', methods=['GET'])
def index():
    return jsonify({
        'message': 'States & Cities API',
        'endpoints': {
            'states': '/api/v1/states',
            'search': '/api/v1/states?q=<query>',
            'state': '/api/v1/state/<name_or_code>',
            'lgas': '/api/v1/state/<name_or_code>/lgas',
            'lga': '/api/v1/state/<name_or_code>/lgas/<lga_name>',
            'cities': '/api/v1/state/<name_or_code>/cities',
        }
    })


@mod_endpoints.route('/states', methods=['GET'])
def get_states():
    query = request.args.get('q', '').strip()
    if query:
        return jsonify(State.search_states(query))
    return jsonify(State.get_all_states())

@mod_endpoints.route('/state/<state_name_or_code>', methods=['GET'])
def get_state(state_name_or_code):
    return jsonify(State.get_one_state(state_name_or_code))

@mod_endpoints.route('/state/<state_name_or_code>/lgas', methods=['GET'])
def get_lgas(state_name_or_code):
    return jsonify(LGA.get_all_lgas(state_name_or_code))

@mod_endpoints.route('/state/<state_name_or_code>/lgas/<lga_name>', methods=['GET'])
def get_lga(state_name_or_code, lga_name):
    return jsonify(LGA.get_one_lga(state_name_or_code, lga_name))

@mod_endpoints.route('/state/<state_name_or_code>/cities', methods=['GET'])
def get_cities(state_name_or_code):
    return jsonify(LGA.get_all_cities(state_name_or_code))
