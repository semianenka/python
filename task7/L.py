# Linskov substitution principle
class Ball:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


class HugeUltraSuperRedBall(Ball):
    def __init__(self, x, y, r):
        super().__init__(x, y, r)


class Game:
    def __init__(self, ball, speed):
        self.ball = ball
        self.speed = speed

    def update(self):
        self.ball.move(*self.speed)


ball = Ball(0, 0, 5)
huge_ultra_super_ball = HugeUltraSuperRedBall(0, 0, 1000)
game = Game(ball, (5, 5))
# nothing will change
# game = Game(huge_ultra_super_ball, (5, 5))
while True:
    game.update()
