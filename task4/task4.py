import parse_util

used = [1, 3, 2, 4, 3]
dirty_input = [1, 3, 2, 2, 4, 3, 3, 3]

keys = ['C', 'Lua', 'Python']
values = [1972, 1993, 1990]

langs1 = {'C': 1972, 'Lua': 1993, 'Python': 1990}
langs2 = {'Lisp': 1958, 'Scheme': 1975}

INPUT_FILE = 'prize.json'


def difference(list_used, list_all):
    result = list_all[:]
    for i in list_used:
        result.remove(i)
    return result


def create_dict(keys_, values_):
    return dict(zip(keys_, values_))


def dict_update(dict1, dict2):
    return {**dict1, **dict2}


def swap_key_value(dict_):
    return {value: key for key, value in dict_.items()}


def call_parser(input_):
    try:
        parse_util.Parser(input_).parse()
    except Exception as e:
        print(e)
    except FileNotFoundError as e:
        print(f'An error {e.__class__.__name__} was occurred')


print(difference(used, dirty_input))
print(create_dict(keys, values))
print(dict_update(langs1, langs2))
print(swap_key_value(langs1))
call_parser(INPUT_FILE)
