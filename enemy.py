import random
import pygame
import os

class Enemy():
    def __init__(self, id=1, lvl=1):

        self.name = self.get_enemy_names()
        self.id = random.randrange(0, len(self.name))
        self.lvl = lvl
        self.boss = self.chech_if_boss(self.lvl)
        self.prog = self.lvl*6.5
        """
        if self.boss == "Small boss":
            self.mod = Enemy_mod("Small boss")

        elif self.boss == "Boss":
            self.mod = Enemy_mod("Boss")

        else:
            self.mod = Enemy_mod(False)
        """

        self.hp = 30 + self.prog
        self.max_hp = self.hp

        self.lvl = 1
        self.money = self.lvl*3.8

        self.ttk = int(60-0.2)
        self.max_ttk = self.ttk
        
    def deal_dmg_click(self, click):
        self.hp -= click

    def deal_dmg_dps(self, dps):
        self.hp -= dps
    
    def decrese_ttk(self):
        self.ttk -= 1

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name[self.id]

    def get_ttk(self):
        return self.ttk

    def get_max_ttk(self):
        return self.max_ttk

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp 

    def get_money(self):
        return self.money 

    def chech_if_boss(self, lvl):
        list_lvl = list(str(lvl))
        if list_lvl[-1] == "0":
            return "Boss"

        elif list_lvl[-1] == "5":    
            return "Small boss"

        else:
            return False

    def get_enemy_names(self):
        finall_names = []
        names = os.listdir("img/enemy/")
        
        for name in names:
            name = name.replace(".png", "")
            finall_names.append(name)

        return finall_names
        
    def get_img(self):
            # return pygame.image.load(os.path.join(f'img/enemy/Boss/{self.name[self.id]}.png'))
        return pygame.image.load(os.path.join(f'img/enemy/{self.name[self.id]}.png'))
