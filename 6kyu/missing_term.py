# https://www.codewars.com/kata/find-the-missing-term-in-an-arithmetic-progression/python

def find_missing(arr):
    sub = arr[1] - arr[0]
    for i in arr:
        a = i + sub
        if a not in arr and a < max(arr):
            print(a)
        else:
            continue


find_missing([1, 3, 5, 9, 11])
