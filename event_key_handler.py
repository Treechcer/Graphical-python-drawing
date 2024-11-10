import pygame

def eventhandler(lastpress, event, bod):
    if event.type == pygame.MOUSEBUTTONDOWN and lastpress == "a":
        pos = pygame.mouse.get_pos()
        bod.set_x(pos[0])
        bod.set_y(pos[1])
    #elif event.type == pygame.MOUSEBUTTONDOWN and lastpress == "b":
    #    pass
    elif lastpress == "q":
        bod.add_to_color((1, 0, 0))
        bod.point_draw()
    elif lastpress == "w":
        bod.add_to_color((0, 1, 0))
        bod.point_draw()
    elif lastpress == "e":
        bod.add_to_color((0, 0, 1))
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