import pygame

import time

class point:
    def __init__(self, x, y, window, color = (0,0,0), state = False):
        self.x = x
        self.y = y
        self.color = color
        self.state = state
        self.window = window

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x: int):
        self.erase()
        self.x = x
        if self.state == True:
            self.point_draw()
        return self.x

    def set_y(self, y: int):
        self.erase()
        self.y = y
        if self.state == True:
            self.point_draw()
        return self.y
    
    def point_draw(self):
        for dx in (-2, -1, 0, 1, 2):
            for dy in (-2, -1, 0, 1, 2):
                self.window.set_at((self.x + dx, self.y + dy), self.color)
        self.state = True
        return self
    
    def erase(self):
        for dx in (-2, -1, 0, 1, 2):
            for dy in (-2, -1, 0, 1, 2):
                self.window.set_at((self.x + dx, self.y + dy), (255,255,255))
        return self

def main():
    pygame.init
    window_size = (250, 250)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("graphical test")
    window.fill((255,255,255))

    lastpress = ""

    bod = point(-10, -10, window)
    bod.point_draw()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        lastpress = keyhandler()
        eventhandler(lastpress, event, bod)

        pygame.display.flip()

def eventhandler(lastpress, event, bod):
        if event.type == pygame.MOUSEBUTTONDOWN and lastpress == "a":
            pos = pygame.mouse.get_pos()
            bod.set_x(pos[0])
            bod.set_y(pos[1])
        elif event.type == pygame.MOUSEBUTTONDOWN and lastpress == "b":
            pass

def keyhandler():
    lastpress = ""
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        lastpress = "a"
    if keys[pygame.K_s]:
        lastpress = "b"
    return lastpress
    
main()
