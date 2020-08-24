import pygame

class TopBar(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 750
        self.height = 50
        self.font = pygame.font.SysFont("arial.ttf", 25)


    def draw(self, win, hp, max_hp, time, max_time):
        self.current_hp = hp
        self.max_hp = max_hp
        self.current_time = time
        self.max_time = max_time
        
        hp_percent = self.max_hp/self.current_hp
        hp_percent2 = (self.current_hp/self.max_hp)*100
        hp_percent0 = self.width/hp_percent
        
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y,
                                          self.width, self.height)) #Bottom for hp

        pygame.draw.rect(win, (0, 0, 0), (self.x+hp_percent0, self.y,
                                          self.width, self.height))

        hp_text = self.font.render(f'{round(self.current_hp)}/{self.max_hp} | {round(hp_percent2)}%', False, (255, 255, 255))
        win.blit(hp_text, (775, 30))

        
        time_percent = self.max_time/self.current_time
        time_percent0 = self.width/time_percent

        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y,
                                          self.width, self.height-25))

        pygame.draw.rect(win, (0, 0, 255), (self.x-time_percent0, self.y,
                                          self.width, self.height-25)) #Top for time

        time_text = self.font.render(f'{self.current_time}/{self.max_time}', False, (255, 255, 255))
        win.blit(time_text, (765, 5))

