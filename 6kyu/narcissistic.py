# https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python
def narcissistic(value):
    print(sum([int(v)**len(str(value)) for v in str(value)]) == value)



narcissistic(153)
