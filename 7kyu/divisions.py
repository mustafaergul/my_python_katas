def divisions(n, divisor):
    count = 0
    while n > 1:
        print(f'n: {n}')
        n = (n / divisor)
        count += 1
    print(f'result: {count-1}')
    print('------')


divisions(6, 2)
divisions(2450, 5)
