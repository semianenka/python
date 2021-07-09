import os

from airline.models import aircrafts
from airline.models.airlines import Airline

initial_aircrafts = {
    aircrafts.MilitaryAircraft: 2,
    aircrafts.PassengerAircraft: 5,
    aircrafts.DroneAircraft: 3,
}

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
    airline = Airline(input('Enter airline name: '), initial_aircrafts)
    print(f'Airline name: "{airline.name}"')
    print(f'Airline aircrafts: {airline}\n')
    print(f'Airline total capacity: {airline.total_capacity()}\n')
    print(f'Sorted aircrafts by range: {airline.sort_by_range()}\n')
    print(f'Aircrafts by params: {airline.find_aircrafts(params)}')
