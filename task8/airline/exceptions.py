class ObjectIsNotAircraftError(Exception):
    """Except when user tried to pass unsupported type of aircraft"""
    pass


class AircraftNotFoundError(Exception):
    """Except when user tried to get aircraft with wrong id"""
    pass
