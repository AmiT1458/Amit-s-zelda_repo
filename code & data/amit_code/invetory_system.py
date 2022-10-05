import pygame
from settings import *

class invetory_slot:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.height = 40
        self.width = 40
        self.offset = 15
        self.rect = pygame.Rect(WINDOW_WIDTH * 0.3,10 , WINDOW_WIDTH * 0.5 -20, WINDOW_HEIGHT - 20)
        self.Rect_slot = pygame.Rect(WINDOW_WIDTH * 0.3,10 + self.offset , self.width, self.height)
        self.White = (255,255,255)

    def draw_test(self):
        pygame.draw.rect(self.display_surface,self.White,self.rect,6)

    def display_slot(self):
        for i in range(6):
            pygame.draw.rect(self.display_surface,self.White,self.Rect_slot,4)