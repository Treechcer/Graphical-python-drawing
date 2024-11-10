import pygame
from point import Point, Square
from event_key_handler import eventhandler, keyhandler

def main():
    pygame.init()
    window_size = (250, 250)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Graphical Test")
    window.fill((255, 255, 255))
    clock = pygame.time.Clock()

    lastpress = ""
    objPoint = Point(-10, -10, window)
    objPoint.point_draw()

    objSquare = Square(-50, -50, window)
    objSquare.point_draw()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        lastpress = keyhandler(lastpress)
        eventhandler(lastpress, event, objPoint, objSquare)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()