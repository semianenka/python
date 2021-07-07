import sys


class SkipThisFile(Exception):
    """Tells the generator to jump to the next file in list."""
    pass


def read_lines(files_):
    for file in files_:
        print(f'\nStart reading file: {file}\n')
        try:
            yield from open(file, 'r', encoding='utf-8').readlines()
        except SkipThisFile:
            pass


def display_files(files_):
    source = read_lines(files_)
    try:
        while True:
            print(next(source).rstrip(), end='')
            if input().lower() == 'n':
                print('\nMove to next file')
                source.throw(SkipThisFile)
    except StopIteration:
        print('\nFiles run out')


if __name__ == '__main__':
    files = [i for i in sys.argv[1:]]
    print('  ______ _____ _      ______   _____  ______          _____  ______ _____')
    print('|  ____|_   _| |    |  ____| |  __ \|  ____|   /\   |  __ \|  ____|  __ \ ')
    print('| |__    | | | |    | |__    | |__) | |__     /  \  | |  | | |__  | |__) |')
    print('|  __|   | | | |    |  __|   |  _  /|  __|   / /\ \ | |  | |  __| |  _  / ')
    print('| |     _| |_| |____| |____  | | \ \| |____ / ____ \| |__| | |____| | \ \ ')
    print('|_|    |_____|______|______| |_|  \_\______/_/    \_\_____/|______|_|  \_\\')

    print('Available actions:')
    print('- Press Enter to read the next line')
    print('- Press n and Enter to skip the rest of the current file and start reading the next file')
    print('- Press anything else and Enter to display the next line\n')

    display_files(files)
