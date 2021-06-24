class CustomKeyNotFoundError(Exception):
    def __init__(self, message, key):
        self.message = message
        self.key = key
        super().__init__(self.message)


class RowNotFoundError(Exception):
    def __init__(self, message, row):
        self.message = message
        self.row = row
        super().__init__(self.message)


class DataNotFoundError(Exception):
    def __init__(self, message, data):
        self.message = message
        self.data = data
        super().__init__(self.message)
