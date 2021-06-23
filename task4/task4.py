import parse_util

used = [1, 3, 2, 4, 3]
dirty_input = [1, 3, 2, 2, 4, 3, 3, 3]

keys = ['C', 'Lua', 'Python']
values = [1972, 1993, 1990]

langs1 = {'C': 1972, 'Lua': 1993, 'Python': 1990}
langs2 = {'Lisp': 1958, 'Scheme': 1975}

INPUT_FILE = 'prize.json'
OUTPUT_FILE = 'data.csv'


def difference(list_used, list_all):
    return all(n is not None for n in [list_all.remove(i) for i in list_used if i in list_all]) or list_all


def create_dict(keys_, values_):
    return dict(zip(keys_, values_))


def dict_update(dict1, dict2):
    new_dict = dict1.copy()
    return new_dict.update(dict2) or new_dict


def swap_key_value(dict_):
    return {value: key for key, value in dict_.items()}


print(difference(used, dirty_input))
print(create_dict(keys, values))
print(dict_update(langs1, langs2))
print(swap_key_value(langs1))
try:
    parser = parse_util.Parser(INPUT_FILE, OUTPUT_FILE)
    parser.parse()
except FileNotFoundError as e:
    print(f'An error {e.__class__.__name__} was occurred')
except FileExistsError as e:
    print(f'An error {e.__class__.__name__} was occurred: Please delete file or move to other directory')
