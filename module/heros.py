import pygame

class Hero(object):
    name_list = ["Bob", "Joseph", "Alice", "Mathew", "Tom", "Tim", "Jeffrey", "Jow", "DO NOT TOUCH"]
    def __init__(self, id=1, bought=False):
        self.id = id
        self.name = self.name_list[self.id]
        self.lvl = 1
        self.prog = 12
        self.dps = 1
        self.cost = self.id*38.8+10
        self.bought = bought

    def get_name_list(self):
        return self.name_list
        
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
    
    def get_dps(self):
        if self.bought:
            return self.dps
        else:
            return 0
    
    def get_lvl(self):
        return self.lvl

    def get_cost(self):
        return self.cost

    def get_prog(self):
        return self.prog

    def get_status(self):
        return self.bought
    
    def add_dps(self, dps):
        if self.bought:
            self.dps += dps
        else:
            return None

    def add_lvl(self, lvl=1):
        if self.bought:
            self.lvl += lvl
            self.update_stats()
        else:
            return None

    def add_cost(self, cost):
        self.cost += self.prog + cost

    def dec_cost(self, cost):
        self.cost -= cost 

    def add_prog(self, prog, type=True):
        self.prog += prog

    def dec_prog(self, prog, type=True):
        self.prog -= prog 

    def change_status(self):
        self.bought = True
        self.update_stats()

    def update_stats(self):
        self.dps += self.lvl + self.prog + (self.id*1.6)
        self.add_prog(self.lvl*1.3)
        self.add_cost(10)
        