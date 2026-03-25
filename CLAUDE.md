# States & Cities API

A public REST API providing Nigerian states, cities, and local government areas (LGAs). Built with Python 3 / Flask, using a local JSON data file. CORS-enabled.

## Project Structure

```
app/
  __init__.py              # Flask app setup, CORS, error handler registration
  data/
    states.json            # Static dataset: 37 states with codes, capitals, coordinates, LGAs, cities
  mod_endpoints/
    __init__.py
    controllers.py         # Blueprint with API route handlers (url prefix: /api/v1)
    models.py              # State and LGA classes with query methods (reads from states.json)
    exceptions.py          # InvalidAPIUsage custom exception class
tests/
  test_api.py              # API endpoint tests (pytest)
run.py                     # Local dev server (0.0.0.0:8080)
passenger_wsgi.py          # WSGI entry point for production (Passenger)
Procfile                   # Railway/Heroku deployment (gunicorn)
requirements.txt           # Pinned Python 3 dependencies
```

## API Endpoints

All routes are under `/api/v1`:

- `GET /states` — list all states
- `GET /state/<name_or_code>` — single state by name or 2-letter code
- `GET /state/<name_or_code>/lgas` — LGAs for a state
- `GET /state/<name_or_code>/cities` — cities for a state

## Key Details

- **Data source**: All data lives in `app/data/states.json`. No external database or API needed.
- **State lookup**: 2-character input is treated as a state code (uppercased); longer input is matched case-insensitively by name.
- **CORS**: Enabled for all origins via `flask-cors`.

## Running Locally

```bash
pip install -r requirements.txt
python run.py
# Server starts at http://localhost:8080
```

## Running Tests

```bash
pytest tests/ -v
```
