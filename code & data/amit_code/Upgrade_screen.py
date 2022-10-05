import pygame
from settings import *
from invetory_system import *

class Upgrade:
    def __init__(self,player):
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.attribute_nr = len(player.stats)
        self.attribute_names = list(player.stats.keys())
        self.font = pygame.font.Font(UPGRADE_FONT, UI_FONT_SIZE)
        self.stats_names = ['health','energy','attack','magic','speed']

        #selection system
        self.selection_index = 0
        self.can_move = True
        self.selection_time = None

        #items dimensions
        self.height = self.display_surface.get_size()[1] * 0.3
        self.width = self.display_surface.get_size()[0] * 0.25
        self.background = pygame.Rect(0,0,WINDOW_WIDTH,WINDOW_HEIGHT)
        self.can_draw = True

        #invetory section
        self.big_rect = invetory_slot()

    def input(self):
        keys = pygame.key.get_pressed()
        if self.can_move:
            if keys[pygame.K_DOWN] and self.selection_index < self.attribute_nr - 1 :
                self.selection_index += 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()


            if keys[pygame.K_UP] and self.selection_index >= 1:
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

    def display_stats(self):
        pass

    def draw_text(self,text,color,pos):
        draw_text = self.font.render(text,True,color)
        self.display_surface.blit(draw_text, pos)

    def upgrade_screen(self):
        self.input()
        self.selection_cooldown()
        pygame.draw.rect(self.display_surface,backgournd_color,self.background)
        self.draw_text('health: '+ str(self.player.stats['health']), (255, 255, 255), (30, 40))
        self.draw_text('energy: '+ str(self.player.stats['energy']),(255,255,255),(30,100))
        self.draw_text('attack: '+ str(self.player.stats['attack']), (255, 255, 255), (30, 160))
        self.draw_text('magic: '+ str(self.player.stats['magic']), (255, 255, 255), (30, 220))
        self.draw_text('speed: '+ str(self.player.stats['speed']), (255, 255, 255), (30, 280))
        self.draw_text('total exp: ' + str(self.player.exp), (0, 45, 255), (30, 660))
        self.big_rect.draw_test()
        self.big_rect.display_slot()
class Upgrade_box:
    def __init__(self,display_surface,l,t,w,h,index):
        self.index = index
        self.Rect = pygame.Rect(l,t,w,h)
        self.display_surface = display_surface
        self.box_color = (23,0,6)

    def draw_box(self):
        pygame.draw.rect(self.display_surface,self.box_color,self.Rect)\

