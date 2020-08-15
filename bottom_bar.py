import pygame

class BottomBar:
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

    def __init__(self, x, y, player):
        self.x = x #400
        self.y = y #650
        self.WIDTH = 800
        self.HEIGHT = 150
        self.player = player
        self.font = pygame.font.SysFont("arial.ttf", 35)

    def draw(self, win):
        pygame.draw.rect(win, (255, 150, 0), (self.x, self.y, self.WIDTH, self.HEIGHT))
        text_dps = self.font.render(f'Dps: {self.player.get_dps()}', False, (255, 255, 255))
        text_clicks = self.font.render(f'Click dmg: {self.player.get_click()}', False, (255, 255, 255))
        text_money = self.font.render(f'Money: {self.player.get_money()}', False, (255, 255, 255))
        text_skills = self.font.render(f'Skills: {self.player.get_skills()}', False, (255, 255, 255))

        win.blit(text_dps, (450, 675))
        win.blit(text_clicks, (450, 700))
        win.blit(text_money, (450, 725))
        win.blit(text_skills, (450, 750))





