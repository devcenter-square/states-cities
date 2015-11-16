from flask import Flask
from parse_rest.connection import register

app = Flask(__name__)

from app.mod_endpoints.controllers import mod_endpoints as endpoints_module

# Register blueprint(s)
app.register_blueprint(endpoints_module)

#connect to Parse
register('azP8OG6mI6hw4OQC4hl5La5B2me8b2yk67qTTJVl', 'PWT4hbPVtZ59MU73OfIxjhpCVIkqXYOOb4LY8ars')

