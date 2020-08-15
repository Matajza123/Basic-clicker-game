class Player():
    def __init__(self, name):
        self.name = name
        self.click = 1
        self.dps = 0
        self.money = 0.0
        self.items = {}
        self.skills = []

    def set_dps(self, dps):
        self.dps = dps
    
    def add_dps(self, dps):
        self.dps += dps

    def dec_dps(self, dps):
        self.dps -= dps

    def add_money(self, money):
        self.money += money

    def dec_money(self, money):
        new_money = self.money - money
        if new_money > 0.0:
            self.money -= money

    def append_item(self, item, dps):
        self.items[item] = dps
        self.add_dps(dps)
    
    def append_skill(self, skill, dps):
        self.skills.append(skill)
        self.add_dps(dps)

    def get_name(self):
        return self.name

    def get_money(self):
        return self.money
    
    def get_click(self):
        return self.click

    def get_dps(self):
        return self.dps

    def get_items(self):
        return self.items

    def get_skills(self):
        return self.skills
    
