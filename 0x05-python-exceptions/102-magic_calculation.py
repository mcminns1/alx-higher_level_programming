#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exceptions('Too far')

            result += a ** b / 1
        except:
            result = b + a
            break

        return result
