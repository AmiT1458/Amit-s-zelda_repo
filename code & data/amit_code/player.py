import pygame
from settings import *
import os
from support import *
from entity import Entity

class Player(Entity):
    def __init__(self,pos,groups,obstacle_sprites,create_attack,destroy_weapon,create_magic):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.obstacle_sprites = obstacle_sprites


        self.hitbox = self.rect.inflate(0,-26)

        self.import_player_assets()
        #movement
        #self.direction = pygame.math.Vector2()
        self.speed = 5
        #self.frame_index = 0
        #self.animation_speed = 0.15
        self.attacking = False
        self.attacking_cooldown = 400
        self.attacking_time = 0
        self.status = 'down'
        self.current_time = pygame.time.get_ticks()
        self.destroy_weapon = destroy_weapon

        #weapon
        self.create_attack = create_attack
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]
        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.switch_duration_cooldown = 200

        #magic
        self.create_magic = create_magic
        self.magic_index = 0
        self.magic = list(magic_data.values())[self.magic_index]
        self.can_switch_magic = True
        self.magic_switch_time = None

        self.stats = {'health' : 100 , 'energy': 60 ,'attack':10,'magic':4,'speed':6}
        self.max_stats = {'health': 300, 'energy': 140, 'attack': 20, 'magic': 10, 'speed': 10}
        self.upgrade_cost = {'health': 100, 'energy': 100, 'attack': 100, 'magic': 100, 'speed': 100}
        self.health = self.stats['health']
        self.energy = self.stats['energy']
        self.exp = 500
        self.speed = self.stats['speed']

        # hit timer
        self.vulnerable = True
        self.hurt_time = None
        self.invulnerability_duration = 500


    def import_player_assets(self):
        character_path = '../graphics/player/'

        self.animations = {'up': [],'down': [],'left': [], 'right':[],
            'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
                'right_attack':[],'left_attack':[],'up_attack':[],'down_attack':[] }

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        keys = pygame.key.get_pressed()

        #movement keys
        if not self.attacking:

            if keys[pygame.K_w]: #up
                self.direction.y = -1
                self.status = 'up'

            elif keys[pygame.K_s]: # down
                self.direction.y = 1
                self.status = 'down'

            else:
                self.direction.y = 0
            if keys[pygame.K_d]: # right
                self.direction.x = 1
                self.status = 'right'
            elif keys[pygame.K_a]: # left
                self.direction.x = -1
                self.status = 'left'
            else:
                self.direction.x = 0

            if keys[pygame.K_SPACE] and not self.attacking:
                self.attacking = True
                self.attacking_time = pygame.time.get_ticks()
                self.create_attack()
                #print('attack!')

            if keys[pygame.K_LCTRL] and not self.attacking:
                self.attacking = True
                self.attacking_time = pygame.time.get_ticks()
                style = list(magic_data.keys())[self.magic_index]
                strength = list(magic_data.values())[self.magic_index]['strength'] + self.stats['magic']
                cost = list(magic_data.values())[self.magic_index]['cost']
                self.create_magic(style,strength,cost)

            if keys[pygame.K_q] and self.can_switch_weapon:
                self.can_switch_weapon = False
                self.weapon_switch_time = pygame.time.get_ticks()
                if self.weapon_index < len(list(weapon_data.keys())) - 1:
                    self.weapon_index += 1
                else:
                    self.weapon_index = 0
                self.weapon = list(weapon_data.keys())[self.weapon_index]

            if keys[pygame.K_e] and self.can_switch_magic:
                self.can_switch_magic = False
                self.magic_switch_time = pygame.time.get_ticks()
                if self.magic_index < len(list(magic_data.keys())) - 1:
                    self.magic_index += 1
                else:
                    self.magic_index = 0
                self.magic = list(magic_data.values())[self.magic_index]

    def get_status(self):


        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and 'attack' not in self.status:
                self.status = self.status + '_idle'


        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('idle','attack')

                else:
                    self.status = self.status + '_attack'

        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack','_idle')


    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.attacking_time >= self.attacking_cooldown + weapon_data[self.weapon]['cooldown']:
            self.attacking = False
            self.destroy_weapon()
        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
                self.can_switch_weapon = True

        if not self.can_switch_magic:
            if current_time - self.magic_switch_time >= self.switch_duration_cooldown:
                self.can_switch_magic = True

        if not self.vulnerable:
            if current_time - self.hurt_time >= self.invulnerability_duration:
                self.vulnerable = True


    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center= self.hitbox.center)

        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)

        else:
            self.image.set_alpha(255)
    def get_full_damage(self):

        base_damage = self.stats['attack']
        weapon_damage = weapon_data[self.weapon]['damage']
        return base_damage + weapon_damage

    def get_full_magic_damage(self):
        base_damage = self.stats['magic']
        spell_damage = self.magic['strength']
        return spell_damage + base_damage

    def check_player_death(self):
        if self.health <= 0:
            pass
            #print('you died')

    def energy_recovery(self):
        if self.energy < self.stats['energy']:
            self.energy += 0.01 * self.stats['magic']
        else:
            self.energy = self.stats['energy']

    def update(self):
        self.input()
        self.cooldowns()
        self.check_player_death()
        self.get_status()
        self.animate()
        self.move(self.speed)
        self.energy_recovery()

