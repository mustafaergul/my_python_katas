def broken(n):
    print(''.join(["1" if i == "0" else "0" for i in list(n)]))


broken("01010101111")
