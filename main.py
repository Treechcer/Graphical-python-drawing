import pygame
from point import Point
from event_key_handler import eventhandler, keyhandler

def main():
    pygame.init()
    window_size = (250, 250)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Graphical Test")
    window.fill((255, 255, 255))

    lastpress = ""
    bod = Point(-10, -10, window)
    bod.point_draw()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        lastpress = keyhandler(lastpress)
        eventhandler(lastpress, event, bod)
        pygame.display.flip()

if __name__ == "__main__":
    main()