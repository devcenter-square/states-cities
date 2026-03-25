from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from app.mod_endpoints.controllers import mod_endpoints as endpoints_module
from app.mod_endpoints.exceptions import InvalidAPIUsage

# Register blueprint(s)
app.register_blueprint(endpoints_module)

@app.route('/')
def index():
    return jsonify({
        'message': 'States & Cities API',
        'endpoints': {
            'states': '/api/v1/states',
            'state': '/api/v1/state/<name_or_code>',
            'lgas': '/api/v1/state/<name_or_code>/lgas',
            'cities': '/api/v1/state/<name_or_code>/cities',
        }
    })

@app.errorhandler(InvalidAPIUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
