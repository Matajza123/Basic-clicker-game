import pygame
import random
import os

class Board(object):
    ROWS = COLS = 90
    COLORS = {
        0: (255,255,255),
        1: (0,0,0),
        2: (255,0,0),
        3: (0,255,0),
        4: (0,0,255),
        5: (255,255,0),
        6: (255,140,0),
        7: (165,42,42),
        8: (128,0,128)
    }

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.WIDTH = 750
        self.HEIGHT = 620

        self.bg_name = self.get_bg_names()
        self.id = random.randrange(0, len(self.bg_name))

    def draw(self, win, lvl, enemy_name, enemy_img):
        self.font = pygame.font.SysFont("arial.ttf", 75)
        self.font_name = pygame.font.SysFont("arial.ttf", 50)

        lvl_text = self.font.render(f'{lvl}', False, (255, 255, 255))
        name = self.font_name.render(f'{enemy_name}', False, (255, 255, 255))
        
        win.blit(self.get_bg_img(), (400, 0))
        win.blit(name, (650, 600))
        win.blit(lvl_text, (785, 80))
        win.blit(enemy_img, (650, 150))


    def get_bg_img(self):
        return pygame.image.load(os.path.join(f'img/bg/{self.bg_name[self.id]}.jpg'))# 750x675

    def get_bg_names(self):
        bg0 = []
        bgs = os.listdir("img/bg/")

        for bg in bgs:
            bg = bg.replace(".jpg", "")
            bg0.append(bg)
        return bg0

    def click(self, x, y):
        if 1150 > x > 400 and 680 > y > 80:
            return True