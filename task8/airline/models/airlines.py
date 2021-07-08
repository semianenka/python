import collections

from airline import exceptions


class Airline(collections.deque):
    def __init__(self, name, initial_aircrafts):
        self.name = name
        self.types = initial_aircrafts.keys()
        super().__init__(self._initial_values(initial_aircrafts))

    def _initial_values(self, initial_aircrafts):
        aircrafts = []
        for class_obj, count in initial_aircrafts.items():
            for _ in range(count):
                aircrafts.append(
                    class_obj(id=len(aircrafts) + 1, name=f'Default {class_obj.__name__}', location=self.name))
        return aircrafts

    def append(self, *args):
        for aircraft in args:
            if isinstance(aircraft, tuple(self.types)):
                aircraft.id = len(self) + 1
                self.append(aircraft)
            else:
                raise exceptions.ObjectIsNotAircraftError

    def total_capacity(self):
        return sum(aircraft.capacity for aircraft in self)

    def sort_by_range(self):
        return sorted(self, key=lambda aircraft: aircraft.max_range)

    def get_by_id(self, id):
        if id <= len(self) - 1:
            return self[id - 1]
        raise exceptions.AircraftNotFoundError

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
