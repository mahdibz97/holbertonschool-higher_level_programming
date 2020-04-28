#!/usr/bin/python3
def remove_char_at(str, n):
    char = ""
    for i in range(0, len(str)):
        if i != n:
            char += str[i]
    return char
