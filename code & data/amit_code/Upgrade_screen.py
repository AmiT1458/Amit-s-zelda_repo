import pygame
from settings import *


class Upgrade:
    def __init__(self,player):
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.attribute_nr = len(player.stats)
        self.attribute_names = list(player.stats.keys())
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)


        #selection system
        self.selection_index = 0
        self.can_move = True
        self.selection_time = None


        #items dimensions
        self.height = self.display_surface.get_size()[1] * 0.3
        self.width = self.display_surface.get_size()[0] * 0.25
        self.box1 = Upgrade_box(self.display_surface,0,0,self.width,self.height,1)

    def input(self):
        keys = pygame.key.get_pressed()
        if self.can_move:
            if keys[pygame.K_RIGHT] and self.selection_index < self.attribute_nr - 1:
                self.selection_index += 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()


            if keys[pygame.K_LEFT] and self.selection_index >= 1:
                self.selection_index -= 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()

            if keys[pygame.K_SPACE]:
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                print(self.selection_index)

    def selection_cooldown(self):
        if not self.can_move:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 400:
                self.can_move = True


    def upgrade_screen(self):
        self.input()
        self.selection_cooldown()
        self.box1.draw_box()


class Upgrade_box:
    def __init__(self,display_surface,l,t,w,h,index):
        self.index = index
        self.Rect = pygame.Rect(l,t,w,h)
        self.display_surface = display_surface
        self.box_color = (23,0,6)

    def draw_box(self):
        pygame.draw.rect(self.display_surface,self.box_color,self.Rect)