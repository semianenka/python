from random import randint


class BaseAircraft:
    def __init__(self, name, location, id=None, fuel=None, weight=None,
                 speed=None, capacity=None, max_range=None, *args, **kwargs):
        self.id = id
        self.name = name
        self.fuel = fuel
        self.weight = weight
        self.speed = speed
        self.capacity = capacity or randint(100, 200)
        self.max_range = max_range or randint(10_000, 20_000)
        self.location = location

    def departure(self, city):
        self.location = city

    def __repr__(self):
        return f'{self.__class__.__name__}[{self.id}, {self.name}, {self.location}, {self.capacity}, {self.max_range}]'
