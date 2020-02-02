import pygame
from fighter import Fighter


class Player:
    def __init__(self, name, screen,  window_size=(300, 500)):
        self.screen = screen
        self.name = name
        self.window_size = window_size

    def move_left(self, x, y):
        return x-10, y


    def move_right(self, x, y):
        return x+10, y

    def move_up(self, x, y):
        return x, y-10

    def move_down(self, x, y):
        return x, y+10

    def shoot(self, head, direction):
        pygame.draw.rect(self.screen, (255, 255, 255), (head[0]+50, head[1], 10, 10))
        return direction




