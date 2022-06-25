#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


intconverter = {0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9', 10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
stringconverter = {'0': 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}

bin_alphabet = ['0', '1']
oct_alphabet = ['0', '1', '2', '3', '4', '5', '6', '7']
dec_alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
hex_alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def baseconverter_fromDecimal(num, base):
    result = ''
    if '.' in num:
        parts = num.split('.')
        wholepart = int(parts[0])
        decpart = parts[1]
    else:
        wholepart = int(num)
    while wholepart >= base:
        remain = wholepart % base
        remain = intconverter[remain]
        result += remain
        wholepart //=  base
    wholepart = intconverter[wholepart]
    result += wholepart
    result = result[::-1]
    if '.' not in num:
        return result
    else:
        result += '.'
        decpart = float('0.' + decpart)
        process = True
        counter = 0
        while process:
            decpart *= base
            parts = str(decpart).split('.')
            wholepart = intconverter[int(parts[0])]
            result += wholepart
            decpart = parts[1]
            counter += 1
            if decpart == 0 or counter == 10:
                process = False
            else:
                decpart = float('0.' + decpart)
        return result


def baseconverter_toDecimal(num, base):
    result = 0
    if '.' in num:
        parts = num.split('.')
        wholepart = parts[0]
        decpart = parts[1]
    else:
        wholepart = num
    power = len(wholepart) - 1
    for i in wholepart:
        i = stringconverter[i]
        result += i * (base ** power)
        power -= 1
    if '.' not in num:
        return str(result)
    else:
        power = -1
        for i in decpart:
            i = stringconverter[i]
            result += i * (base ** power)
            power -= 1
        return str(result)


def int_generator(alphabet, min_len, max_len):
    integers = []
    for i in range(random.randint(min_len, max_len)):
        integers.append(random.choice(alphabet))
        integer = ''.join(integers)
        if len(integer) > 1:
            for i in integer:
                if len(integer) > 1:
                    if i == '0':
                        integer = integer[1:]
                    else:
                        break
    return integer


def float_generator(alphabet, min_len1, max_len1, min_len2, max_len2):
    int_parts = []
    for i in range(random.randint(min_len1, max_len1)):
        int_parts.append(random.choice(alphabet))
        int_part = ''.join(int_parts)
        if len(int_part) > 1:
            for i in int_part:
                if len(int_part) > 1:
                    if i == '0':
                        int_part = int_part[1:]
                    else:
                        break
        int_part += '.'
        float_parts = []
        for i in range(random.randint(min_len2, max_len2)):
            float_parts.append(random.choice(alphabet))
        float_part = ''.join(float_parts)
        if len(float_part) > 1:
            float_part_copy = float_part[::-1]
            for i in float_part_copy:
                if len(float_part_copy) > 1:
                    if i == '0':
                        float_part_copy = float_part_copy[1:]
                    else:
                        break
            float_part = float_part_copy[::-1]
        number = int_part + float_part
    return number


def create_problem(difficulty, system):
    problems = []
    if system == 'дво':
        alphabet = bin_alphabet
        base = 2
    elif system == 'восьмер':
        alphabet = oct_alphabet
        base = 8
    else:
        alphabet = hex_alphabet
        base = 16
    if difficulty == 'Легкий':
        if system == 'дво':
            min_length = 2
            max_length = 4
        if system == 'восьмер':
            min_length = 2
            max_length = 3
        if system == 'шестнадцатер':
            min_length = 1
            max_length = 2
        problem1 = int_generator(alphabet, min_length, max_length)
        problems.append(problem1)
        problem2 = int_generator(dec_alphabet, 2, 3)
        problems.append(problem2)
    elif difficulty == 'Средний':
        if system == 'дво':
            min_length = 5
            max_length = 7
        if system == 'восьмер':
            min_length = 4
            max_length = 5
        if system == 'шестнадцатер':
            min_length = 3
            max_length = 4
        problem1 = int_generator(alphabet, min_length, max_length)
        problems.append(problem1)
        problem2 = int_generator(dec_alphabet, 4, 5)
        problems.append(problem2)
    else:
        if system == 'дво':
            min_length1 = 4
            max_length1 = 6
            min_length2 = 2
            max_length2 = 3
        if system == 'восьмер':
            min_length1 = 3
            max_length1 = 4
            min_length2 = 2
            max_length2 = 3
        if system == 'шестнадцатер':
            min_length1 = 2
            max_length1 = 3
            min_length2 = 1
            max_length2 = 2
        problem1 = float_generator(alphabet, min_length1, max_length1, min_length2, max_length2)
        problems.append(problem1)
        problem2 = float_generator(dec_alphabet, 3, 4, 2, 3)
        problems.append(problem2)

    problem = random.choice(problems)
    if problem == problem1:
        dest_syst = 'десят'
        start_syst = system
        result = baseconverter_toDecimal(problem, base)
        if '.' in result:
            parts = result.split('.')
            float_part = parts[1]
            if len(parts[1]) >= 3:
                float_part = float_part[:2]
                result = parts[0] + '.' + float_part

    else:
        dest_syst = system
        start_syst = 'десят'
        result = baseconverter_fromDecimal(problem, base)
        if '.' in result:
            parts = result.split('.')
            float_part = parts[1]
            if len(parts[1]) >= 3:
                float_part = float_part[:2]
                result = parts[0] + '.' + float_part

    created_problem = {'problem' : problem, 'result' : result, 'from' : start_syst, 'to' : dest_syst}
    return created_problem
