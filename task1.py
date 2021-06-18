from copy import deepcopy

list_of_strings = [
    'python',
    'java',
    'assembler',
    'c',
    'ruby',
    'go'
]


def get_second_by_length(list_):
    new_list = deepcopy(list_)
    return sort_by_length(new_list)[1]


def sort_by_length(list_):
    new_list = deepcopy(list_)
    new_list.sort(key=lambda string: len(string))
    return new_list


def sort_by_vowels(list_):
    def vowels_count(string):
        vowels = ['a', 'e', 'i' 'o', 'u', 'y']
        count = 0
        for vowel in vowels:
            if vowel in string:
                count += string.lower().count(vowel)
        return count

    new_list = deepcopy(list_)
    new_list.sort(key=lambda string: vowels_count(string))
    return new_list


def sort_by_consonants(list_):
    def consonants_count(string):
        consonants = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n',
                      'p', 'q', 's', 't', 'v', 'x', 'z', 'h', 'r', 'w']
        count = 0
        for consonant in consonants:
            if consonant in string:
                count += string.lower().count(consonant)
        return count

    new_list = deepcopy(list_)
    new_list.sort(key=lambda string: consonants_count(string))
    return new_list


def change_letters_place(list_):
    new_list = deepcopy(list_)
    for i in range(len(new_list)):
        if i % 2:
            strings = list(new_list[i])
            strings[0], strings[-1] = strings[-1], strings[0]
            new_list[i] = ''.join(map(str, strings))
    return new_list


def revert_list_of_strings(list_):
    new_list = deepcopy(list_)
    for i in range(len(new_list)):
        new_list[i] = new_list[i][::-1]
    return new_list


print('Find the second by length string in a list or array\n', get_second_by_length(list_of_strings))
print('Sort list by string length:\n', sort_by_length(list_of_strings))
print('Sort list by count of vowels in string\n', sort_by_vowels(list_of_strings))
print('Sort list by count of consonants in string\n', sort_by_consonants(list_of_strings))
print('Change by places first and last letters in each second string of list or array\n',
      change_letters_place(list_of_strings))
print('Revert strings of list or array\n', revert_list_of_strings(list_of_strings))
