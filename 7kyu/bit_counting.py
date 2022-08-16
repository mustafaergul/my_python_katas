def bit_c(num):
    print(sum([int(n) for n in "{0:b}".format(num)]))


bit_c(1234)
