from flask import Blueprint, request, redirect, url_for

# Import module models
# from app.mod_endpoints.models import ...

# Define the blueprint: 'endpoints', set its url prefix: app.url/api/v1
mod_endpoints = Blueprint('api/v1', __name__, url_prefix='/api/v1')

# Set the route and accepted methods
@mod_endpoints.route('/hello', methods=['GET'])
def send_hello():
    return 'hello'
