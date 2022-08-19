# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python
def find_outlier(integers):
    arr = [i for i in list(integers) if i % 2 == 0]
    arr2 = [i for i in list(integers) if i % 2 != 0]
    print(arr) if len(arr) == 1 else print(arr2)


find_outlier([2, 4, 6, 8, 10, 3])
