import pygame
import random
# import heros
from heros import Hero


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

    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player
        self.WIDTH = 400
        self.HEIGHT = 800
        self.hero_list = [Hero(0, True), Hero(1)]
        self.hero_loc = []
        # self.hero_list = [Hero(0, True)]

    def draw(self, win):
        self.win_height = 100
        self.font = pygame.font.SysFont("arial.ttf", 25)
        for hero in self.hero_list:
            x = hero.get_id()
            hero_cost = hero.get_cost()

            pygame.draw.rect(win, (255, 150, 0), (x, self.y+(self.win_height*x), self.WIDTH, self.win_height))
            hero_name = self.font.render(f'{hero.get_name()} DPS{hero.get_dps()}', False, (255, 255, 255))
            win.blit(hero_name,(self.x, self.y+(self.win_height*x)))

            if hero.get_status() == True:
                if self.player.get_money() - hero_cost > 0.0:
                    pygame.draw.rect(win, (0, 255, 0), (210, self.y+(self.win_height*x)+12, 160, 75))
                else:
                    pygame.draw.rect(win, (255, 0, 0), (210, self.y+(self.win_height*x)+12, 160, 75))

                hero_lvl = self.font.render(f'LVL: {hero.get_lvl()}', False, (255, 255, 255))
                lvl_cost = self.font.render(f'Cost: {hero.get_cost()}', False, (255, 255, 255))

                win.blit(hero_lvl,(260, self.y+(self.win_height*x)+35))
                win.blit(lvl_cost,(260, self.y+(self.win_height*x)+55))
                
            else:
                if self.player.get_money() - hero_cost > 0.0:
                    pygame.draw.rect(win, (255, 255, 0), (210, self.y+(self.win_height*x)+12, 160, 75))
                else:
                    pygame.draw.rect(win, (255, 0, 0), (210, self.y+(self.win_height*x)+12, 160, 75))

                hero_lvl = self.font.render(f'LVL: 0', False, (255, 255, 255))
                lvl_cost = self.font.render(f'Cost: {hero.get_cost()}', False, (255, 255, 255))

                win.blit(hero_lvl,(260, self.y+(self.win_height*x)+35))
                win.blit(lvl_cost,(260, self.y+(self.win_height*x)+55))


    def click(self, x, y):
        if 400 > x > 0 and 800 > y > 0:
            return True

    def buy_hero(self, mouse):
        for hero in self.hero_list:
            if 370 > mouse[0] > 210:
                if self.y+(self.win_height*hero.get_id())+87 > mouse[1] > self.y+(self.win_height*hero.get_id())+12:
                    
                    hero_cost = hero.get_cost()

                    if self.player.get_money() - hero_cost > 0.0:
                        if hero.get_status() == True:
                            self.player.dec_dps(hero.get_dps())
                            hero.add_lvl()
                            self.player.add_dps(hero.get_dps())

                        elif hero.get_status() == False:
                            if hero.get_id()+1 < 8:
                                hero.change_status()
                                self.player.add_dps(hero.get_dps())
                                self.hero_list.append(Hero(hero.get_id()+1))

                        self.player.dec_money(hero_cost)