import pygame

class Point:
    def __init__(self, x, y, window, color=(0,0,0), state=False):
        self.x = x
        self.y = y
        self.color = color
        self.state = state
        self.window = window

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def add_to_color(self, changer):
        color = self.color
        if color[0] + changer[0] > 255 or color[0] + changer[0] < 0:
            color = (0, color[1], color[2])
        if color[1] + changer[1] > 255 or color[1] + changer[1] < 0:
            color = (color[0], 0, color[2])
        if color[2] + changer[2] > 255 or color[2] + changer[2] < 0:
            color = (color[0], color[1], 0)
        color = (color[0] + changer[0], color[1] + changer[1], color[2] + changer[2])
        self.color = color
        return self.color
    
    def set_color(self, color):
        self.color = color
        return color

    def set_x(self, x):
        self.erase()
        self.x = x
        if self.state:
            self.point_draw()
        return self.x

    def set_y(self, y):
        self.erase()
        self.y = y
        if self.state:
            self.point_draw()
        return self.y
    
    def point_draw(self):
        self.pixelchange(self.color)
        self.state = True
        return self
    
    def erase(self):
        self.pixelchange((255, 255, 255))
        return self
    
    def pixelchange(self, color):
        for dx in (-2, -1, 0, 1, 2):
            for dy in (-2, -1, 0, 1, 2):
                self.window.set_at((self.x + dx, self.y + dy), color)
        return self