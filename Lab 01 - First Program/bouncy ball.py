
import arcade
from random import randint, choice

WIDTH = 1600
HEIGHT = 800
TITLE = "The Bouncing Ball"
balls = []

class Ball():
    def __init__(self, x, y, vx, vy, size, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.size = size
        self.color = color

    def update(self):
        if self.x < 0 + self.size:
            self.vx = abs(self.vx)
        if self.x > WIDTH - self.size:
            self.vx = -abs(self.vx)
        if self.y < 0 + self.size:
            self.vy = abs(self.vy)
        if self.y > HEIGHT - self.size:
            self.vy = -abs(self.vx)
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)

def on_draw(dt):

    arcade.start_render()
    for b in balls:
        b.update()
        b.draw()

for i in range(randint(1, 50)):
    b = Ball(randint(0, WIDTH), randint(0, HEIGHT), randint(1, 10), randint(1, 10), randint(0, 200), (randint(0, 255), randint(0, 255), randint(0, 255)))
    balls.append(b)

arcade.open_window(WIDTH, HEIGHT, TITLE)

arcade.schedule(on_draw, 1/60)
arcade.run()