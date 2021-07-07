# Linskov substitution principle
class Ball:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


class Game:
    def __init__(self, ball, speed):
        self.ball = ball
        self.speed = speed

    def update(self):
        self.ball.move(*self.speed)


ball = Ball(0, 0, 5)
game = Game(ball, (5, 5))
while True:
    game.update()
    # not game.ball.move(5, 5)
