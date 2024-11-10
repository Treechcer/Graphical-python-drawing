import pygame

class DrawableObject:
    def __init__(self, x, y, window, color=(0, 0, 0), state=False):
        self.x = x
        self.y = y
        self.color = color
        self.state = state
        self.window = window

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

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

    def erase(self):
        self.pixelchange((255, 255, 255))
        return self

    def add_to_color(self, changer):
        color = self.color
        color = (
            max(0, min(255, color[0] + changer[0])),
            max(0, min(255, color[1] + changer[1])),
            max(0, min(255, color[2] + changer[2])),
        )
        self.color = color
        return self.color

    def set_color(self, color):
        self.color = color
        return color

    def point_draw(self):
        self.pixelchange(self.color)
        self.state = True
        return self

    def __str__(self):
        return f"this object has: x = {self.x}, y = {self.y}, color = {self.color}, state = {self.state}, window = {self.window}"


class Point(DrawableObject):
    def __init__(self, x, y, window, color=(0, 0, 0), state=False):
        super().__init__(x, y, window, color, state)

    def pixelchange(self, color):
        for dx in (-2, -1, 0, 1, 2):
            for dy in (-2, -1, 0, 1, 2):
                self.window.set_at((self.x + dx, self.y + dy), color)
        return self


class Square(DrawableObject):
    def __init__(self, x, y, window, size=6, color=(0, 0, 0), state=False):
        super().__init__(x, y, window, color, state)
        self.size = size

    def pixelchange(self, color):
        for dx in range(-(self.size), self.size + 1):
            for dy in range(-(self.size), self.size + 1):
                self.window.set_at((self.x + dx, self.y + dy), color)
        return self

    def __str__(self):
        return f"this object has: x = {self.x}, y = {self.y}, color = {self.color}, state = {self.state}, window = {self.window}, size = {self.size}"

    def add_to_size(self):
        self.size += 1
        return self.size

    def sub_to_size(self):
        self.erase()
        self.size -= 1
        self.pixelchange(self.color)
        return self.size


class Triangle(DrawableObject):
    def __init__(self, x, y, window, size=6, color=(0, 0, 0), state=False):
        super().__init__(x, y, window, color, state)
        self.size = size

    def pixelchange(self, color):
        for row in range(self.size):
            start_x = self.x - row
            end_x = self.x + row
            y_position = self.y + row
            for x_position in range(start_x, end_x + 1):
                self.window.set_at((x_position, y_position), color)
        return self

    def erase(self):
        for row in range(self.size):
            start_x = self.x - row
            end_x = self.x + row
            y_position = self.y + row
            for x_position in range(start_x, end_x + 1):
                self.window.set_at((x_position, y_position), (255, 255, 255))
        return self

    def set_x(self, x):
        self.x = x
        return self.x

    def set_y(self, y):
        self.y = y
        return self.y