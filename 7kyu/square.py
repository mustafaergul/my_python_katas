import math


def square(n):
    return n > -1 and math.sqrt(n) % 1 == 0


square(25)
square(22)
square(0)
square(-1)
