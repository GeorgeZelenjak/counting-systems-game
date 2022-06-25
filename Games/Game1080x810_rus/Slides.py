#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame, sys


class Menu:
    def __init__(self, points, title, font_size):
        self.points = points
        self.image = pygame.image.load('picts/menu.png').convert()
        self.image.get_rect()
        self.title = title
        self.font_size = font_size


    def render(self, place, font, point_num):
        for point in self.points:
            if point_num == point[5]:
                place.blit(font.render(point[2], True, point[4]), (point[0], point[1]))
            else:
                place.blit(font.render(point[2], True, point[3]), (point[0], point[1]))

    def return_choice(self, selected_point):
        if selected_point == 0:
            return 0
        if selected_point == 1:
            return 1
        if selected_point == 2:
            return 2


    def menu_loop(self):
        pygame.font.init()
        font_menu = pygame.font.SysFont('IMPACT', 100)
        title_font = pygame.font.SysFont('IMPACT', self.font_size)
        title = title_font.render(self.title, True, (0, 255, 0))

        window = pygame.display.set_mode((1080, 810))
        menu_screen = pygame.Surface((1080, 810))
        
        pygame.mouse.set_visible(True)

        point = 0
        loop = True

        while loop:
            menu_screen.fill((0, 0, 0))
            menu_screen.blit(self.image, (0, 0))
            mouse_pos = pygame.mouse.get_pos()
            for i_point in self.points:
                if mouse_pos[0] > i_point[0] and mouse_pos[0] < i_point[0] + 300 and mouse_pos[1] > i_point[1] and mouse_pos[1] < i_point[1] + 100:
                    point = i_point[5]
                self.render(menu_screen, font_menu, point)


            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if point > 0:
                            point -= 1
                    if e.key == pygame.K_DOWN:
                        if point < len(self.points) - 1:
                            point += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1 or e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                    choice = self.return_choice(point)
                    return choice
                    loop = False

            
            menu_screen.blit(title, (window.get_width()/2 - title.get_width()/2, 50))
            window.blit(menu_screen, (0, 0))
            pygame.key.set_repeat(0, 0)
            pygame.time.Clock().tick(30)
            pygame.display.flip()


def intro():
    pygame.font.init()

    window = pygame.display.set_mode((1080, 810))
    screen = pygame.Surface((1080, 810))
    
    pygame.key.set_repeat(0, 0)
    pygame.mouse.set_visible(1)


    text_font = pygame.font.SysFont('Segoe Script', 32)


    text1 = text_font.render(u'Добро пожаловать в игру!', True, (255, 255, 0))
    text2 = text_font.render(u'Чтобы выиграть, нужно правильно решить примеры.', True, (255, 255, 0))
    text3 = text_font.render(u'Для передвижения используйте стрелки и пробел.', True, (255, 255, 0))
    text4 = text_font.render(u'Внизу экрана находится строка для ввода ответов.', True, (255, 255, 0))
    text5 = text_font.render(u'Для ее активации нажмите на нее мышью.', True, (255, 255, 0))
    text6 = text_font.render(u'Если выбрали \'сложный\' уровень сложности, то ответ', True, (255, 255, 0))
    text7 = text_font.render(u'округляйте ВНИЗ ДО ДВУХ ЦИФР ПОСЛЕ ЗАПЯТОЙ!', True, (255, 255, 0))
    text8 = text_font.render(u'Не делайте глупостей! Приятной игры!', True, (255, 255, 0))
    text9 = text_font.render(u'Нажмите ENTER, чтобы начать игру', True, (255, 255, 0))

    texts = [text1, text2, text3, text4, text5, text6, text7, text8, text9]

    loop = True
    while loop:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    loop = False

        screen.fill((0, 0, 0))
        counter = 0
        for text in texts:
            screen.blit(text, (window.get_width()/2 - text.get_width()/2, counter * 70 + 100))
            counter += 1
        window.blit(screen, (0, 0))
        pygame.time.Clock().tick(30)
        pygame.display.flip()


def outcome(text):
    pygame.font.init()

    window = pygame.display.set_mode((1080, 810))
    screen = pygame.Surface((1080, 810))

    text_font1 = pygame.font.SysFont('COMIC SANS MS', 80, bold = True)
    text_font2 = pygame.font.SysFont('IMPACT', 30)

    title = text_font1.render(text, True, (255, 255, 0))
    info = text_font2.render(u'Нажмите ENTER', True, (255, 255, 0))

    pygame.key.set_repeat(0, 0)
    pygame.mouse.set_visible(True)

    loop = True
    while loop:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    loop = False

        screen.fill((0, 0, 0))
        screen.blit(title, (window.get_width()/2 - title.get_width()/2, window.get_height()/2 - title.get_height()))
        screen.blit(info, (window.get_width()/2 - info.get_width()/2, window.get_height()/2 + info.get_height()))
        window.blit(screen, (0, 0))
        pygame.time.Clock().tick(30)
        pygame.display.flip()
