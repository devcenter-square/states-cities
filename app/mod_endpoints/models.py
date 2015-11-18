from parse_rest.datatypes import Object

class State(Object):

    def as_dict(self):
        state = {}
        state['name'] = self.name
        state['capital'] = self.cap_city
        state['latitude'] = self.latitude
        state['longitude'] = self.longitude
        state['min-lat'] = self.min_latitude
        state['min-long'] = self.min_longitude
        state['max-lat'] = self.max_latitude
        state['max-long'] = self.max_longitude
        state['state-code'] = self.state_code
        state['state-id'] = self.state_id
        return state

  @staticmethod
  def get_all_states():
    result_set = []
    states = State.Query.all()
    for state in states:
      result_set.append(state.as_dict())
    return result_set

@staticmethod
def get_one_state(state_name):
    result_set = []
    state = State.Query.get(name = state_name).limit(1)
    result_set.append(state.as_dict())
    return result_set

class LocalGovernmentArea(Object):

  def as_dict(self):
    lga = {}
    lga["name"] = self.name
    return lga

  @staticmethod
  def get_all_lgas_with_state_name(state_name):
    result_set = []
    state = State.Query.get(name = state_name).limit(1)
    lgas = LocalGovernmentArea.Query.get(state = state.objectId)
    for LGA in lgas:
        result_set.append(LGA.as_dict())
    return result_set
