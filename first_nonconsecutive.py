# https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/python
def first_non_consec(arr):
    if not arr: return 0
    for i, v in enumerate(arr[:-1]):
        if v + 1 != arr[i + 1]:
            print(arr[i + 1])


first_non_consec([1, 2, 3, 4, 6, 7, 8])
first_non_consec([4, 6, 7, 8, 9, 11])
