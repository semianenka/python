import csv
import json
from pathlib import Path
from datetime import datetime

import yaml

import exceptions as ex


class PrizesParser:
    def __init__(self, input_):
        if not Path(input_).exists():
            raise FileNotFoundError()
        self.input = json.loads(open(input_).read())
        self.datetime_now_str = datetime.now().strftime('%d-%m-%Y - %H-%M-%S')
        self.output_csv = csv.writer(open(fr'{self.datetime_now_str}.csv', 'a+', encoding='utf-8', newline=''),
                                     delimiter=',')
        self.output_yaml = open(fr'{self.datetime_now_str}.yaml', 'a+', encoding='utf-8')

    def _get_dict_of_values(self, fields):
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
        return data

    def _dict_to_yaml_format(self, dict_):
        return {
            f'{dict_["id"]}': {key: value for key, value in dict_.items() if key != 'id'}
        }

    def _write_csv(self, data):
        self.output_csv.writerow(data)

    def _write_yaml(self, data):
        yaml.dump(data, self.output_yaml)

    def parse(self):
        DATA_TO_PARSE = 'prizes'
        ROW_TO_PARSE = 'laureates'

        try:
            if DATA_TO_PARSE not in self.input:
                raise ex.DataNotFoundError('Data not found', DATA_TO_PARSE)
            headers = ['id', 'firstname', 'surname', 'motivation', 'year', 'category']
            self._write_csv(headers)
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
                        data = self._get_dict_of_values(fields)
                        self._write_csv(list(data.values()))
                        self._write_yaml(self._dict_to_yaml_format(data))
                except ex.RowNotFoundError as e:
                    print(f'An error {e.__class__.__name__} was occurred: '
                          f'{e.row} were missing, row skipped')
        except ex.DataNotFoundError as e:
            print(f'An error {e.__class__.__name__} was occurred: '
                  f'Not found data {e.data}')
