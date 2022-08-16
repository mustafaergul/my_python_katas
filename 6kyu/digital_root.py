def digital_root(n):
    if n >= 10:
        n = sum([int(nu) for nu in str(n)])
        digital_root(n)
    else:
        print(n)


digital_root(16)
digital_root(942)
digital_root(132189)
digital_root(493193)
digital_root(10)
