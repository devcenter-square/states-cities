from flask import Flask
app = Flask(__name__)

from app.mod_endpoints.controllers import mod_endpoints as endpoints_module

# Register blueprint(s)
app.register_blueprint(endpoints_module)

