# https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/python

def revese_seq(n):
    return print(list(reversed([n for n in range(1, n + 1) if n >= 1])))
# return list(range(n, 0, -1))


revese_seq(5)
