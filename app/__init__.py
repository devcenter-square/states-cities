from flask import Flask, jsonify

app = Flask(__name__)

from app.mod_endpoints.controllers import mod_endpoints as endpoints_module
from app.mod_endpoints.exceptions import InvalidAPIUsage

# Register blueprint(s)
app.register_blueprint(endpoints_module)

@app.errorhandler(InvalidAPIUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
