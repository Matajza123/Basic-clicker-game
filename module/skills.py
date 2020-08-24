import pygame

class Skills():
    skills = ["Boost DPS", "Boost Click", "100% more gold", "Lower enemy prog"]
    def __init__(self, id=1):
        self.id = []
        if not id in self.id:
            self.id.append(id)

        self.max_id = len(self.skills)
        # self.duration = self.id + 5
        self.effect = self.skills[0] 

        self.width = 40
        self.height = 40
        self.x = 410
        self.y = 175

    def draw(self, win):
        pass

    def click(self):
        pass
