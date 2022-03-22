# https://www.codewars.com/kata/55edaba99da3a9c84000003b/train/python
def divisible_by(numbers, d):
    return list(filter(lambda n: n % d == 0, numbers))



divisible_by([1, 2, 3, 4, 5, 6], 2),[2, 4, 6])

divisible_by([1, 2, 3, 4, 5, 6], 3), [3, 6])
