# Single responsibility principle
class User:
    def __init__(self, username):
        """Create user entity"""
        self.username = username


class UserDB:
    @classmethod
    def save(cls, user):
        """Save user entity to db"""
        pass

