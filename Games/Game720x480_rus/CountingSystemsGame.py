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
pygame.mixer.music.load('music/Mozart.ogg')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)


active_colour = (255, 0, 0)
inactive_colour = (255, 255, 0)


points_menu = [[size[0]/2 - 73, size[1]/2 - 75, u'Старт', inactive_colour, active_colour, 0],
                [size[0]/2 - 88, size[1]/2 + 25, u'Выход', inactive_colour, active_colour, 1]]

start_menu = Menu(points_menu, u'Counting Systems Game', 70)

if start_menu.menu_loop() == 1:
    sys.exit()


points_difficulty = [[size[0]/2 - 92, size[1]/2 - 100, u'Легкий', inactive_colour, active_colour, 0],
                     [size[0]/2 - 117, size[1]/2, u'Средний', inactive_colour, active_colour, 1],
                     [size[0]/2 - 129, size[1]/2 + 100, u'Сложный', inactive_colour, active_colour, 2]]

select_difficulty = Menu(points_difficulty, u'Выберите уровень сложности:', 52)

difficulty = select_difficulty.menu_loop()

if difficulty == 0:
    difficulty = 'Легкий'
    player_lives = 5
    enemy_lives = 10
elif difficulty == 1:
    difficulty = 'Средний'
    player_lives = 6
    enemy_lives = 12
else:
    difficulty = 'Сложный'
    player_lives = 5
    enemy_lives = 15


points_system = [[size[0]/2 - 16, size[1]/2 - 100, '2', inactive_colour, active_colour, 0],
                 [size[0]/2 - 16, size[1]/2, '8', inactive_colour, active_colour, 1],
                 [size[0]/2 - 25, size[1]/2 + 100, '16', inactive_colour, active_colour, 2]]

select_system = Menu(points_system, u'Выберите систему счисления:', 52)

system = select_system.menu_loop()

if system == 0:
    system = 'дво'
    bg = pygame.image.load('picts/marsh.png').convert()
    music = 'music/Dvorak.ogg'
    enemy_picts = ['picts/marshmonster_left.png', 'picts/marshmonster_right.png']
elif system == 1:
    system = 'восьмер'
    bg = pygame.image.load('picts/ruins.png').convert()
    music = 'music/Wagner.ogg'
    enemy_picts = ['picts/troll_left.png', 'picts/troll_right.png']
else:
    system = 'шестнадцатер'
    bg = pygame.image.load('picts/hell.png').convert()
    music = 'music/Orff.ogg'
    enemy_picts = ['picts/devil_left.png', 'picts/devil_right.png']


points_characters = [[size[0]/2 - 82, size[1]/2 - 75, u'Валли', inactive_colour, active_colour, 0],
                 [size[0]/2 - 43, size[1]/2 + 25, u'Ева', inactive_colour, active_colour, 1]]

select_character = Menu(points_characters, u'Выберите персонажа:', 65)

character = select_character.menu_loop()

if character == 0:
    character = 'Валли'
    player_picts = ['picts/walle.png', 'picts/walle_left.png', 'picts/walle_right.png', 'picts/walle.png']
    gravity = 0.4
else:
    character = 'Ева'
    player_picts = ['picts/eve.png', 'picts/eve_left.png', 'picts/eve_right.png', 'picts/eve_up.png']
    gravity = 0


pygame.mixer.music.stop()

intro()

winner = level(player_lives, enemy_lives, player_picts, enemy_picts, music, bg, gravity, character, system, difficulty)


if winner == 'player':
    text = 'Вы выиграли!' 
else:
    text = 'Вы проиграли'
outcome(text)
pygame.mixer.music.stop()

exec(open('CountingSystemsGame.py', encoding = 'UTF-8-sig').read())

input()
