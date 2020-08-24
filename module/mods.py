import pygame

class Enemy_mod():
    def __init__(self, type0=False, lvl=1, base_hp=30, hp=1, base_ttk=60, ttk=1, money=1, prog=1):
        self.type = type0
        self.prog = prog
        self.lvl = lvl
        
        if self.type == False: self.prog = self.lvl * 7
        elif self.type  == True: self.prog = self.lvl * 10
        elif self.type == "Boss": self.prog = self.lvl * 15

        self.base_hp = base_hp 
        self.hp = base_hp * self.prog
        self.ttk = ttk 
        self.base_ttk = base_ttk
        self.money = money + (self.lvl * self.prog)
    
    def get_hp(self):
        return self.hp

    def get_base_hp(self):
        return self.base_hp
    
    def get_lvl(self):
        return self.lvl
    
    def get_ttk(self):
        return self.ttk

    def get_base_ttk(self):
        return self.base_ttk
    
    def get_money(self):
        return self.money

    def get_prog(self):
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

    
