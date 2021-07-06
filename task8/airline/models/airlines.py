import collections

from airline.exceptions import ObjectIsNotAircraftError


class Airline(collections.deque):
    def __init__(self, name, supported_types, initial_aircrafts):
        self.name = name
        self.types = self._init_types(supported_types)
        super().__init__(self._initial_values(initial_aircrafts))

    def _initial_values(self, dict_):
        aircrafts = []
        for key, value in dict_.items():
            if key in self.types.keys():
                for id_ in range(1, value + 1):
                    aircrafts.append(self.types[key](id_=id_, name=f'Default {key}', location=self.name))
        return aircrafts

    def _init_types(self, supported_types):
        return {i.__name__.lower().replace('aircraft', ''): i for i in supported_types}

    def append(self, *args):
        for aircraft in args:
            if isinstance(aircraft, tuple(self.types)):
                self.append(aircraft)
            else:
                raise ObjectIsNotAircraftError

    def total_capacity(self):
        return sum(aircraft.capacity for aircraft in self)

    def sort_by_range(self):
        return sorted(self, key=lambda aircraft: aircraft.max_range)

    def find_aircrafts(self, params=None):
        def _filter_by_params(el):
            """Main logic of this filter is count of required params(that not null) and compare with passed"""
            required = 0
            passed = 0
            for key, value in params.items():
                if value:
                    if key == 'name':
                        required += 1
                        if value.lower() in el.name.lower():
                            passed += 1
                    if key == 'location':
                        required += 1
                        if value == el.location:
                            passed += 1
                    if key == 'capacity':
                        required += 1
                        if value['from'] <= el.capacity <= value['til']:
                            passed += 1
                    if key == 'max_range':
                        required += 1
                        if value['from'] <= el.max_range <= value['til']:
                            passed += 1
            return required == passed

        return list(filter(_filter_by_params, self))
