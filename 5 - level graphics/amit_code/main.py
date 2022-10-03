from settings import *
import pygame
import sys,time
from level import Level
from debug import debug

class Game:
    def __init__(self):

        # setup
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #1280 x 720
        pygame.display.set_caption('Amits Zelda')
        self.clock = pygame.time.Clock()
        self.level = Level()

        #graphics set up

    def run(self):
        #last_time = time.time()
        while True:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        self.level.display_upgrade()
            # game logic
            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
