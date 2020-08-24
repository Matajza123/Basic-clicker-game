class Stats():
    def __init__(self):
        self.clicks = 0
        self.max_dps = 0
        self.time_played = 0
        self.max_lvl = 0
        self.small_boss = 0
        self.boss = 0
        self.enemy = 0

    def add_click(self, clicks):
        self.clicks += clicks
    
    def add_max_dps(self, dps):
        self.max_dps += dps
    
    def add_time_played(self, time):
        self.time_played += time

    def update_max_lvl(self, max):
        if max > self.max_lvl:
            self.max_lvl = max

    def add_small_boss(self, value=1):
        self.small_boss += value

    def add_boss(self, value=1):
        self.boss += value
    
    def add_enemy(self, value=1):
        self.enemy += value
    
    def get_clicks(self):
        return self.clicks
    
    def get_max_dps(self):
        return self.max_dps

    def get_time_played(self):
        return self.time_played

    def get_max_lvl(self):
        return self.max_lvl

    def get_small_boss(self):
        return self.small_boss
    
    def get_boss(self):
        return self.boss
    
    def get_enemy(self):
        return self.enemy

    def update_enemy_count(self, type=False, value=1):
        if type == False:
            self.add_enemy()
        elif type == True:
            self.add_small_boss()
        elif type == "Boss":
            self.add_boss()
