from parse_rest.datatypes import Object

class State(Object):

  def as_dict(self):
    state = {}
    state['name'] = self.name
    state['latitude'] = self.latitude
    state['longitude'] = self.longitude
    state['min-lat'] = self.min_latitude
    state['min-long'] = self.min_longitude
    state['max-lat'] = self.max_latitude
    state['max-long'] = self.max_longitude
    return state

  @staticmethod
  def get_all_states():
    result_set = []
    states = State.Query.all()
    for state in states:
      result_set.append(state.as_dict())
    return result_set


