#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    sum = 0    
    rom = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    for i in range(len(roman_string)):
        if roman_string[i] in rom:
                if i > 0 and rom[roman_string[i]] > rom[roman_string[i - 1]]:
                    sum += (rom[roman_string[i]] - 2 * rom[roman_string[i - 1]])
                else:
                    sum += rom[roman_string[i]]
        else:
            return 0
    return sum
