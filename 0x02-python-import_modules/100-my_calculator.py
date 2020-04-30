#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    if argv[2] != '+' and argv[2] != '-' and argv[2] != '*' and argv[2] != '/':
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == '+':
        summ = add(a, b)
    if argv[2] == '-':
        summ = sub(a, b)
    if argv[2] == '*':
        summ = mul(a, b)
    if argv[2] == '/':
        summ = div(a, b)
    print('{} {} {} = {}'.format(a, argv[2], b, summ))
