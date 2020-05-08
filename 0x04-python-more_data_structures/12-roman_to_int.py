#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    sum = 0
    rm = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    for j in range(len(roman_string)):
        if roman_string[j] in rm:
                if j > 0 and rm[roman_string[j]] > rm[roman_string[j - 1]]:
                    sum += (rm[roman_string[j]] - 2 * rm[roman_string[j - 1]])
                else:
                    sum += rm[roman_string[j]]
        else:
            return 0
    return sum
