def phone(parr):
    print(f"({''.join([str(i) for i in parr[0:3]])}) {''.join([str(i) for i in parr[3:6]])}-{''.join([str(i) for i in parr[6:10]])}")


phone([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
