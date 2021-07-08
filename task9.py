from datetime import datetime
import sqlite3


class LoggerMetaclass(type):
    INFO = 10
    WARNING = 20
    ERROR = 30
    NOTSET = 0
    level = NOTSET
    LOGFILE = 'logs.txt'
    f = open(LOGFILE, 'a', encoding='utf-8')
    connection = sqlite3.connect('database.sqlite3')

    def __new__(mcs, name, bases, attrs):

        cursor = mcs.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            level VARCHAR(10) NOT NULL,
            datetime DATETIME NOT NULL,
            function VARCHAR(50) NOT NULL,
            message TEXT NOT NULL
        )""")

        def log(func):
            def wrapper(*args, **kwargs):
                current_datetime = datetime.now()
                try:
                    if mcs.level <= 10:
                        msg = args[1:] if args[1:] else 'without args'
                        log_console_file_db('INFO', current_datetime, func, msg)
                        return func(*args, **kwargs)
                    elif mcs.level == 20:
                        result = func(*args, **kwargs)
                        if result is None:
                            log_console_file_db('WARNING', current_datetime, func, 'function returns None')
                        return result
                    else:
                        return func(*args, **kwargs)
                except Exception as e:
                    if mcs.level == 30:
                        log_console_file_db('ERROR', current_datetime, func, f'{e.__class__.__name__}: {e}')

            def console_pattern(level, current_datetime, name, message):
                return f'{level} | [{current_datetime}] {name} - {message}'

            def database_log(level, current_datetime, function, message):
                cursor.execute("""INSERT INTO logs(level, datetime, function, message) VALUES (?, ?, ?, ?)""",
                               (level, current_datetime, function, message))
                mcs.connection.commit()

            def log_console_file_db(level, current_datetime, func, msg):
                log_msg = console_pattern(level, current_datetime, func.__name__, msg)
                mcs.f.write(f'{log_msg}\n')
                database_log(level, current_datetime, func.__name__, f'{msg}')
                print(log_msg)

            return wrapper

        newattrs = {}
        for key, value in attrs.items():
            if len(key.split('__')) == 1 and not key.isupper():
                newattrs[key] = log(value)
            else:
                newattrs[key] = value
        return super().__new__(mcs, name, bases, newattrs)

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)


class SimpleClass(metaclass=LoggerMetaclass):

    def raise_exception(self):
        raise Exception('Critical failure')

    def return_none(self):
        return None

    def say_hello(self, name):
        return f'Hello, {name}!'


def call_methods():
    s_class.say_hello('Alex')
    s_class.return_none()
    s_class.raise_exception()


s_class = SimpleClass()
call_methods()
LoggerMetaclass.level = LoggerMetaclass.WARNING
call_methods()
LoggerMetaclass.level = LoggerMetaclass.ERROR
call_methods()
