import pygame

def eventhandler(lastpress, event, objPoint, objSquare):
    if event.type == pygame.MOUSEBUTTONDOWN and lastpress == "a":
        pos = pygame.mouse.get_pos()
        objPoint.set_x(pos[0])
        objPoint.set_y(pos[1])
    elif event.type == pygame.MOUSEBUTTONDOWN and lastpress == "s":
        pos = pygame.mouse.get_pos()
        objSquare.set_x(pos[0])
        objSquare.set_y(pos[1])
    elif lastpress == "qa":
        objPoint.add_to_color((1, 0, 0))
        objPoint.point_draw()
    elif lastpress == "wa":
        objPoint.add_to_color((0, 1, 0))
        objPoint.point_draw()
    elif lastpress == "ea":
        objPoint.add_to_color((0, 0, 1))
        objPoint.point_draw()
    elif lastpress == "qs":
        objSquare.add_to_color((1, 0, 0))
        objSquare.point_draw()
    elif lastpress == "ws":
        objSquare.add_to_color((0, 1, 0))
        objSquare.point_draw()
    elif lastpress == "es":
        objSquare.add_to_color((0, 0, 1))
        objSquare.point_draw()
    elif lastpress == "+":
        objSquare.add_to_size()
    elif lastpress == "-":
        objSquare.sub_to_size()

def keyhandler(lastpress):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_F1]:
        lastpress = "+"
    elif keys[pygame.K_F2]:
        lastpress = "-"
    elif keys[pygame.K_q] and keys[pygame.K_a]:
        lastpress = "qa"
    elif keys[pygame.K_w] and keys[pygame.K_a]:
        lastpress = "wa"
    elif keys[pygame.K_e] and keys[pygame.K_a]:
        lastpress = "ea"
    elif keys[pygame.K_q] and keys[pygame.K_s]:
        lastpress = "qs"
    elif keys[pygame.K_w] and keys[pygame.K_s]:
        lastpress = "ws"
    elif keys[pygame.K_e] and keys[pygame.K_s]:
        lastpress = "es"
    elif keys[pygame.K_a]:
        lastpress = "a"
    elif keys[pygame.K_s]:
        lastpress = "s"
    else:
        lastpress = ""
    return lastpress