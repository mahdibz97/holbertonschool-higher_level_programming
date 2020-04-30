#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    arg = argv[2]    
    if arg != '+' and arg != '-' and arg != '*' and arg != '/':
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if arg == '+':
        summ = add(a, b)
    if arg == '-':
        summ = sub(a, b)
    if arg == '*':
        summ = mul(a, b)
    if arg == '/':
        summ = div(a, b)
    print('{} {} {} = {}'.format(a, arg, b, summ))
