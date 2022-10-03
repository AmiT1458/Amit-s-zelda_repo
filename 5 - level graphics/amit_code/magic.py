import pygame
from settings import *
from particles import *
from random import randint
class MagicPlayer:
    def __init__(self,player_animation):
        self.player_animation = player_animation

    def heal(self,player,strength,cost,groups):
        if player.energy >= cost:
            player.health += strength
            player.energy -= cost
            if player.health >= player.stats["health"]:
                player.health = player.stats["health"]
            self.player_animation.create_particles('aura', player.rect.center, groups)
            self.player_animation.create_particles('heal',player.rect.center,groups)


        print('heal')

    def flame(self,player,cost,groups):
        if player.energy >= cost:
            player.energy -= cost

            if player.status.split('_')[0] == "right":  direction = pygame.math.Vector2(1,0)
            elif player.status.split('_')[0] == "left": direction = pygame.math.Vector2(-1,0)
            elif player.status.split('_')[0] == "down": direction = pygame.math.Vector2(0,1)
            else: direction = pygame.math.Vector2(0,-1)

            for i in range(1,6):
                if direction.x:
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x + randint(-TILESIZE // 3 ,TILESIZE // 3 )
                    y = player.rect.centery + randint(-TILESIZE // 3 ,TILESIZE // 3 )
                    self.player_animation.create_particles('flame',(x,y),groups)
                else:
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx + randint(-TILESIZE // 3 ,TILESIZE // 3 )
                    y = player.rect.centery + offset_y + randint(-TILESIZE // 3 ,TILESIZE // 3 )
                    self.player_animation.create_particles('flame',(x,y),groups)