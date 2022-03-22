# https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9
def number(lst):
    lst2 = []
    for ls in lst:
        n = 0
        lst2.append(f"{n}: {ls}")
    print(lst2)


number([1, 2, 3])
number([])
