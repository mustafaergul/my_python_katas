def square_digits(num):
    print(int(''.join([str(a) for a in [m ** 2 for m in [int(n) for n in str(num)]]])))


square_digits(9119)
