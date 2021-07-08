# Open/closed principle
class BaseUser:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class User(BaseUser):
    def __init__(self, username, password, first_name, last_name):
        super().__init__(username, password)
        self.first_name = first_name
        self.last_name = last_name
