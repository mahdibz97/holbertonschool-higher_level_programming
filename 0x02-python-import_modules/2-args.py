#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lenn = len(argv)
    if lenn == 1:
        print('{} arguments.'.format(lenn - 1))
    elif len == 2:
        print('{} argument:'.format(lenn - 1))
    else:
        print('{} arguments:'.format(lenn - 1))
    for i in range(1, lenn):
        print('{:d}: {:s}'.format(i, argv[i]))
