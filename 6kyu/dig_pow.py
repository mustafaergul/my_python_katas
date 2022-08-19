# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python
def dig_pow(n, p):
    lst = []
    for i in [int(x) for x in str(n)]:
        lst.append(i**p)
        p += 1
    print(sum(lst)) if sum(lst) % n == 0 else print(-1)


dig_pow(89, 1)
dig_pow(92, 1)
dig_pow(46288, 1)
