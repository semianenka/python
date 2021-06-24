import csv
import json
from pathlib import Path


class Parser:
    def __init__(self, input_, output_):
        if not Path(input_).exists():
            raise FileNotFoundError
        self.input = json.loads(open(input_).read())

        if Path(output_).exists():
            raise FileExistsError
        self.output = csv.writer(open(output_, 'w', encoding='utf-8', newline=''), delimiter=',')

    def get_list_of_values(self, fields):
        def dict_to_list(dict_):
            return list(dict_.values())

        data = {}
        for key, value in fields.items():
            try:
                if key not in value:
                    raise CustomKeyNotFoundError('Key not found', key)
                data[key] = value[key]
            except CustomKeyNotFoundError as e:
                data[key] = None
                print(f'An error {e} was occurred: '
                      f'Parser wrote None on {e.key} position because value is missing')
        return dict_to_list(data)

    def writeline(self, data):
        self.output.writerow(data)

    def parse(self):
        try:
            for row in self.input['prizes']:
                try:
                    for laureate in row['laureates']:
                        fields = {
                            'id': laureate,
                            'firstname': laureate,
                            'surname': laureate,
                            'motivation': laureate,
                            'year': row,
                            'category': row
                        }
                        data = self.get_list_of_values(fields)
                        self.writeline(data)
                except KeyError as e:
                    print(f'An error {e.__class__.__name__} was occurred: '
                          f'Laureates were missing, row skipped')
        except KeyError as e:
            print(f'An error {e.__class__.__name__} was occurred: '
                  f'Critical failure')


class CustomKeyNotFoundError(Exception):
    def __init__(self, message, key):
        self.message = message
        self.key = key
        super().__init__(self.message)
