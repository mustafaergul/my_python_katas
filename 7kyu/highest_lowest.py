def high_low(numbers):
    s = [int(n) for n in numbers.split(' ')]
    print(f"{max(s)} {min(s)}")
    # print(f"{sorted[-1]} {sorted[0]}")


high_low("1 2 3 4 5")
high_low("1 2 -3 4 5")
high_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
