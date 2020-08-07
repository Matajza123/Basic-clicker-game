import pygame
import random


class LeftBar(object):
    ROWS = 100
    COLS = 50
    COLORS = {
        0: (255, 255, 255),
        1: (0, 0, 0),
        2: (255, 0, 0),
        3: (0, 255, 0),
        4: (0, 0, 255),
        5: (255, 255, 0),
        6: (255, 140, 0),
        7: (165, 42, 42),
        8: (128, 0, 128)
    }

    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y
        self.WIDTH = 400
        self.HEIGHT = 800
        self.left_bar = self.create_board()

    def draw(self):
        pygame.draw.rect(self.win, (123, 123, 123), (self.x, self.y, self.WIDTH, self.HEIGHT))
        # for y, _ in enumerate(self.left_bar):
        #     for x, col in enumerate(self.left_bar[y]):
        #         pygame.draw.rect(
        #             win, col, (self.x + x*8, self.y + y*8, 8, 8), 0)

    def create_board(self):
        return pygame.draw.rect(self.win, (255, 255, 255), (self.x, self.y, self.WIDTH, self.HEIGHT))
        # return [[(255, 255, 255) for x in range(self.COLS)] for y in range(self.ROWS)]
