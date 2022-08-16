def missing_no(arr):
    print((set(range(101)) - set(arr)).pop())


arr2 = list(range(1, 99))
arr2.remove(29)
missing_no(arr2)
