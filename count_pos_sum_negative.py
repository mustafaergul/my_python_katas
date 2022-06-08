# https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python


def count_positives_sum_negatives(arr):
    return print(list(filter(lambda x: x != 0, [len([x for x in arr if x > 0]), sum([y for y in arr if y < 0])])))


count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])
