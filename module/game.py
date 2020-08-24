import pygame
import pygame_gui
import random
import time

from top_bar import TopBar
from left_bar import LeftBar
from board import Board
from bottom_bar import BottomBar

from player import Player
from enemy import Enemy
from heros import Hero
from mods import Enemy_mod
from stats import Stats

class Game():
    bg_clr = (0,0,0)
    COLORS = {
        (255, 255, 255): 0,
        (0, 0, 0): 1,
        (255, 0, 0): 2,
        (0, 255, 0): 3,
        (0, 0, 255): 4,
        (255, 255, 0): 5,
        (255, 140, 0): 6,
        (165, 42, 42): 7,
        (128, 0, 128): 8
    }

    def __init__(self):
        pygame.font.init()

        self.WIDTH = 1150
        self.HEIGHT = 800
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.background = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.manager = pygame_gui.UIManager((self.WIDTH, self.HEIGHT))

        self.lvl = 1
        self.player = Player("Joseph")
        self.enemy = Enemy()
        self.stats = Stats()
        # self.mod = Enemy_mod() TODO
        
        self.top_bar = TopBar(400, 0)
        self.left_bar = LeftBar(0, 0, self.player)
        self.bottom_bar = BottomBar(400, 650, self.player, self.stats)
        self.board = Board(400, 50)

        self.max_click_ps = 10


    def next_lvl(self):
        self.player.add_money(self.enemy.get_money())
        self.stats.update_enemy_count(self.enemy.chech_if_boss(self.lvl))

        if self.board:
            del self.board

        if self.enemy:
            del self.enemy

        self.lvl += 1
        self.board = Board(400, 50)
        self.enemy = Enemy(self.lvl, self.lvl)

        pygame.display.update()

    def previous_lvl(self):
        self.player.add_money(self.enemy.get_money())
        if self.enemy:
            del self.enemy

        if self.lvl <= 1:
            self.lvl = 1
        else:
            self.lvl -= 1

        self.enemy = Enemy(self.lvl, self.lvl)
        pygame.display.update()
        
    def draw_lvl(self):
        self.win.fill(self.bg_clr)

        self.board.draw(self.win, self.lvl, self.enemy.get_name(), self.enemy.get_img())
        self.top_bar.draw(self.win, self.enemy.get_hp(), self.enemy.get_max_hp(), self.enemy.get_ttk(), self.enemy.get_max_ttk())
        self.left_bar.draw(self.win)
        self.bottom_bar.draw(self.win)

        pygame.display.update()

    def check_clicks(self):
        mouse = pygame.mouse.get_pos()
        
        clicked_board = self.board.click(*mouse)
        if clicked_board:
            self.enemy.deal_dmg_click(self.player.get_click())
            return True

        clicked_left_bar = self.left_bar.click(*mouse)
        if clicked_left_bar:
            self.left_bar.buy_hero(mouse)
            return True


    def run(self):
        self.clock = pygame.time.Clock()
        clock_loop = 0
        click_clock = 0
        is_running = True

        while is_running:
            fps = self.clock.tick(30)
            button_pressed = False

            if self.enemy.get_hp() <= 0:
                self.next_lvl()
            
            if self.enemy.get_ttk() <= 0:
                self.previous_lvl()

            self.draw_lvl()
            
            if clock_loop > 30:  # timer
                self.enemy.decrese_ttk()
                self.enemy.deal_dmg_dps(self.player.get_dps())
                clock_loop = 0
            else:
                clock_loop += 1

            if click_clock > 1: 
                if pygame.mouse.get_pressed()[0]:
                    self.check_clicks()
                    click_clock = 0
            else:
                click_clock += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

    
if __name__ == "__main__":
    pygame.font.init()
    game = Game()
    game.run()
