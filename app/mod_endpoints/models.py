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
        state = State.Query.get(name=state_name)
        result_set.append(state.as_dict())
        return state.as_dict()

    @staticmethod
    def get_one_state_with_state_code(code):
        state = State.Query.get(state_code=code)
        return state.as_dict()


class LGA(Object):
    def as_dict(self):
        lga = {}
        lga["name"] = self.name
        return lga

    @staticmethod
    def get_all_lgas_with_state_name(state_name):
        result_set = []
        state_result = State.Query.get(name=state_name)
        print state_result.objectId
        lgas = LGA.Query.filter(state=state_result)
        for lga in lgas:
            result_set.append(lga.as_dict())
        return result_set

    @staticmethod
    def get_all_lgas_with_state_code(code):
        result_set = []
        state_result = State.Query.get(state_code=code)
        lgas = LGA.Query.filter(state=state_result)
        for lga in lgas:
            result_set.append(lga.as_dict())
        return result_set
