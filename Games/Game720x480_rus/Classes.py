#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pygame.sprite import Sprite
import pygame, sys
import pyganim
from Mathematics import *


pygame.init()

class Player(Sprite):
    def __init__(self, x, y, lives, picts, gravity, character):
        Sprite.__init__(self)
        self.image = pygame.Surface((70, 70))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.blit_pos_x, self.blit_pos_y = self.rect.x, self.rect.y
        self.w, self.h = self.rect.size
        self.speedx = 0
        self.speedy = 0
        self.move_speed = 7
        self.jump_power = 7
        self.left = self.right = self.up = self.down = False
        self.onGround = True
        self.picts = picts
        self.lives = lives
        self.gravity = gravity
        self.character = character
        self.calculating = False
        self.anim_delay = 1
        
        
        self.boltAnimStay = pyganim.PygAnimation([(self.picts[0], self.anim_delay)])
        self.boltAnimStay.play()

        self.boltAnimLeft = pyganim.PygAnimation([(self.picts[1], self.anim_delay)])
        self.boltAnimLeft.play()

        self.boltAnimRight = pyganim.PygAnimation([(self.picts[2], self.anim_delay)])
        self.boltAnimRight.play()

        self.boltAnimUp = pyganim.PygAnimation([(self.picts[3], self.anim_delay)])
        self.boltAnimUp.play()


    def update(self, s_w, s_h, world, enemy, problem_string, window, new_problem):
        if self.left:
            self.speedx = -self.move_speed
            self.image.fill((255, 255, 255))
            self.boltAnimLeft.blit(self.image, (0, 0))

        if self.right:
            self.speedx = self.move_speed
            self.image.fill((255, 255, 255))
            self.boltAnimRight.blit(self.image, (0, 0))

        if not (self.left or self.right):
            self.speedx = 0
            if not self.up:
                self.image.fill((255, 255, 255))
                self.boltAnimStay.blit(self.image, (0, 0))

        if self.up:
            if self.character == 'Валли' and self.onGround:
                self.speedy = -self.jump_power
                self.image.fill((255, 255, 255))
                self.boltAnimUp.blit(self.image, (0, 0))
                self.onGround = False
            if self.character == 'Ева':
                self.speedy = -self.move_speed
                self.image.fill((255, 255, 255))
                self.boltAnimUp.blit(self.image, (0, 0))
                self.onGround = False
                
        if self.down and self.character == 'Ева':
            self.speedy = self.move_speed
            self.image.fill((255, 255, 255))
            self.boltAnimUp.blit(self.image, (0, 0))

        if not self.onGround and self.character == 'Валли':
            self.speedy += self.gravity

        self.rect.x += self.speedx     
        if self.rect.x > world.w - self.rect.w:
            self.rect.x = world.w - self.rect.w
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x < s_w/2:
            self.blit_pos_x = self.rect.x
        elif self.rect.x > world.w - s_w/2:
            self.blit_pos_x = self.rect.x - world.w + s_w
        else:
            self.blit_pos_x = s_w/2
            world.x += -self.speedx
        self.collide(self.speedx, 0, enemy, problem_string, window, new_problem)

        self.rect.y += self.speedy     
        if self.rect.y < -s_h:
            self.rect.y = -s_h
        if self.rect.y > s_h - self.rect.h:
            self.rect.y = s_h - self.rect.h
            self.onGround = True
        if self.rect.y > s_h/2:
            self.blit_pos_y = self.rect.y
        elif self.rect.y < -s_h + s_h/2:
            self.blit_pos_y = self.rect.y + world.h - s_h
        else:
            self.blit_pos_y = s_h/2
            world.y += -self.speedy
        self.collide(0, self.speedy, enemy, problem_string, window, new_problem)
        
        

    def collide(self, speedx, speedy, enemy, problem_string, window, new_problem):
        if self.rect.colliderect(enemy.rect):
            if speedx > 0:
                self.rect.right = enemy.rect.left - 15
            if speedx < 0:
                self.rect.left = enemy.rect.right + 15
            if speedy > 0:
                self.rect.bottom = enemy.rect.top - 15
                self.onGround = True
            problem_string.update(window, u'Переведите {0}ичное число {1} в {2}ичную систему счисления'.format(new_problem['from'], new_problem['problem'], new_problem['to']))
            self.calculating = True


