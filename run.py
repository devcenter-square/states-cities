import os
from app import app

port = int(os.environ.get('PORT', 8080))
debug = os.environ.get('FLASK_DEBUG', '0') == '1'
app.run(host='0.0.0.0', port=port, debug=debug)
