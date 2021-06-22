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
    return sorted(list_, key=len)


def sort_by_letters(list_, letters):
    def letters_count(string, source):
        count = 0
        string = string.lower()
        for vowel in source:
            if vowel in string:
                count += string.count(vowel)
        return count

    return sorted(list_, key=lambda string: letters_count(string, letters))


def swap_first_last_letter(list_):
    new_list = list_[:]
    for i in range(1, len(new_list), 2):
        strings = list(new_list[i])
        strings[0], strings[-1] = strings[-1], strings[0]
        new_list[i] = ''.join(strings)
    return new_list


def revert_list_of_strings(list_):
    return [i[::-1] for i in list_]


print(f'Find the second by length string in a list or array:\n{sort_by_length(list_of_strings)[1]}')
print(f'Sort list by string length:\n{sort_by_length(list_of_strings)}')
print(f'Sort list by count of vowels in string:\n{sort_by_letters(list_of_strings, VOWELS)}')
print(f'Sort list by count of consonants in string:\n{sort_by_letters(list_of_strings, CONSONANTS)}')
print(f'Change by places first and last letters in each second string of list or array:\n'
      f'{swap_first_last_letter(list_of_strings)}')
print(f'Revert strings of list or array:\n{revert_list_of_strings(list_of_strings)}')
