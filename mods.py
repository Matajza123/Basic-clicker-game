import pygame

class Enemy_mod():
    def __init__(self, type0=False, base_hp=10, hp=1, lvl=1, base_ttk=60, ttk=1, money=1, prog=6):
        self.type = type0
        self.hp = hp
        self.base_hp = base_hp
        self.lvl = lvl
        self.ttk = ttk
        self.base_ttk = base_ttk
        self.money = money
        self.prog = prog

        if self.type == "Boss":
            print("boss")
        elif self.type == "Small boss":
            print("small boss")
        else:
            print("normall")
            
    
    def get_hp(self, hp):
        return self.hp

    def get_base_hp(self, base_hp):
        return self.base_hp
    
    def get_lvl(self, lvl):
        return self.lvl
    
    def get_ttk(self, ttk):
        return self.ttk

    def get_base_ttk(self, ttk):
        return self.base_ttk
    
    def get_money(self, money):
        return self.money

    def get_prog(self, prog):
        return self.prog

    def change_hp(self, hp):
        self.hp = hp
    
    def change_lvl(self, lvl):
        self.lvl = lvl
    
    def change_ttk(self, ttk):
        self.ttk = ttk

    def change_base_ttk(self, base_ttk):
        self.base_ttk = base_ttk
    
    def change_money(self, money):
        self.money = money

    def change_prog(self, prog):
        self.prog = prog

    
