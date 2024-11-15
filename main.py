import pygame
from classes import Point, Square
from event_key_handler import eventhandler, keyhandler

def main():
    pygame.init()
    window_size = (250, 250)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Graphical python drawing")
    window.fill((255, 255, 255))
    clock = pygame.time.Clock()

    lastpress = ""

    keys_pressed = {}
    points = []
    squares = []

    objPoint = Point(-10, -10, window)
    objPoint.point_draw()

    objSquare = Square(-50, -50, window, size=10)
    objSquare.point_draw()

    points.append(objPoint)
    squares.append(objSquare)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        lastpress, keys_pressed = keyhandler(lastpress, event, keys_pressed)
        squares, points = eventhandler(lastpress, event, objPoint, objSquare, squares, points, window)

        window.fill((255, 255, 255))
        
        for ob in points:
            ob.point_draw()
        for ob in squares:
            ob.point_draw()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()