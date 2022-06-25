#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame, sys
from Classes import *
from Mathematics import *


def level(lives1, lives2, picts1, picts2, music, bg, gravity, character, system, difficulty):
    pygame.init()
    pygame.font.init()


    window = pygame.display.set_mode((1080, 810))
    w_w, w_h = window.get_rect().size

    screen = pygame.Surface((1080, 720))
    s_w, s_h = screen.get_rect().size

    bg = pygame.transform.scale(bg, (s_w * 2, s_h * 2))

    world = World(0, -720, s_w, s_h)
    

    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.mixer.init()
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.4)


    player = Player(0, 595, lives1, picts1, gravity, character)

    enemy = Enemy(world.w, 570, lives2, picts2)

    sprites = pygame.sprite.Group(player, enemy)


    text_font = pygame.font.SysFont('COMIC SANS MS', 21)
    info_string = InfoString(0, 0, 1080, 30, text_font, (255, 0, 0), (0, 255, 255), u'Counting Systems Game', left_text = u'Ваши жизни: {0}'.format(player.lives), right_text = u'Жизни злодея: {0}'.format(enemy.lives))
    problem_string = InfoString(0, 30, 1080, 30, text_font, (0, 0, 0), (255, 0, 0), '')
    input_box = InputBox(0, 780, 1080, 30, text_font)


    new_problem = create_problem(difficulty, system)

    game_is_ended = False

    clock = pygame.time.Clock()
    pygame.key.set_repeat(1, 1)

    game_on = True

    while game_on:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    sys.exit()
                if e.key == pygame.K_LEFT:
                    player.left = True
                if e.key == pygame.K_RIGHT:
                    player.right = True
                if e.key == pygame.K_UP or e.key == pygame.K_SPACE:
                    player.up = True
                    player.onGround = False
                if e.key == pygame.K_DOWN:
                    player.down = True
                if e.key == pygame.K_RETURN and game_is_ended:
                    game_on = False
                    return winner

            if e.type == pygame.KEYUP:
                if e.key == pygame.K_LEFT:
                    player.left = False
                if e.key == pygame.K_RIGHT:
                    player.right = False
                if e.key == pygame.K_UP or e.key == pygame.K_SPACE:
                    player.up = False
                    player.speedy = 0
                if e.key == pygame.K_DOWN:
                    player.down = False
                    player.speedy = 0

            input_box.handle_event(e, window, player)
        

        if enemy.lives == 0:
            enemy.kill()
            game_is_ended = True
            winner = 'player'
            problem_string.update(window, u'Поздравляю! Вы выиграли! Нажмите ENTER для выхода из игры')
            problem_string.render(window)
            
        if player.lives == 0:
            player.kill()
            game_is_ended = True
            winner = 'enemy'
            problem_string.update(window, u'К сожалению, Вы проиграли! Нажмите ENTER для выхода из игры')
            problem_string.render(window)
            
        
        info_string.render(window)
        input_box.render(window)
        problem_string.render(window)

        player.update(s_w, s_h, world, enemy, problem_string, window, new_problem)


        if player.calculating:
            if input_box.done:
                player_input = input_box.answer.upper()
                input_box.answer = ''
                if player_input == new_problem['result']:
                    enemy.lives -= 1
                    problem_string.update(window, u'Правильно! Вы молодец!')
                    problem_string.render(window)
                else:
                    player.lives -= 1
                    problem_string.update(window, u'К сожалению, неверно. Правильный ответ {0}'.format(new_problem['result']))
                    problem_string.render(window)


                info_string.update(window, u'Counting Systems Game', left_text = u'Ваши жизни: {0}'.format(player.lives), right_text = u'Жизни злодея: {0}'.format(enemy.lives))
                input_box.done = False
                player.calculating = False

                if player.lives > 0:
                    if enemy.right:
                        enemy.right = False
                        enemy.left = True
                    else:
                        enemy.left = False
                        enemy.right = True
                new_problem = create_problem(difficulty, system)
            

        world.update()
        screen.blit(bg, (world.x, world.y))
        

        if enemy.alive():
            enemy.update()
            if enemy.left:
                enemy.blit_left(player, s_w, s_h, world)
            if enemy.right:
                enemy.blit_right(player, s_w, s_h, world)


        for sprite in sprites:
            screen.blit(sprite.image, (sprite.blit_pos_x, sprite.blit_pos_y))
        

        if not player.alive():
            enemy.update()
            if enemy.left:
                screen.blit(enemy.image, (0, s_h - enemy.h))
            if enemy.right:
                screen.blit(enemy.image, (s_w - enemy.w, s_h - enemy.h))

            
        window.blit(screen, (0, 60))

        pygame.display.flip()
        dt = 60
        clock.tick(dt)
