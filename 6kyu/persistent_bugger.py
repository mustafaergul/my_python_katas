from functools import reduce


def persistent(num):
    counter = 0
    while num > 9:
        num = reduce(lambda x, y: x * y, [int(i) for i in str(num)])
        counter += 1
    print(counter)


persistent(39)
persistent(4)
persistent(25)
persistent(999)
