list_of_strings = [
    'python',
    'java',
    'assembler',
    'c',
    'rUby',
    'Go',
    '',
    ' '
]

VOWELS = 'aeiouy'

CONSONANTS = 'bcdfgjklmnpqstvxzhrw'


def sort_by_length(list_):
    new_list = list_[:]
    new_list.sort(key=len)
    return new_list


def sort_by_letters(list_, by_vowels=True):
    def letters_count(string, source):
        count = 0
        string = string.lower()
        for vowel in source:
            if vowel in string:
                count += string.count(vowel)
        return count

    new_list = list_[:]
    if by_vowels:
        new_list.sort(key=lambda string: letters_count(string, VOWELS))
    else:
        new_list.sort(key=lambda string: letters_count(string, CONSONANTS))
    return new_list


def swap_first_last_letter(list_):
    new_list = list_[:]
    for i in range(len(new_list)):
        if i % 2:
            strings = list(new_list[i])
            strings[0], strings[-1] = strings[-1], strings[0]
            new_list[i] = ''.join(map(str, strings))
    return new_list


def revert_list_of_strings(list_):
    new_list = list_[:]
    for i in range(len(new_list)):
        new_list[i] = new_list[i][::-1]
    return new_list


print(f'Find the second by length string in a list or array:\n{sort_by_length(list_of_strings)[1]}')
print(f'Sort list by string length:\n{sort_by_length(list_of_strings)}')
print(f'Sort list by count of vowels in string:\n{sort_by_letters(list_of_strings)}')
print(f'Sort list by count of consonants in string:\n{sort_by_letters(list_of_strings, False)}')
print(f'Change by places first and last letters in each second string of list or array:\n'
      f'{swap_first_last_letter(list_of_strings)}')
print(f'Revert strings of list or array:\n{revert_list_of_strings(list_of_strings)}')
