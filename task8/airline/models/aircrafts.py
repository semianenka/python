from . import base


class PassengerAircraft(base.BaseAircraft):
    def __init__(self, name, location, id=None, fuel=None, weight=None, speed=None, capacity=None, max_range=None):
        super().__init__(name, location, id, fuel, weight, speed, capacity, max_range)


class DroneAircraft(base.BaseAircraft):
    def __init__(self, name, location, id, fuel=None, weight=None,
                 speed=None, capacity=None, max_range=None, max_height=None):
        super().__init__(name, location, id, fuel, weight, speed, capacity, max_range)
        self.max_height = max_height


class MilitaryAircraft(base.BaseAircraft):
    def __init__(self, name, location, id, fuel=None, weight=None,
                 speed=None, capacity=None, max_range=None, number_of_weapons=None):
        super().__init__(name, location, id, fuel, weight, speed, capacity, max_range)
        self.number_of_weapons = number_of_weapons
