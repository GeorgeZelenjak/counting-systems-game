#!/usr/bin/env python3

intconverter = {0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9', 10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
stringconverter = {'0': 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}

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

choice = input('Kas soovite teisendada kümnendsüsteemi või kümnendsüsteemist (kumnendsusteemi/kumnendsusteemist)?\n').lower()
if choice == 'kumnendsusteemi':
	base = int(input('Sisestage praeguse süsteemi alus (kuni 16 k.a):\n'))
	number = input('Sisestage number:\n').upper()
	answer = baseconverter_toDecimal(number, base)
elif choice == 'kumnendsusteemist':
	base = int(input('Sisestage süsteemi alus, kuhu tahate teisendada (kuni 16 k.a):\n'))
	number = input('Sisestage number:\n').upper()
	answer = baseconverter_fromDecimal(number, base)
else:
	process = True
	while process:
		choice = input('Kas soovite teisendada kümnendsüsteemi või kümnendsüsteemist (kumnendsusteemi/kumnendsusteemist)?\n').lower()
		if choice == 'kumnendsusteemi':
			base = int(input('Sisestage praeguse süsteemi alus (kuni 16 k.a):\n'))
			number = input('Sisestage number:\n').upper()
			answer = baseconverter_toDecimal(number, base)
			process = False
		elif choice == 'kumnendsusteemist':
			base = int(input('Sisestage süsteemi alus, kuhu tahate teisendada (kuni 16 k.a):\n'))
			number = input('Sisestage number:\n').upper()
			answer = baseconverter_fromDecimal(number, base)
			process = False

print("Vastus:")
print(answer)

