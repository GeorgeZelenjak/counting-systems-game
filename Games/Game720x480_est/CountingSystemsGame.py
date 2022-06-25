#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame, sys
from Slides import *
from Level import *

pygame.init()
pygame.font.init()


size = (720, 480)
window = pygame.display.set_mode(size)
pygame.display.set_caption(u'CountingSystemsGame')
screen = pygame.Surface(size)


pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.mixer.music.load('Mozart.ogg')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)


active_colour = (255, 0, 0)
inactive_colour = (255, 255, 0)


points_menu = [[size[0]/2 - 93, size[1]/2 - 60, u'Start', inactive_colour, active_colour, 0],
                [size[0]/2 - 72, size[1]/2 + 30, u'Quit', inactive_colour, active_colour, 1]]

start_menu = Menu(points_menu, u'Counting Systems Game', 55)

if start_menu.menu_loop() == 1:
    sys.exit()


points_difficulty = [[size[0]/2 - 97, size[1]/2 - 90, u'Kerge', inactive_colour, active_colour, 0],
                     [size[0]/2 - 155, size[1]/2, u'Keskmine', inactive_colour, active_colour, 1],
                     [size[0]/2 - 97, size[1]/2 + 90, u'Raske', inactive_colour, active_colour, 2]]

select_difficulty = Menu(points_difficulty, u'Palun valige raskusaste:', 52)

difficulty = select_difficulty.menu_loop()

if difficulty == 0:
    difficulty = 'Kerge'
    player_lives = 7
    enemy_lives = 10
elif difficulty == 1:
    difficulty = 'Keskmine'
    player_lives = 6
    enemy_lives = 12
else:
    difficulty = 'Raske'
    player_lives = 5
    enemy_lives = 15


points_system = [[size[0]/2 - 17, size[1]/2 - 90, '2', inactive_colour, active_colour, 0],
                 [size[0]/2 - 17, size[1]/2, '8', inactive_colour, active_colour, 1],
                 [size[0]/2 - 37, size[1]/2 + 90, '16', inactive_colour, active_colour, 2]]

select_system = Menu(points_system, 'Palun valige arvutussüsteem:', 44)

system = select_system.menu_loop()

if system == 0:
    system = 'kahend'
    bg = pygame.image.load('marsh.png').convert()
    music = 'Dvorak.ogg'
    enemy_picts = ['marshmonster_left.png', 'marshmonster_right.png']
elif system == 1:
    system = 'kaheksand'
    bg = pygame.image.load('ruins.png').convert()
    music = 'Wagner.ogg'
    enemy_picts = ['troll_left.png', 'troll_right.png']
else:
    system = 'kuueteistkümnend'
    bg = pygame.image.load('hell.png').convert()
    music = 'Orff.ogg'
    enemy_picts = ['devil_left.png', 'devil_right.png']


points_characters = [[size[0]/2 - 90, size[1]/2 - 70, u'WALLE', inactive_colour, active_colour, 0],
                 [size[0]/2 - 53, size[1]/2 + 20, u'EVE', inactive_colour, active_colour, 1]]

select_character = Menu(points_characters, 'Palun valige tegelast:', 60)

character = select_character.menu_loop()

if character == 0:
    character = 'WALLE'
    player_picts = ['walle.png', 'walle_left.png', 'walle_right.png', 'walle.png']
    gravity = 0.4
else:
    character = 'EVE'
    player_picts = ['eve.png', 'eve_left.png', 'eve_right.png', 'eve_up.png']
    gravity = 0


pygame.mixer.music.stop()

intro()

winner = level(player_lives, enemy_lives, player_picts, enemy_picts, music, bg, gravity, character, system, difficulty)


if winner == 'player':
    text = 'You won!' 
else:
    text = 'Game over'
outcome(text)
pygame.mixer.music.stop()

exec(open('CountingSystemsGame.py', encoding = 'UTF-8-sig').read())

input()
