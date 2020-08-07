class Stats():
    def __init__(self):
        self.clicks = 0
        self.max_dps = 0
        self.time_played = 0
        self.max_lvl = 0

    def add_click(self, clicks):
        self.clicks += clicks
    
    def add_max_dps(self, dps):
        self.max_dps += dps
    
    def add_time_played(self, time):
        self.time_played += time

    def update_max_lvl(self, max):
        if max > self.max_lvl:
            self.max_lvl = max
    
    def get_clicks(self):
        return self.clicks
    
    def get_max_dps(self):
        return self.max_dps

    def get_time_played(self):
        return self.time_played

    def get_max_lvl(self):
        return self.max_lvl

