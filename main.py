import pygame
from classes import Point, Square, Triangle
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
    triangles = []

    objTriangle = Triangle(-100,-100, window)

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
        triangles, squares, points = eventhandler(lastpress, event, objPoint, objSquare, squares, points, triangles, objTriangle, window)

        window.fill((255, 255, 255))
        
        for po in points:
            po.point_draw()
        for sq in squares:
            sq.point_draw()
        for tr in triangles:
            tr.point_draw()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()