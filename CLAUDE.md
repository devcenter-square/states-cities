# States & Cities API

A public REST API providing Nigerian states, cities, and local government areas (LGAs). Built with Python 2 / Flask, backed by Parse as the data store.

## Project Structure

```
app/
  __init__.py              # Flask app setup, Parse connection, error handler registration
  mod_endpoints/
    __init__.py
    controllers.py         # Blueprint with API route handlers (url prefix: /api/v1)
    models.py              # Parse ORM models (State, LGA) with query methods
    exceptions.py          # InvalidAPIUsage custom exception class
run.py                     # Local dev server (0.0.0.0:8080)
passenger_wsgi.py          # WSGI entry point for production (Passenger)
requirements.txt           # Pinned Python 2 dependencies
```

## API Endpoints

All routes are under `/api/v1`:

- `GET /states` — list all states
- `GET /state/<name_or_code>` — single state by name or 2-letter code
- `GET /state/<name_or_code>/lgas` — LGAs for a state
- `GET /state/<name_or_code>/cities` — cities for a state (LGAs with `city=True`)

## Key Details

- **Python 2**: Uses Python 2 syntax (`print` statement, `except X, e:` form, `urllib.unquote`).
- **Parse backend**: Data is stored in Parse (connected via `parse_rest`). Models extend `parse_rest.datatypes.Object`. Parse keys are in `app/__init__.py`.
- **State lookup**: 2-character input is treated as a state code (uppercased); longer input is treated as a state name (title-cased).
- **No tests**: There is no test suite.

## Running Locally

```bash
pip install -r requirements.txt
python run.py
# Server starts at http://localhost:8080
```
