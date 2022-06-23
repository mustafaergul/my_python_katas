def move_zeros(arr):
    for a in arr:
       if a == 0:
        arr.remove(a)
        arr.append(a)
    print(arr)


move_zeros([1, 0, 1, 2, 0, 1, 3])
