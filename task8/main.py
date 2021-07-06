import os
import random

from airline.models.aircrafts import PassengerAircraft
from airline.models.aircrafts import MilitaryAircraft
from airline.models.aircrafts import DroneAircraft
from airline.models.airlines import Airline

AIRCRAFTS_INITIAL = {
    'military': 2,
    'passenger': 5,
    'drone': 3,
}

AIRCRAFT_TYPES = [MilitaryAircraft, PassengerAircraft, DroneAircraft]

params = {
    'name': 'default',
    'location': '',
    'capacity': {
        'from': 100,
        'til': 150,
    },
    'max_range': {
        'from': 10_000,
        'til': 17_000,
    }
}

if __name__ == '__main__':
    print('          _____ _____  _      _____ _   _ ______ ')
    print('    /\   |_   _|  __ \| |    |_   _| \ | |  ____|')
    print('   /  \    | | | |__) | |      | | |  \| | |__'   )
    print('  / /\ \   | | |  _  /| |      | | | . ` |  __|  ')
    print(' / ____ \ _| |_| | \ \| |____ _| |_| |\  | |____ ')
    print('/_/    \_\_____|_|  \_\______|_____|_| \_|______|')
    airline = Airline(input('Enter airline name: '), AIRCRAFT_TYPES, AIRCRAFTS_INITIAL)
    print(f'Airline name: "{airline.name}"')
    for aircraft in airline:
        aircraft.capacity = random.randint(100, 200)
        aircraft.max_range = random.randint(10_000, 20_000)
    print(f'Airline aircrafts: {airline}\n')
    print(f'Airline total capacity: {airline.total_capacity()}\n')
    print(f'Sorted aircrafts by range: {airline.sort_by_range()}\n')
    print(f'Aircrafts by params: {airline.find_aircrafts(params)}')

