import pygame

class point:
    def __init__(self, x, y, window, color = (0,0,0), state = False):
        self.x = x
        self.y = y
        self.color = color
        self.state = state
        self.window = window

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
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
    
    def set_color(self, color: int):
        self.color = color
        return color

    def set_x(self, x: int) -> int:
        self.erase()
        self.x = x
        if self.state == True:
            self.point_draw()
        return self.x

    def set_y(self, y: int) -> int:
        self.erase()
        self.y = y
        if self.state == True:
            self.point_draw()
        return self.y
    
    def point_draw(self):
        self.pixelchange(self.color)
        self.state = True
        return self
    
    def erase(self):
        self.pixelchange((255,255,255))
        return self
    
    def pixelchange(self, color):
        for dx in (-2, -1, 0, 1, 2):
            for dy in (-2, -1, 0, 1, 2):
                self.window.set_at((self.x + dx, self.y + dy), color)
        return self

def main():
    pygame.init()
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

        lastpress = keyhandler(lastpress)
        eventhandler(lastpress, event, bod)
        pygame.display.flip()

def eventhandler(lastpress, event, bod):
        if event.type == pygame.MOUSEBUTTONDOWN and lastpress == "a":
            pos = pygame.mouse.get_pos()
            bod.set_x(pos[0])
            bod.set_y(pos[1])
        elif event.type == pygame.MOUSEBUTTONDOWN and lastpress == "b":
            pass
        elif lastpress == "q":
            bod.add_to_color((1,0,0))
            bod.point_draw()
        elif lastpress == "w":
            bod.add_to_color((0,1,0))
            bod.point_draw()
        elif lastpress == "e":
            bod.add_to_color((0,0,1))
            bod.point_draw()

def keyhandler(lastpress):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        lastpress = "a"
    elif keys[pygame.K_s]:
        lastpress = "b"
    elif keys[pygame.K_q]:
        lastpress = "q"
    elif keys[pygame.K_w]:
        lastpress = "w"
    elif keys[pygame.K_e]:
        lastpress = "e"
    else:
        lastpress = ""
    return lastpress
    
main()
