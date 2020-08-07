import pygame
import pygame_gui
from game import Game

class Main_Menu:
    BG = (255, 255, 255)

    def __init__(self):
        self.WIDTH = 1000
        self.HEIGHT = 1000
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.background = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.manager = pygame_gui.UIManager((self.WIDTH, self.HEIGHT))

    def draw(self): #draw main menu 
        self.start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.WIDTH/2-40, self.HEIGHT/2-100), (100, 50)),
                                                    text='Start',
                                                    manager=self.manager)

        self.options_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.WIDTH/2-40, self.HEIGHT/2-50), (100, 50)),
                                                    text='Options',
                                                    manager=self.manager)

        self.exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.WIDTH/2-40, self.HEIGHT/2), (100, 50)),
                                                    text='Exit',
                                                    manager=self.manager)
        


    def run(self):
        clock = pygame.time.Clock()
        self.draw()

        is_running = True

        while is_running:
            time_delta = clock.tick(60)/1000.0
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.start_button:
                            game = Game()
                            game.run()

                        if event.ui_element == self.options_button:
                            pass#TODO add options

                        if event.ui_element == self.exit_button:
                            is_running = False

                self.manager.process_events(event)

            self.manager.update(time_delta)
            #TODO add background
            self.manager.draw_ui(self.win)
            pygame.display.update()


if __name__ == "__main__":
    pygame.font.init()
    main = Main_Menu()
    main.run()
