import pygame
from classes import Point, Square

def eventhandler(lastpress, event, objPoint, objSquare, squares, points, window):
    lastShape = ""
    if event.type == pygame.MOUSEBUTTONDOWN and lastpress == "a" or lastpress == "ay":
        pos = pygame.mouse.get_pos()
        objPoint.set_x(pos[0])
        objPoint.set_y(pos[1])
        lastShape = "point"
    elif event.type == pygame.MOUSEBUTTONDOWN and lastpress == "s" or lastpress == "sy":
        pos = pygame.mouse.get_pos()
        objSquare.set_x(pos[0])
        objSquare.set_y(pos[1])
        lastShape = "square"
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
    elif lastpress == "F3":
        if squares:
            squares.pop()
    elif lastpress == "F4":
        if points:
            points.pop()
    if lastShape == "square" and lastpress == "sy":
        objSquare = Square(pos[0], pos[1], window, color = objSquare.color, size=10)
        squares.append(objSquare)
        lastShape = ""
    elif lastShape == "point" and lastpress == "ay":
        objPoint = Point(pos[0], pos[1], window, color = objPoint.color)
        points.append(objPoint)
        lastShape = ""

    return squares, points

import pygame

def keyhandler(lastpress, event, keys_pressed):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_F1]:
        lastpress = "+"
    elif keys[pygame.K_F2]:
        lastpress = "-"
    elif keys[pygame.K_s] and keys[pygame.K_y] and not keys_pressed.get("sy", False):
        lastpress = "sy"
        keys_pressed["sy"] = True 
    elif keys[pygame.K_a] and keys[pygame.K_y] and not keys_pressed.get("ay", False):
        lastpress = "ay"
        keys_pressed["ay"] = True 
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

    if keys[pygame.K_F3] and not keys_pressed.get("F3", False):
        lastpress = "F3"
        keys_pressed["F3"] = True
    elif keys[pygame.K_F4] and not keys_pressed.get("F4", False):
        lastpress = "F4"
        keys_pressed["F4"] = True

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_s and keys_pressed.get("sy", False):
            keys_pressed["sy"] = False
        if event.key == pygame.K_y and keys_pressed.get("ay", False):
            keys_pressed["ay"] = False
        if event.key == pygame.K_F4 and keys_pressed.get("F4", False):
            keys_pressed["F4"] = False
        if event.key == pygame.K_F3 and keys_pressed.get("F3", False):
            keys_pressed["F3"] = False

    return lastpress, keys_pressed
