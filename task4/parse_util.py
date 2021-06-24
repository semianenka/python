import csv
import json
from pathlib import Path

import exceptions as ex


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
                    raise ex.CustomKeyNotFoundError('Key not found', key)
                data[key] = value[key]
            except ex.CustomKeyNotFoundError as e:
                data[key] = None
                print(f'An error {e} was occurred: '
                      f'Parser wrote None on {e.key} position because value is missing')
        return dict_to_list(data)

    def writeline(self, data):
        self.output.writerow(data)

    def parse(self):
        DATA_TO_PARSE = 'prizes'
        ROW_TO_PARSE = 'laureates'

        try:
            if DATA_TO_PARSE not in self.input:
                raise ex.DataNotFoundError('Data not found', DATA_TO_PARSE)
            for row in self.input['prizes']:
                try:
                    if ROW_TO_PARSE not in row.keys():
                        raise ex.RowNotFoundError('Row not found', ROW_TO_PARSE)
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
                except ex.RowNotFoundError as e:
                    print(f'An error {e.__class__.__name__} was occurred: '
                          f'{e.row} were missing, row skipped')
        except ex.DataNotFoundError as e:
            print(f'An error {e.__class__.__name__} was occurred: '
                  f'Not found data {e.data}')
