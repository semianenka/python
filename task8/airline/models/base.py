class BaseAircraft:
    def __init__(self, id_, name, location, fuel=None, weight=None, speed=None, capacity=None, max_range=None):
        self.id = id_
        self.name = name
        self.fuel = fuel
        self.weight = weight
        self.speed = speed
        self.capacity = capacity
        self.max_range = max_range
        self.location = location

    def departure(self, city):
        self.location = city

    def __repr__(self):
        return f'{self.__class__.__name__}[{self.id}, {self.name}, {self.location}, {self.capacity}, {self.max_range}]'