class Enemy(Sprite):
    def __init__(self, x, y, lives, picts):
        Sprite.__init__(self)
        self.image = pygame.Surface((80, 80))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.blit_pos_x, self.blit_pos_y = self.rect.x, self.rect.y
        self.w, self.h = self.rect.size
        self.picts = picts
        self.lives = lives
        self.right = True
        self.left = False
        self.anim_delay = 1

        self.boltAnimLeft = pyganim.PygAnimation([(picts[0], self.anim_delay)])
        self.boltAnimLeft.play()

        self.boltAnimRight = pyganim.PygAnimation([(picts[1], self.anim_delay)])
        self.boltAnimRight.play()


    def update(self):
        if self.right:
            self.image.fill((255, 255, 255))
            self.boltAnimLeft.blit(self.image, (0, 0))

        if self.left:
            self.image.fill((255, 255, 255))
            self.boltAnimRight.blit(self.image, (0, 0))


    def blit_right(self, player, s_w, s_h, world):
        if player.blit_pos_x > s_w/2:
            self.blit_pos_x = s_w - self.w
            self.rect.x = self.blit_pos_x - s_w + world.w
        else:
            self.blit_pos_x = self.rect.x = world.w

        if player.blit_pos_y > s_h/2:
            self.blit_pos_y = self.rect.y = s_h - self.h
        else:
            self.blit_pos_y = self.rect.y = world.h


    def blit_left(self, player, s_w, s_h, world):
        if player.blit_pos_x < s_w/2:
            self.blit_pos_x = self.rect.x = 0
        else:
            self.blit_pos_x = self.rect.x = 0 - self.w

        if player.blit_pos_y > s_h/2:
            self.blit_pos_y = self.rect.y = s_h - self.h
        else:
            self.blit_pos_y = self.rect.y = world.h


class World:
    def __init__(self, x, y, s_w, s_h):
        self.x, self.y = x, y
        self.w, self.h = s_w * 2, s_h * 2

    def update(self):
        if self.x < -self.w/2:
            self.x = -self.w/2
        if self.x > 0:
            self.x = 0
        if self.y < -self.h/2:
            self.y = -self.h/2
        if self.y > 0:
            self.y = 0

            
class InputBox:
    def __init__(self, x, y, w, h, font, text = '' ):
        self.rect = pygame.Rect(x, y, w, h)
        self.inactive_colour = (255, 255, 0)
        self.active_colour = (255, 0, 0)
        self.font = font
        self.colour = self.inactive_colour
        self.text = text
        self.text_surf = self.font.render(text, True, self.colour)
        self.answer = ''
        self.done = False
        self.active = False
 
    def handle_event(self, e, window, player):
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            if self.rect.collidepoint(e.pos):
                self.active = True
                self.colour = self.active_colour
            else:
                self.active = False
                self.colour = self.inactive_colour
 
        if e.type == pygame.KEYDOWN:
            if self.active:
                if e.key == pygame.K_RETURN:
                    if player.calculating:
                        self.answer = self.text
                        self.done = True
                        self.text = ''
                    else:
                        self.text = ''
                elif e.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += e.unicode.upper()
            pygame.key.set_repeat(1, 1)
            window.fill((0, 0, 0))
            self.text_surf = self.font.render(self.text, False, self.colour)

    def render(self, window):
        window.blit(self.text_surf, self.rect.midtop)
        pygame.draw.rect(window, self.colour, self.rect, 2)

class InfoString:
    def __init__(self, x, y, w, h, font, colour, extra_colour, mid_text, left_text = '', right_text = ''):
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.colour = colour
        self.extra_colour = extra_colour
        self.colour = colour
        self.mid_text = mid_text
        self.left_text = left_text
        self.right_text = right_text
        self.text_surf_mid = self.font.render(mid_text, False, self.extra_colour)
        self.text_surf_left = self.font.render(left_text, False, self.colour)
        self.text_surf_right = self.font.render(right_text, False, self.colour)

    def update(self, window, mid_text, left_text = '', right_text = ''):
        window.fill((0, 0, 0))
        self.text_surf_mid = self.font.render(mid_text, False, self.extra_colour)
        self.text_surf_left = self.font.render(left_text, False, self.colour)
        self.text_surf_right = self.font.render(right_text, False, self.colour)
     
    def render(self, window):
        window.blit(self.text_surf_mid, (window.get_width()/2 - self.text_surf_mid.get_width()/2, self.rect.y))
        window.blit(self.text_surf_left, (self.rect.x + 5, self.rect.y))
        window.blit(self.text_surf_right, (window.get_width() - self.text_surf_right.get_width() - 5, self.rect.y))
        pygame.draw.rect(window, (255, 255, 0), self.rect, 2)




