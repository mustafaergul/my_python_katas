# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/python

def count_sheep(n):
    result = ""
    for a in range(1, n+1):
        result = result + f"{a} sheep..."
        a += 1
    return print(result)


count_sheep(0)
count_sheep(2)
count_sheep(5)
