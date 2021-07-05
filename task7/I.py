# Interface segregation principle
class BaseShape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle(BaseShape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h


class Circle(BaseShape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r
