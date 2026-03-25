import json
import os
from app.mod_endpoints.exceptions import InvalidAPIUsage

_data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'states.json')
with open(_data_path) as f:
    _states = json.load(f)

# Build lookup indexes
_by_name = {s['name'].lower(): s for s in _states}
_by_code = {s['code'].upper(): s for s in _states}


class State:
    @staticmethod
    def _as_dict(s):
        return {
            'name': s['name'],
            'capital': s['capital'],
            'latitude': s['latitude'],
            'longitude': s['longitude'],
        }

    @classmethod
    def find_by_name_or_code(cls, state_name_or_code):
        key = state_name_or_code.strip()
        if len(key) == 2:
            state = _by_code.get(key.upper())
        else:
            state = _by_name.get(key.lower())
        if state is None:
            raise InvalidAPIUsage(
                "State with state name or code '{}' does not exist".format(state_name_or_code),
                status_code=404
            )
        return state

    @staticmethod
    def get_all_states():
        return [State._as_dict(s) for s in _states]

    @staticmethod
    def get_one_state(state_name_or_code):
        return State._as_dict(State.find_by_name_or_code(state_name_or_code))


class LGA:
    @staticmethod
    def get_all_lgas(state_name_or_code):
        state = State.find_by_name_or_code(state_name_or_code)
        return [{'name': lga} for lga in state['lgas']]

    @staticmethod
    def get_all_cities(state_name_or_code):
        state = State.find_by_name_or_code(state_name_or_code)
        return [{'name': city} for city in state.get('cities', [])]
